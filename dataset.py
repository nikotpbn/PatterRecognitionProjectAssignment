import glob
import pathlib

debug = False


class Dataset:
    # Function to import values for phone accelerometer dataset
    def add_data(self, device, sensor, data):
        file_count = 0

        for f in data:
            # Open file and get the 1st line
            file = open(f)
            file_count += 1
            line = file.readline().split(",")

            # Get subject id from line
            subject_id = line[0]

            # Add subject to the dataset
            self.dataset[device][sensor][subject_id] = {}
            print(file_count, ": New subject created ->", subject_id) if debug is True else False
            sample = 0

            # Add samples of the subject to the dataset
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
                    self.dataset[device][sensor][subject_id][sample] = data
                    sample += 1

                except ValueError:
                    print("Could not parse string to float at sample ", sample, "for subject ", subject_id,
                          "Values: x->",
                          data_str[3], ", y->", data_str[4], ", z", data_str[5])

            print("Finished adding samples for: ", subject_id) if debug is True else False

    # Function to print phone accelerometer data values
    # TODO: Functions to print other values(?)
    def print_phone_accel_dataset(self):
        for subject in self.dataset["phone"]["accel"]:
            for sample in self.dataset["phone"]["accel"][subject]:
                print(self.dataset["phone"]["accel"][subject][sample])

    def __init__(self):
        # Path to the project file
        current_dir = pathlib.Path().absolute()

        # Paths to accelerometer and gyroscope dataset's
        phone_accel_paths = "%s/wisdm-dataset/raw/phone/accel/*.txt" % current_dir
        watch_accel_paths = "%s/wisdm-dataset/raw/watch/accel/*.txt" % current_dir
        watch_gyro_paths = "%s/wisdm-dataset/raw/watch/gyro/*.txt" % current_dir
        phone_gyro_paths = "%s/wisdm-dataset/raw/phone/gyro/*.txt" % current_dir

        # Load files
        phone_accel = glob.glob(phone_accel_paths)
        watch_accel = glob.glob(watch_accel_paths)
        watch_gyro = glob.glob(watch_gyro_paths)
        phone_gyro = glob.glob(phone_gyro_paths)

        # Structure
        self.dataset = {
            "phone": {
                "accel": {},
                "gyro": {}
            },
            "watch": {
                "accel": {},
                "gyro": {}
            }
        }

        print("Starting to add data...might take a few minutes!")
        # Add data to the set structure
        print("Adding phone accelerometer data...")
        self.add_data("phone", "accel", phone_accel)

        print("Adding watch accelerometer data...")
        # self.add_data("watch", "accel", watch_accel)

        print("Adding watch gyroscope data...")
        # self.add_data("watch", "gyro", watch_gyro)

        print("Adding phone gyroscope data...")
        # self.add_data("phone", "gyro", phone_gyro)

        print("Finished!")
