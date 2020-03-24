from dataset import Dataset
import numpy as np

# Frequency in Hz corresponding to 1s
max_series = 20

# Structure to hold the 20 time series values [x, y, z]
sample = []

# Import raw dataset
dataset = Dataset().dataset

# Structure
feature_dataset = {
    "phone": {
        "accel": {},
        "gyro": {}
    },
    "watch": {
        "accel": {},
        "gyro": {}
    }
}


# Method to gather high-level features
def get_features(data):
    # Set max and min variables for each axis
    x_max = data[0][0]
    x_min = data[0][0]
    y_max = data[0][1]
    y_min = data[0][1]
    z_max = data[0][2]
    z_min = data[0][2]

    for item in data:
        # Get max and min value from X
        aux = item[0]
        if aux > x_max:
            x_max = aux
        else:
            if aux < x_min:
                x_min = aux

        # Get max and min value from Y
        aux = item[1]
        if aux > y_max:
            y_max = aux
        else:
            if aux < y_min:
                y_min = aux

        # Get max and min value from Z
        aux = item[2]
        if aux > z_max:
            z_max = aux
        else:
            if aux < z_min:
                z_min = aux

    # TODO: Add feature data to high-level structure
    # Debug data
    print("Max value of X: ", x_max)
    print("Min value of X: ", x_min)
    print("Max value of Y: ", y_max)
    print("Min value of Y: ", y_min)
    print("Max value of Z: ", z_max)
    print("Min value of Z: ", z_min)

    # Calculate the high-level feature value
    x_feature = (x_max - x_min) / 10
    y_feature = (y_max - y_min) / 10
    z_feature = (z_max - z_min) / 10

    # Debug data
    print("X Feature: ", x_feature)
    print("Y Feature: ", y_feature)
    print("Z Feature: ", z_feature)


# Access raw data structure
for subject in dataset["phone"]["accel"]:
    # Variable to control the number of samples gathered
    sample_count = 0

    # Iterate through the raw_dataset
    for ts in dataset["phone"]["accel"][subject]:

        # Variable to hold sample x, y and z values
        x = dataset["phone"]["accel"][subject][ts]["x_axis"]
        y = dataset["phone"]["accel"][subject][ts]["y_axis"]
        z = dataset["phone"]["accel"][subject][ts]["z_axis"]
        sample_count += 1

        # Add values to sample set
        sample.append([x, y, z])

        # Just to debug data
        # if sample_count % 2 is 0:
        #     print(sample_set)

        # Reset the variables after 1s has passed (or 20 instances)
        if sample_count is max_series:
            # TODO: Gather the 1st feature from sample_set (max-min) / 10 for x, y and z axis
            sample_count = 0
            print(sample)
            print(len(sample))
            get_features(sample)
            sample = []

