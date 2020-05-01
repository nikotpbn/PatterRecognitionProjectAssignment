# Imports
import matplotlib
import numpy as np
from scipy import stats
from sklearn import neighbors, svm
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, multilabel_confusion_matrix
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import SelectKBest
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

matplotlib.use("TkAgg")


# Kbest method for feature selection
def kbest(data, n_features):
    # Choosing the K-best features to be used
    selector = SelectKBest(f_classif, k=n_features)
    new_data = selector.fit_transform(data["data"], data["target"])

    # Recover from the model the indexes that represent the features maintained
    # and keep them in the label vector
    indexes = selector.get_support(indices=True)
    new_label = [data["label"][i] for i in indexes]

    # Update dataset replacing the old data and labels
    data["data"] = new_data
    data["label"] = new_label

    return data


# Kruskal-Wallis method for feature selection
def kruskal_wallis(data, n_features):
    # Variables
    new_data = []
    new_labels = []
    labels = data["label"]
    targets = data["target"]
    t_data = np.transpose(data["data"])

    # Array to hold H values and indexes from Kruskal-Wallis method
    h_array = []

    # Compute H value for each pattern
    for i in range(0, len(t_data)):
        k = stats.kruskal(t_data[i, :], targets)
        h_value = k[0]
        values = (h_value, i)

        # Add index and H value to array
        h_array.append(values)

    # Sort array in crescent order
    sorted_h = sorted(h_array, key=lambda h_val: h_val[0])

    # Select patterns using index from computed H value
    for i in range(0, n_features):
        # Get index from sorted H array
        index = sorted_h[i][1]

        # Use index value to get the pattern from data matrix and label from labels array
        pattern = t_data[index].tolist()
        label = labels[index]

        # Add values to new arrays
        new_data.append(pattern)
        new_labels.append(label)

    # Update dataset replacing the old data and labels
    data["data"] = np.transpose(np.array(new_data))
    data["label"] = new_labels

    return data


# Method for redundancy measure in order to eliminate correlated features
def redundancy_measure(data):
    # Variables
    correlation_rate = 0.9
    maintained_features_idx = []
    redundant_features_idx = []
    redundant_features_label = []

    # Correlation matrix with numpy
    correlation_matrix = np.corrcoef(np.transpose(data["data"]))

    # Upper diagonal interaction of the matrix. If the correlation score are out of +-correlation_rate then the feature
    # in the line is maintained and the feature in the column is deleted.
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

    # Exclude the features highly correlated from the matrix, fixes the label vector and prepare the redundant vector
    # with their respective labels
    new_data = np.transpose(data["data"])
    new_label = data["label"]
    for feature in redundant_features_idx:
        new_data = np.delete(new_data, feature, 0)
        redundant_features_label.append(data["label"][feature])
        new_label.pop(feature)
        for i in range(redundant_features_idx.index(feature), len(redundant_features_idx)):
            redundant_features_idx[i] = redundant_features_idx[i] - 1
    data["data"] = np.transpose(new_data)
    data["label"] = new_label
    return data, redundant_features_label


# Method to run PCA feature analysis (plots)
def pca_analysis(data):
    # PCA for reduction analysis
    pca = PCA()
    pca.fit(data["data"])

    # Set up data to plot
    x_values = np.arange(1, len(data["label"]) + 1)

    return pca.explained_variance_, x_values, pca.singular_values_


# Method to apply PCA feature reduction
def run_pca(data, n_features):
    # PCA application
    pca = PCA(n_components=n_features)
    new_data = pca.fit_transform(data["data"])
    data["data"] = new_data

    return data


# Minimum distance classifier (MDC)
def minimum_distance_classifier(x_train, y_train, x_test, y_test):
    # Variables to hold prediction and mean values of features
    prediction = []
    means = []

    # Transpose x_train and y_train to feature x readings
    train_x = np.transpose(x_train)
    test_x = np.transpose(x_test)

    # Get labels dynamically for scenario A, B and C
    activity_labels = np.unique(y_train)

    # Calculate means for each feature
    for i in range(0, len(activity_labels)):
        indexes = np.nonzero(np.in1d(y_train, activity_labels[i]))
        means.append(np.mean(train_x[:, indexes], 2))

    # Iterate through test data
    for k in range(0, len(test_x[1])):
        # Variable to hold Euclidian distance general formula values
        g_value = []

        # Get the sample to classify
        test_sample = np.transpose(np.array([test_x[:, k]]))

        # Apply Euclidian general formula
        for i in range(0, len(activity_labels)):
            g_value.append(np.subtract(means[i].transpose().dot(test_sample),
                                       np.dot(0.5, means[i].transpose().dot(means[i]))))

        # Index of the maximum value out of g_value vector
        max_index = g_value.index(max(g_value))

        # Use the index to add label to prediction array
        prediction.append(activity_labels[max_index])

    return prediction


