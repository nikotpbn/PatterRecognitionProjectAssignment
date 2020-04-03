# Imports
from arff_dataset import Dataset
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Load the dataset
data = Dataset().get_database("PA")

# -------------------- Feature selection (K bests) --------------------
# Choosing the K best features
selector = SelectKBest(f_classif, k=50)
new_data = selector.fit_transform(data["data"], data["target"])
indexes = selector.get_support(indices=True)
new_label = [data["label"][i] for i in indexes]

# Update dataset replacing the old data and label to the bests
data["data"] = new_data
data["label"] = new_label

# -------------------- Feature selection result --------------------
# print(new_data)
# print(new_label)

# -------------------- Feature Reduction --------------------
# Variables
correlation_rate = 0.9
maintained_features_idx = []
redundant_features_idx = []
redundant_features_label = []

# Correlation matrix with numpy
correlation_matrix = np.corrcoef(np.transpose(data["data"]))

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
new_data = np.transpose(data["data"])
new_label = data["label"]
for feature in redundant_features_idx:
    new_data = np.delete(new_data, feature, 0)
    redundant_features_label.append(data["label"][feature])
    new_label.pop(feature)
    for i in range(redundant_features_idx.index(feature), len(redundant_features_idx)):
        redundant_features_idx[i] = redundant_features_idx[i]-1
data["data"] = np.transpose(new_data)
data["label"] = new_label

# -------------------- Feature Reduction result --------------------
# print(data["data"])
# print(data["label"])
# print(redundant_features_label)

# TODO -------------------- PCA (Kaiser or Scree) --------------------

# -------------------- Classifiers --------------------
# TODO -------------------- Classifier: Minimum distance classifier (MDC) --------------------

# TODO -------------------- Classifier: Fisher LDA --------------------

# -------------------- Print Results or save code --------------------
# pandadataframe = pd.DataFrame(data=data["data"], columns=data["label"])
