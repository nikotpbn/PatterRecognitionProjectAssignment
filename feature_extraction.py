from dataset import Dataset
import math

debug = True

# Frequency in Hz corresponding to 1s and 10s windows
one_second = 20
ten_seconds = 200


# Method to gather high-level features
def get_features(data, code):
    # Variables
    binned_distribution_x = []
    binned_distribution_y = []
    binned_distribution_z = []
    avg_abs_diff_x = 0
    avg_abs_diff_y = 0
    avg_abs_diff_z = 0
    variance_x = 0
    variance_y = 0
    variance_z = 0
    item_count = 0
    total_x = 0
    total_y = 0
    total_z = 0

    # Set max and min variables for each axis
    x_max = data[0][0]
    x_min = data[0][0]
    y_max = data[0][1]
    y_min = data[0][1]
    z_max = data[0][2]
    z_min = data[0][2]

    # Iterate through data to find real max and min values of each axis
    for item in data:
        # Get total of {x, y, z} for average calculation
        total_x += item[0]
        total_y += item[1]
        total_z += item[2]

        # Check max and min value for X axis
        aux = item[0]
        if aux > x_max:
            x_max = aux
        else:
            if aux < x_min:
                x_min = aux

        # Check max and min value for Y axis
        aux = item[1]
        if aux > y_max:
            y_max = aux
        else:
            if aux < y_min:
                y_min = aux

        # Check max and min value for Z axis
        aux = item[2]
        if aux > z_max:
            z_max = aux
        else:
            if aux < z_min:
                z_min = aux

        # Track the number of iteration o data items
        item_count += 1

        # Reaching one second (20 instances) add values to the binned distribution vector
        if item_count % one_second is 0:
            # Calculate the high-level feature value
            x_feature = (x_max - x_min) / 10
            y_feature = (y_max - y_min) / 10
            z_feature = (z_max - z_min) / 10

            # Add the calculated values to binned distribution vectors
            binned_distribution_x.append(x_feature)
            binned_distribution_y.append(y_feature)
            binned_distribution_z.append(z_feature)

    # Calculate averages
    avg_x = total_x / ten_seconds
    avg_y = total_y / ten_seconds
    avg_z = total_z / ten_seconds

    for item in data:
        # Calculate Variance Numerator
        variance_x += math.pow((item[0] - avg_x), 2)
        variance_y += math.pow((item[1] - avg_y), 2)
        variance_z += math.pow((item[2] - avg_z), 2)

        # Calculate MAD (Mean/average Absolute Difference/Deviation) Numerator
        avg_abs_diff_x = abs(item[0] - avg_x)
        avg_abs_diff_y = abs(item[1] - avg_y)
        avg_abs_diff_z = abs(item[2] - avg_z)

    variance_x /= ten_seconds
    variance_y /= ten_seconds
    variance_z /= ten_seconds

    avg_abs_diff_x /= ten_seconds
    avg_abs_diff_y /= ten_seconds
    avg_abs_diff_z /= ten_seconds

    # Calculate standard deviation
    deviation_x = math.sqrt(variance_x)
    deviation_y = math.sqrt(variance_y)
    deviation_z = math.sqrt(variance_z)

    # Structure to be returned and added to high-level dataset
    high_level_data = {
        "activity_code": code,
        "x": binned_distribution_x,
        "y": binned_distribution_y,
        "z": binned_distribution_z,
        "avg": [avg_x, avg_y, avg_z],
        "variance": [variance_x, variance_y, variance_z],
        "deviation": [deviation_x, deviation_y, deviation_z],
        "mad": [avg_abs_diff_x, avg_abs_diff_y, avg_abs_diff_z]
    }

    return high_level_data


class HLDataset:
    def add_data(self, device, sensor, data):
        # Structure to hold the 200 time series values [x, y, z]
        ten_seconds_sample = []
        # one_second_sample = []

        # Access raw data structure
        for subject in data[device][sensor]:
            # Variable to control the number of samples gathered
            sample_count = 0
            window = 0

            # Add subject to high-level feature structure
            self.dataset[device][sensor][subject] = {}

            # Iterate through the raw_dataset
            for ts in data[device][sensor][subject]:

                if sample_count is 1:
                    # Get the item label
                    label = data[device][sensor][subject][ts]["activity_code"]

                # Variable to hold sample x, y and z values
                x = data[device][sensor][subject][ts]["x_axis"]
                y = data[device][sensor][subject][ts]["y_axis"]
                z = data[device][sensor][subject][ts]["z_axis"]
                sample_count += 1

                # Add values to sample set
                ten_seconds_sample.append([x, y, z])

                # Extract features and reset the variables after 10s (200 instances)
                if sample_count is ten_seconds:
                    hld = get_features(ten_seconds_sample, label)

                    # If debug variable is true, print data
                    if debug:
                        print("Window: ", window)
                        print("Activity Code: ", hld["activity_code"])
                        print("Binned X: ", hld["x"])
                        print("Binned Y: ", hld["y"])
                        print("Binned Z: ", hld["z"])
                        print("Average {X, Y, Z}: ", hld["avg"])
                        print("Variance {X, Y, Z}: ", hld["variance"])
                        print("Standard Deviation {X, Y, Z}: ", hld["deviation"])
                        print("MAD: ", hld["mad"])
                        print("---------------------------------------------------------------------------------------")

                    # Add high-level data to main structure and reset variables
                    self.dataset[device][sensor][subject][window] = hld
                    window += 1
                    sample_count = 0
                    ten_seconds_sample = []

    def __init__(self):
        # Import raw dataset
        raw_dataset = Dataset().dataset

        # Structure to hold high-level features
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

        # Extract data from raw dataset and add to new structure
        print("Extracting features for phone accelerometer")
        self.add_data("phone", "accel", raw_dataset)

        print("Extracting features for phone gyroscope")
        # self.add_data("phone", "gyro", raw_dataset)

        print("Extracting features for watch accelerometer")
        # self.add_data("watch", "accel", raw_dataset)

        print("Extracting features for watch gyroscope")
        # self.add_data("watch", "gyro", raw_dataset)

        print("Feature extraction finished!")