# Fisher Discriminant Analisys (Fisher LDA)
def fisher_discriminant_analisys(x_train, y_train, x_test, y_test):
    # Classifier training
    lda = LinearDiscriminantAnalysis().fit(x_train, y_train)

    # Classifier test
    prediction = lda.predict(x_test)

    return prediction


# Naive-Bayes Classifier
def bayes_classifier(x_train, y_train, x_test, y_test):
    # Create object
    gnb = GaussianNB()

    # Training and Classification
    prediction = gnb.fit(x_train, y_train).predict(x_test)

    return prediction


# KNN Classifier
def k_nearest_neighbors(x_train, y_train, x_test, y_test, constant):
    # K Constant of KNN classifier
    k = int(constant)

    # Training and classification
    for weights in ['uniform', 'distance']:
        clf = neighbors.KNeighborsClassifier(k, weights=weights)

        clf.fit(x_train, y_train)
        prediction = clf.predict(x_test)

    return prediction


# SVM Classifier
def support_vector_machines(x_train, y_train, x_test, y_test, constant):
    # C Constant of SVM classifier
    c = float(constant)

    # Training
    clf = svm.SVC(kernel='linear', C=c)
    clf.fit(x_train, y_train)

    # Classification
    prediction = clf.predict(x_test)

    return prediction


# Method to calculate the error of the classifier
def cm_derivations_calculation(cm, cm_derivations):
    # Error calculation
    false_positive = round(sum(cm.sum(axis=0) - np.diag(cm)) / len(cm.sum(axis=0) - np.diag(cm)))
    false_negative = round(sum(cm.sum(axis=1) - np.diag(cm)) / len(cm.sum(axis=1) - np.diag(cm)))
    true_positive = round(sum(np.diag(cm)) / len(np.diag(cm)))
    true_negative = cm.sum() - (false_positive + false_negative + true_positive)

    # Dictionary update
    cm_derivations["fp"] = false_positive
    cm_derivations["fn"] = false_negative
    cm_derivations["tp"] = true_positive
    cm_derivations["tn"] = true_negative

    print("OLD")
    print("TP:", cm_derivations["tp"])
    print("FN:", cm_derivations["fn"])
    print("FP:", cm_derivations["fp"])
    print("TN:", cm_derivations["tn"])

    return cm_derivations


def performance_measurement(target, prediction, scenario, performance):
    if scenario == 1:
        cm = confusion_matrix(target, prediction, labels=['A', 'B'])
        tn, fp, fn, tp = cm.ravel()
        performance["tn"] = tn
        performance["fp"] = fp
        performance["fn"] = fn
        performance["tp"] = tp

    elif scenario == 2:
        cm = multilabel_confusion_matrix(target, prediction, labels=['A', 'B', 'C'])
        performance["tn"] = cm[:, 0, 0]
        performance["fn"] = cm[:, 1, 0]
        performance["tp"] = cm[:, 1, 1]
        performance["fp"] = cm[:, 0, 1]

    else:
        cm = multilabel_confusion_matrix(target, prediction, labels=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                                                                     'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S'])
        performance["tn"] = cm[:, 0, 0]
        performance["fn"] = cm[:, 1, 0]
        performance["tp"] = cm[:, 1, 1]
        performance["fp"] = cm[:, 0, 1]

    # True Positive Rate (TPR) | Sensitivity
    performance['sensitivity'] = performance["tp"] / (performance["tp"] + performance["fn"])

    # True Negative Rate (TNR) | Specificity
    performance['specificity'] = performance["tn"] / (performance["tn"] + performance["fp"])

    # Misclassification
    mc = (performance["fp"] + performance["fn"]) / (performance["fp"] + performance["fn"] + performance["tp"] + performance["tn"])
    performance['avg_misclassification'] += mc
    performance['misclassification_per_run'].append(mc)

    # Accuracy
    performance['accuracy'] = (performance["tp"] + performance["tn"]) / (performance["fp"] + performance["fn"] + performance["tp"] + performance["tn"])

    print(cm)
    return performance


# Method to calculate the misclassification error
def misclassification(cm_derivations):
    numerator = cm_derivations["fp"] + cm_derivations["fn"]
    denominator = cm_derivations["tp"] + cm_derivations["tn"] + cm_derivations["fp"] + cm_derivations["fn"]

    return numerator / denominator


# Method to calculate the sensitivity
def sensitivity(cm_derivations):

    return cm_derivations["tp"] / (cm_derivations["tp"] + cm_derivations["fn"])


# Method to calculate the specificity
def specificity(cm_derivations):

    return cm_derivations["tn"] / (cm_derivations["fp"] + cm_derivations["tn"])
