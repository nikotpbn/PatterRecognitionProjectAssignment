# Imports
import re
import glob
import pathlib
import numpy as np


# Class to read database files into an Object
class Dataset:
    # Constructor Method
    def __init__(self):
        # Private Variables
        self.__phone_gyro = None
        self.__watch_gyro = None
        self.__phone_accel = None
        self.__watch_accel = None

        # Public Variables
        self.database_selected_str = None
        self.database_selected_int = None
        self.scenario_selected_str = None
        self.scenario_selected_int = None
        self.feature_selection_method_str = None
        self.feature_selection_method_int = None
        self.features_excluded_by_feature_reduction = None

        # Structure
        self.dataset = {
            "data": {},
            "label": {},
            "target": {}
        }

        # Path to the project file
        current_dir = pathlib.Path().absolute().parent

        # Paths to accelerometer and gyroscope dataset's
        phone_gyro_paths = "%s/wisdm-dataset/arff_files/phone/gyro/*.arff" % current_dir
        watch_gyro_paths = "%s/wisdm-dataset/arff_files/watch/gyro/*.arff" % current_dir
        watch_accel_paths = "%s/wisdm-dataset/arff_files/watch/accel/*.arff" % current_dir
        phone_accel_paths = "%s/wisdm-dataset/arff_files/phone/accel/*.arff" % current_dir

        # Load files
        self.__phone_gyro = glob.glob(phone_gyro_paths)
        self.__watch_gyro = glob.glob(watch_gyro_paths)
        self.__phone_accel = glob.glob(phone_accel_paths)
        self.__watch_accel = glob.glob(watch_accel_paths)

    # Private method to read data
    def __add_data(self, data_files, device, sensor):
        # Variables
        data = []
        label = []
        target = []
        file_number = 1

        # Read each file in vector data_files
        for data_file in data_files:
            file = open(data_file)
            # Variable to control the lines in the file, to separate the sample from the label
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

                    # Eliminate the target (activity - first value)
                    # And the subject (individual - last value) from the sample
                    read.pop(0)
                    read.pop(-1)

                    # Add values to data array
                    data.append(read)

                line += 1

            file_number += 1

        # Add data array into the structure
        self.dataset["data"] = np.asarray(data).astype(np.float64)
        self.dataset["target"] = np.asarray(target)
        self.dataset["label"] = np.asarray(label)

    # Choose which dataset will be used
    def choose_data(self, data_load):
        # Save the selected database
        self.database_selected_int = data_load

        # Load Dataset
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

    # Pre-process data in function of the scenario:
    # Scenario A: distinguish the "Jogging" activity from the others activities

    # Scenario B: divide the dataset into 3 different classes, Non-hand-oriented activities ,
    #   General Hand-oriented activities, Eating Hand-oriented activities and (Delete the class
    #   Sitting "D" which does not belong to any of the three classes)

    # Scenario C: distinguish all the 18 activities
    def scenario_pre_processing(self, scenario):
        # Save selected scenario
        self.scenario_selected_int = scenario

        # Scenario A: Label jogging as "A" others as "B"
        if scenario == 1:
            self.scenario_selected_str = "Scenario A"
            # Keep the Jogging activity (B) as B class and change all other activities for class A
            for i in range(0, len(self.dataset["data"])):
                if self.dataset["target"][i] != "B":
                    self.dataset["target"][i] = "A"

        # Scenario B: Label activities as A, B and C
        if scenario == 2:
            # Save selected scenario
            self.scenario_selected_str = "Scenario B"

            # Separate classes
            class_for_delete = []
            class_non_hand_oriented = ["A", "B", "C", "E", "M"]
            class_eating_hand_oriented = ["J", "H", "L", "I", "K"]
            class_general_hand_oriented = ["P", "O", "F", "Q", "R", "G", "S"]

            # Label divided classes
            for i in range(0, len(self.dataset["data"])):
                if self.dataset["target"][i] in class_non_hand_oriented:
                    self.dataset["target"][i] = "A"

                if self.dataset["target"][i] in class_general_hand_oriented:
                    self.dataset["target"][i] = "B"

                if self.dataset["target"][i] in class_eating_hand_oriented:
                    self.dataset["target"][i] = "C"

                # Delete the class that does not belong to any other activity
                if self.dataset["target"][i] == "D":
                    class_for_delete.append(i)

            # Deletion of readings and targets
            self.dataset["data"] = np.delete(self.dataset["data"], class_for_delete, axis=0)
            self.dataset["target"] = np.delete(self.dataset["target"], class_for_delete, axis=0)

        # Scenario C - No changes on data, because it is already divided correctly
        if scenario == 3:
            self.scenario_selected_str = "Scenario C"

    # Method to save feature selection method
    def set_feature_selection_method(self, feature_selection_method):
        # Save feature selection method
        self.feature_selection_method_int = feature_selection_method

        # K-bests method
        if feature_selection_method == 1:
            self.feature_selection_method_str = "K-bests"
        # Kruskal-Wallis method
        if feature_selection_method == 2:
            self.feature_selection_method_str = "Kruskal-Wallis"

    # Save features excluded by redundancy measure
    def set_features_excluded_by_feature_reduction(self, features_excluded):
        self.features_excluded_by_feature_reduction = features_excluded
