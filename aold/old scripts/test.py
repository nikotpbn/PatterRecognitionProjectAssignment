# Imports
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from arff_dataset import Dataset
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix

from sklearn.covariance import MinCovDet, EmpiricalCovariance

# Load the dataset and variables
scenario = "A"
data = Dataset().get_database("PA")

# -------------------- Scenario Definition --------------------
if scenario == "A":
    for i in range(0, len(data["target"])):
        if data["target"][i] != "A":
            data["target"][i] = "B"

# -------------------- Feature selection (K bests) --------------------
# Choosing the K best features
selector = SelectKBest(f_classif, k=50)
new_data = selector.fit_transform(data["data"], data["target"])
indexes = selector.get_support(indices=True)
new_label = [data["label"][i] for i in indexes]

# Update dataset replacing the old data and label to the bests
data["data"] = new_data
data["label"] = new_label

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

# -------------------- PCA (Kaiser or Scree) --------------------
# PCA for reduction analysis
pca = PCA()
pca.fit(data["data"])

# Plots
# Preparations to plot
x_values = np.arange(1, len(data["label"]) + 1)
# Plot Eigenvalues
plt.plot(x_values, pca.singular_values_, 'ro')
plt.title('Principal Component Analysis (PCA)')
plt.xlabel('Principal Components')
plt.ylabel('Eigenvalues')
plt.show()
# Plot percentage of variance graphic
plt.plot(x_values, (np.cumsum(pca.explained_variance_)/sum(pca.explained_variance_))*100, 'ro')
plt.title('Principal Component Analysis (PCA)')
plt.xlabel('Principal Components')
plt.ylabel('Percentage of variance')
plt.show()

# PCA application
n_features = len(data["label"]) - 2
pca = PCA(n_components=n_features)
new_data = pca.fit_transform(data["data"])
data["data"] = new_data

# -------------------- Classifiers --------------------
# Variables
numbers_runs = 1
numbers_subsets = 2
classifier = 'MDC'
results = {
    'Misclassification': 0,
    'Sensitivity': 0,
    'Specificity': 0
}
for i in range(0, numbers_runs):
    # Apply K-fold
    kf = KFold(n_splits=numbers_subsets)
    misclassification = 0

    # K-fold Executions
    for idx_train, idx_test in kf.split(data["data"], data["target"]):
        # Train data
        x_train = [data["data"][idx] for idx in idx_train]
        x_train = np.asarray(x_train).astype(np.float64)
        y_train = [data["target"][idx] for idx in idx_train]
        # Test data
        x_test = [data["data"][idx] for idx in idx_test]
        x_test = np.asarray(x_test).astype(np.float64)
        y_test = [data["target"][idx] for idx in idx_test]
        # TODO -------------------- Classifier: Minimum distance classifier (MDC) --------------------
        if classifier == 'MDC':
            # Transpose x_train and y_train to: feature x readings
            train_x = np.transpose(x_train)
            test_x = np.transpose(x_test)

            # Get indexes of the classes
            ix_w1 = np.nonzero(np.in1d(y_train, 'A'))
            ix_w2 = np.nonzero(np.in1d(y_train, 'B'))

            # Calculate the mean of features for each pattern
            mu1 = np.mean(train_x[:, ix_w1], 2)
            mu2 = np.mean(train_x[:, ix_w2], 2)

            # print("MU1", mu1.shape)
            # print("MU2", mu2.shape)

            # Array to hold prediction
            predict = []

            # Iterate through test data
            for k in range(0, len(test_x[1])):
                # 1st part of euclidian general formula
                test_sample = np.transpose(np.array([test_x[:, k]]))
                g1 = mu1.transpose().dot(test_sample)
                g2 = mu1.transpose().dot(test_sample)

                # 2nd part of euclidian general formula
                mm1 = mu1.transpose().dot(mu1)
                mm2 = mu1.transpose().dot(mu2)

                g1 = g1 - mm1
                g2 = g1 - mm2

                if g1 >= g2:
                    predict.append('A')
                    print("For k=",  k, ".Prediction was A")
                else:
                    predict.append('B')
                    # print("For k=",  k, ".Prediction was B")

            cm = confusion_matrix(y_test, predict)

        # -------------------- Classifier: Fisher LDA --------------------
        if classifier == 'fisherLDA':
            # Classifier training
            lda = LinearDiscriminantAnalysis().fit(x_train, y_train)
            # Classifier test
            predict = lda.predict(x_test)
            cm = confusion_matrix(y_test, predict)
        # Results calculations
        fp = round(sum(cm.sum(axis=0) - np.diag(cm)) / len(cm.sum(axis=0) - np.diag(cm)))
        fn = round(sum(cm.sum(axis=1) - np.diag(cm)) / len(cm.sum(axis=1) - np.diag(cm)))
        tp = round(sum(np.diag(cm)) / len(np.diag(cm)))
        tn = cm.sum() - (fp + fn + tp)
        results['Misclassification'] += (fp + fn) / (tp + tn + fp + fn)
        misclassification += (fp + fn) / (tp + tn + fp + fn)
        results['Sensitivity'] += fp / (tp + fn)
        results['Specificity'] += fp / (fp + tn)

# End results calculations
results['Misclassification'] = (results['Misclassification'] / (numbers_runs * numbers_subsets)) * 100
results['Sensitivity'] = results['Sensitivity'] / (numbers_runs * numbers_subsets)
results['Specificity'] = results['Specificity'] / (numbers_runs * numbers_subsets)

# -------------------- Print Results or save code --------------------
print(results)
# pandadataframe = pd.DataFrame(data=data["data"], columns=data["label"])