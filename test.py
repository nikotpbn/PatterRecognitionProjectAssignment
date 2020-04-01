# Imports
from arff_dataset import Dataset
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Load the dataset
data = Dataset().get_database("PA")

# -------------------- Feature selection (K bests) --------------------
# Choosing the K best features
selector = SelectKBest(f_classif, k=5)
new_data = selector.fit_transform(data["data"], data["target"])
indexes = selector.get_support(indices=True)
new_label = [data["label"][i] for i in indexes]

# Update dataset replacing the old data and label to the bests
data["data"] = new_data
data["label"] = new_label

# TODO -------------------- Feature Reduction --------------------

# TODO -------------------- Classifiers --------------------

# -------------------- Print Results --------------------
print(data)