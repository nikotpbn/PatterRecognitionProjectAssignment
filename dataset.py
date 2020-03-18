import glob
import pathlib
import json

debug = False

# Path to the project file
current_dir = pathlib.Path().absolute()

# Paths to accelerometer and gyroscope dataset's
phone_accel_paths = "%s/wisdm-dataset/raw/phone/accel/*.txt" % current_dir
watch_accel_paths = "%s/wisdm-dataset/raw/watch/accel/*.txt" % current_dir
watch_gyro_paths = "%s/wisdm-dataset/raw/watch/gyro/*.txt" % current_dir
phone_gyro_paths = "%s/wisdm-dataset/raw/phone/gyro/*.txt" % current_dir

# Structure
dataset = {
    "phone": {
        "accel": {},
        "gyro": {}
    },
    "watch": {
        "accel": {},
        "gyro": {}
    }
}


# Function to import values for phone accelerometer dataset
def add_data(device, input_type, data):
    file_count = 0

    for f in data:
        # Open file and get the 1st line
        file = open(f)
        file_count += 1
        line = file.readline().split(",")

        # Get subject id from line
        subject_id = line[0]

        # Add subject to the dataset
        dataset[device][input_type][subject_id] = {}
        print(file_count, ": New subject created ->", subject_id) if debug is True else False
        sample = 0

        # Add samples of the subject to the dataset
        for line in file:
            # Split the data
            data_str = line.split(",")

            # Remove the last part of markup on the line --(";\n")--
            data_str[5] = data_str[5][0:len(data_str[5]) - 3]

            # Gather subject data
            data = {

                "activity_code": data_str[1],
                "timestamp": data_str[2],
                "x_axis": data_str[3],
                "y_axis": data_str[4],
                "z_axis": data_str[5]
            }

            # Add to dictionary
            dataset[device][input_type][subject_id][sample] = data
            sample += 1
        print("Finished adding samples for: ", subject_id) if debug is True else False


def write_json_file(filename):
    json_dataset = json.dumps(dataset)
    try:
        with open(filename, "w") as f:
            f.writelines(json_dataset)

        print(filename + " has been created.")
    except Exception as e:
        print(str(e))


# Function to print phone accelerometer data values
# TODO: Functions to print other values(?)
def print_phone_accel_dataset():
    for subject in dataset["phone"]["accel"]:
        for sample in dataset["phone"]["accel"][subject]:
            print(dataset["phone"]["accel"][subject][sample])


class Dataset:
    def __init__(self):
        # Load files
        phone_accel = glob.glob(phone_accel_paths)
        watch_accel = glob.glob(watch_accel_paths)
        watch_gyro = glob.glob(watch_gyro_paths)
        phone_gyro = glob.glob(phone_gyro_paths)

        print("Starting to add data...might take a few minutes!")
        # Add data to the set structure
        print("Adding phone accelerometer data...")
        add_data("phone", "accel", phone_accel)

        print("Adding watch accelerometer data...")
        #add_data("watch", "accel", watch_accel)

        print("Adding watch gyroscope data...")
        #add_data("watch", "gyro", watch_gyro)

        print("Adding phone gyroscope data...")
        #add_data("phone", "gyro", phone_gyro)

        print("Finished!")

        print("Writing the json file...might take a while!")
        write_json_file("dataset.json")
