# Imports
import numpy as np
import matplotlib.pyplot as plt
from arff_dataset import Dataset
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix
from scipy import stats
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
matplotlib.use("TkAgg")


def feature_selection_and_reduction(database, scenario, fr_method, n_features):
    # -------------------- Scenario Definition --------------------
    if scenario == "A":
        data = Dataset().get_database(database)

        # Set patterns for binary classification
        for i in range(0, len(data["target"])):
            if data["target"][i] != "B":
                data["target"][i] = "A"

    # -------------------- Feature selection (K bests) --------------------
    if fr_method == 1:
        # Choosing the K best features
        selector = SelectKBest(f_classif, k=n_features)
        new_data = selector.fit_transform(data["data"], data["target"])
        indexes = selector.get_support(indices=True)
        new_label = [data["label"][i] for i in indexes]

        # Update dataset replacing the old data and label to the bests
        data["data"] = new_data
        data["label"] = new_label

    # ----------------- Feature selection (Kruskal-Wallis) -----------------
    elif fr_method == 2:
        # Get information from the dataset
        t_data = np.transpose(data["data"])
        targets = data["target"]
        labels = data["label"]
        new_data = []
        new_labels = []

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
    
    # -------------------- Feature Reduction --------------------
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
    for i in redundant_features_idx:
        redundant_features_label.append(data["label"][i])
    # Exclude the features highly correlated from the matrix, fixes the label vector and prepare the redundant vector
    # with their respective labels
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
    return data


def pca_analisys(data):
    # -------------------- PCA (Kaiser or Scree) --------------------
    # PCA for reduction analysis
    pca = PCA()
    pca.fit(data["data"])
    # Plots
    # Preparations to plot
    x_values = np.arange(1, len(data["label"]) + 1)
    return pca.explained_variance_, x_values, pca.singular_values_


def pca_method(data, n_features):
    # PCA application
    pca = PCA(n_components=n_features)
    new_data = pca.fit_transform(data["data"])
    data["data"] = new_data
    return data


def classifier(data, classifier_opt, n_runs, n_subsets):
    tests_results = {}

    results = {
        'Misclassification': 0,
        'Sensitivity': 0,
        'Specificity': 0
    }
    for i in range(0, n_runs):
        # Apply K-fold
        kf = KFold(n_splits=n_subsets)
        misclassification_per_run = 0

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
            # -------------------- Classifier: Minimum distance classifier (MDC) --------------------
            if classifier_opt == 1:
                # Transpose x_train and y_train to feature x readings
                train_x = np.transpose(x_train)
                test_x = np.transpose(x_test)

                # Get indexes of the classes
                ix_w1 = np.nonzero(np.in1d(y_train, 'A'))
                ix_w2 = np.nonzero(np.in1d(y_train, 'B'))

                # Calculate the mean of features for each pattern
                mu1 = np.mean(train_x[:, ix_w1], 2)
                mu2 = np.mean(train_x[:, ix_w2], 2)

                # Array to hold prediction
                predict = []

                # Iterate through test data
                for k in range(0, len(test_x[1])):
                    # 1st part of euclidian general formula
                    test_sample = np.transpose(np.array([test_x[:, k]]))
                    g1 = mu1.transpose().dot(test_sample)
                    g2 = mu2.transpose().dot(test_sample)

                    # 2nd part of euclidian general formula
                    mu1sqr = np.dot(0.5, mu1.transpose().dot(mu1))
                    mu2sqr = np.dot(0.5, mu2.transpose().dot(mu2))

                    g1 -= mu1sqr
                    g2 -= mu2sqr

                    if g1 >= g2:
                        predict.append('A')
                        # print("For k=", k, ".Prediction was A")
                    else:
                        predict.append('B')
                        # print("For k=",  k, ".Prediction was B")

                cm = confusion_matrix(y_test, predict)
            # -------------------- Classifier: Fisher LDA --------------------
            if classifier_opt == 2:
                # Classifier training
                lda = LinearDiscriminantAnalysis().fit(x_train, y_train)
                # Classifier test
                predict = lda.predict(x_test)
                cm = confusion_matrix(y_test, predict)

            # Results
            fp = round(sum(cm.sum(axis=0) - np.diag(cm)) / len(cm.sum(axis=0) - np.diag(cm)))
            fn = round(sum(cm.sum(axis=1) - np.diag(cm)) / len(cm.sum(axis=1) - np.diag(cm)))
            tp = round(sum(np.diag(cm)) / len(np.diag(cm)))
            tn = cm.sum() - (fp + fn + tp)

            results['Misclassification'] += (fp + fn) / (tp + tn + fp + fn)
            misclassification_per_run += (fp + fn) / (tp + tn + fp + fn)
            results['Sensitivity'] += fp / (tp + fn)
            results['Specificity'] += fp / (fp + tn)

        # Save results per run
        misclassification_per_run /= n_subsets
        tests_results[i] = {
            'misclassification': misclassification_per_run
        }

    # End results calculations
    results['Misclassification'] = (results['Misclassification'] / (n_runs * n_subsets))
    results['Sensitivity'] = results['Sensitivity'] / (n_runs * n_subsets)
    results['Specificity'] = results['Specificity'] / (n_runs * n_subsets)

    print(tests_results)

    return results
