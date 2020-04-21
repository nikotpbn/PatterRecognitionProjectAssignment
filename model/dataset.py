# Imports
import glob
import pathlib
import re
import numpy as np


# Class to work into the database
class Dataset:
    # Initialization
    def __init__(self):
        # Attributes
        # Inside
        self.__phone_accel = None
        self.__phone_gyro = None
        self.__watch_accel = None
        self.__watch_gyro = None
        # Outside
        self.database_selected_str = None
        self.database_selected_int = None
        self.scenario_selected_str = None
        self.scenario_selected_int = None
        self.feature_selection_method_str = None
        self.feature_selection_method_int = None
        self.features_excluded_by_feature_reduction = None
        self.dataset = {
            "data": {},
            "target": {},
            "label": {}
        }

        # Path to the project file
        current_dir = pathlib.Path().absolute().parent

        # Paths to accelerometer and gyroscope dataset's
        phone_accel_paths = "%s/wisdm-dataset/arff_files/phone/accel/*.arff" % current_dir
        phone_gyro_paths = "%s/wisdm-dataset/arff_files/phone/gyro/*.arff" % current_dir
        watch_accel_paths = "%s/wisdm-dataset/arff_files/watch/accel/*.arff" % current_dir
        watch_gyro_paths = "%s/wisdm-dataset/arff_files/watch/gyro/*.arff" % current_dir

        # Load files
        self.__phone_accel = glob.glob(phone_accel_paths)
        self.__phone_gyro = glob.glob(phone_gyro_paths)
        self.__watch_accel = glob.glob(watch_accel_paths)
        self.__watch_gyro = glob.glob(watch_gyro_paths)

    # Add the data into the attribute
    def __add_data(self, data_files, device, sensor):
        # Variable
        file_number = 1
        data = []
        target = []
        label = []

        # Read each data in vector data_files
        for data_file in data_files:
            file = open(data_file)
            # Variable to control the lines in the file, to separate the sample to the label
            line = 1
            # Read each line in each file
            for sample in file:
                if 4 <= line <= 94 and file_number == 1:
                    # Search for labels of each attribute
                    found = re.search('"(.+?)"', sample).group(1)
                    label.append(found)
                elif line > 97 and sample is not None:
                    # Work in each sample in the file
                    read = sample.split(",")
                    # Add the first value in the sample (activity) in the vector target
                    target.append(read[0])
                    # Eliminate the target (activity - first value) and the subject (individual - last value) from the
                    # sample
                    read.pop(0)
                    read.pop(-1)
                    # Add the vector read in the vector data
                    data.append(read)
                line += 1
            file_number += 1

        # Add the data read into the dataset attribute
        self.dataset["data"] = np.asarray(data).astype(np.float64)
        self.dataset["target"] = np.asarray(target)
        self.dataset["label"] = np.asarray(label)

    # Choose what dataset will be used
    def choose_data(self, data_load):
        # Set attributes
        self.database_selected_int = data_load

        # Database
        # Phone-accelerometer data
        if data_load == 1:
            self.database_selected_str = "Accelerometer from phone"
            self.__add_data(self.__phone_accel, "phone", "accel")
        # Phone-gyroscope data
        if data_load == 2:
            self.database_selected_str = "Gyroscope from phone"
            self.__add_data(self.__phone_gyro, "phone", "gyro")
        # Watch-accelerometer data
        if data_load == 3:
            self.database_selected_str = "Accelerometer from watch"
            self.__add_data(self.__watch_accel, "watch", "accel")
        # Watch-gyroscope data
        if data_load == 4:
            self.database_selected_str = "Gyroscope from watch"
            self.__add_data(self.__watch_gyro, "watch", "gyro")

        return self

    # Apply pre-processing in order of the scenario chosen:
    # Scenario A: distinguish the "Jogging" activity (Class B) from the others activities (A and C - S)
    # Scenario B: divide the hole dataset into 3 different classes, Non-hand-oriented activities (walking - A, jogging
    #   - B, stairs - C, standing - E, kicking - M), General Hand-oriented activities (dribbling - P, playing catch - O,
    #   typing - F, writing - Q, clapping - R, brushing teeth - G, folding clothes - S), Eating Hand-oriented activities
    #   (eating pasta - J, eating soup - H, eating sandwich - L, eating chips - I, drinking - K) and delete the class
    #   Sitting - D
    # Scenario C: distinguish all the 18 activities
    def scenario_pre_processing(self, scenario):
        # Set attributes
        self.scenario_selected_int = scenario
        # Scenarios
        # Scenario A
        if scenario == 1:
            self.scenario_selected_str = "Scenario A"
            # Keep the Jogging activity (B) as B class and change all other activities for class A
            for i in range(0, len(self.dataset["data"])):
                if self.dataset["target"][i] != "B":
                    self.dataset["target"][i] = "A"
        # Scenario B
        if scenario == 2:
            self.scenario_selected_str = "Scenario B"
            class_non_hand_oriented = ["A", "B", "C", "E", "M"]
            class_general_hand_oriented = ["P", "O", "F", "Q", "R", "G", "S"]
            class_eating_hand_oriented = ["J", "H", "L", "I", "K"]
            class_for_delete = []
            # Divide 17 of 18 class's into 3 big "class's" and then exclude the last one from the data and target
            for i in range(0, len(self.dataset["data"])):
                if self.dataset["target"][i] in class_non_hand_oriented:
                    self.dataset["target"][i] = "A"
                if self.dataset["target"][i] in class_general_hand_oriented:
                    self.dataset["target"][i] = "B"
                if self.dataset["target"][i] in class_eating_hand_oriented:
                    self.dataset["target"][i] = "C"
                if self.dataset["target"][i] == "D":
                    class_for_delete.append(i)
            # Delete the class Sitting (D) from the data and target
            self.dataset["data"] = np.delete(self.dataset["data"], class_for_delete, axis=0)
            self.dataset["target"] = np.delete(self.dataset["target"], class_for_delete, axis=0)
        # Scenario C - Don't need to do anything, because the data already divide correctly
        if scenario == 3:
            self.scenario_selected_str = "Scenario C"

    # This method just set the feature selection method chosen to be used
    def set_feature_selection_method(self, feature_selection_method):
        self.feature_selection_method_int = feature_selection_method
        # K-bests method
        if feature_selection_method == 1:
            self.feature_selection_method_str = "K-bests"
        # Kruskal-Wallis method
        if feature_selection_method == 2:
            self.feature_selection_method_str = "Kruskal-Wallis"

    def set_features_excluded_by_feature_reduction(self, features_excluded):
        self.features_excluded_by_feature_reduction = features_excluded
