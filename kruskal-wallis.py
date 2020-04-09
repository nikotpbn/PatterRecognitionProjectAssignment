# Imports
from arff_dataset import Dataset
import numpy as np
from scipy import stats

# Load the dataset
dataset = Dataset().get_database("PA")
user_num_features = 50

# Get information from the dataset
data = np.transpose(dataset["data"])
targets = dataset["target"]
labels = dataset["label"]
new_data = []
new_labels = []

# Array to hold H values and indexes from Kruskal-Wallis method
h_array = []

# -------------------- Feature selection (Kruskal-Wallis) --------------------
# Compute H value for each pattern
for i in range(0, len(data)):
    k = stats.kruskal(data[i, :], targets)
    h_value = k[0]
    values = (h_value, i)

    # Add index and H value to array
    h_array.append(values)

# Sort array in crescent order
sorted_h = sorted(h_array, key=lambda h_val: h_val[0])

# Select patterns using index from computed H value
for i in range(0, user_num_features):
    # Get index from sorted H array
    index = sorted_h[i][1]

    # Use index value to get the pattern from data matrix and label from labels array
    pattern = data[index].tolist()
    label = labels[index]

    # Add values to new arrays
    new_data.append(pattern)
    new_labels.append(label)

# Update dataset replacing the old data and labels
dataset["data"] = np.transpose(np.array(new_data))
dataset["label"] = new_labels

# -------------------- Feature Reduction --------------------
# Variables
correlation_rate = 0.9
maintained_features_idx = []
redundant_features_idx = []
redundant_features_label = []

# Correlation matrix with numpy
correlation_matrix = np.corrcoef(np.transpose(dataset["data"]))

# Upper diagonal interaction of the matrix. If the correlation score are out of +-correlation_rate then the feature in
# the line is maintained and the feature in the column is deleted.
for i in range(0, len(correlation_matrix)):
    for j in range(i + 1, len(correlation_matrix[i])):
        if correlation_matrix[i][j] >= correlation_rate or correlation_matrix[i][j] <= -correlation_rate:
            if i not in maintained_features_idx and i not in redundant_features_idx:
                maintained_features_idx.append(i)
            if j not in redundant_features_idx:
                redundant_features_idx.append(j)
        else:
            if i not in maintained_features_idx and i not in redundant_features_idx:
                maintained_features_idx.append(i)

# Exclude the features highly correlated from the matrix, fixes the label vector and prepare the redundant vector with
# their respective labels
new_data = np.transpose(dataset["data"])
new_label = dataset["label"]
for feature in redundant_features_idx:
    new_data = np.delete(new_data, feature, 0)
    redundant_features_label.append(dataset["label"][feature])
    new_label.pop(feature)
    for i in range(redundant_features_idx.index(feature), len(redundant_features_idx)):
        redundant_features_idx[i] = redundant_features_idx[i]-1
dataset["data"] = np.transpose(new_data)
dataset["label"] = new_label

# -------------------- Feature Reduction result --------------------
print(len(dataset["data"]))
print(len(dataset["data"][1]))
