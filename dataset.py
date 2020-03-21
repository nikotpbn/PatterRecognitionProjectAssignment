import glob
import pathlib

# Variable to help debug code
debug = False

# Path to the project folder
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


# Function to import data from txt files
def add_data(device, sensor, data):

    for f in data:
        # Open file and get the 1st line
        file = open(f)
        line = file.readline().split(",")

        # Get subject id from line
        subject_id = line[0]

        # Add subject to the dataset
        dataset[device][sensor][subject_id] = {}
        # print(file_count, ": New subject created ->", subject_id) if debug is True else False
        sample = 0

        # Add subject sample values to the dataset
        for line in file:
            # Split the data
            data_str = line.split(",")

            # Remove the last part of markup on the line --(";\n")--
            data_str[5] = data_str[5][0:len(data_str[5]) - 2]

            # Try to parse data from string to float
            try:
                x = float(data_str[3])
                y = float(data_str[4])
                z = float(data_str[5])

                # Assign subject data
                data = {
                    "activity_code": data_str[1],
                    "timestamp": data_str[2],
                    "x_axis": x,
                    "y_axis": y,
                    "z_axis": z
                }

                # Add to dataset dictionary
                dataset[device][sensor][subject_id][sample] = data
                sample += 1

            except ValueError:
                print("Could not parse string to float at sample ", sample, "for subject ", subject_id, "Values: x->",
                      data_str[3], ", y->", data_str[4], ", z", data_str[5])

        print("Finished adding ", sample, "samples for: ", subject_id) if debug is True else False


# Function to print phone accelerometer data values
# TODO: Change function to print generalized values is necessary(?)
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
        # Read all dataset's
        print("Reading phone accelerometer data...")
        add_data("phone", "accel", phone_accel)

        print("Reading watch accelerometer data...")
        add_data("watch", "accel", watch_accel)

        print("Reading watch gyroscope data...")
        add_data("watch", "gyro", watch_gyro)

        print("Reading phone gyroscope data...")
        add_data("phone", "gyro", phone_gyro)

        print("Finished!")