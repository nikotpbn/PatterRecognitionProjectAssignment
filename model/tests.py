import numpy as np
from model.dataset import Dataset
from sklearn.model_selection import KFold
from model.rp_methods import kruskal_wallis, redundancy_measure
from model.rp_methods import cm_derivations_calculation, misclassification, sensitivity, specificity
from model.rp_methods import bayes_classifier, support_vector_machines, \
    k_nearest_neighbors, minimum_distance_classifier, fisher_discriminant_analisys

# Test variables
n_runs = 3
n_subsets = 3

# Load data object
data = Dataset()

# Choose dataset to be tested

data.choose_data(1)
print("phone-accel data loaded.")

# Pre-process data for scenario A
data.scenario_pre_processing(1)
print("Finished pre-processing data for Scenario A.")

# Apply Kruskal-Wallis + Correlation redundancy measure
data.set_feature_selection_method(2)
data.dataset = kruskal_wallis(data.dataset, 91)
print("Finished applying kruskal-wallis feature selection method.")

# Apply Correlation redundancy measure
data.dataset, unused_label = redundancy_measure(data.dataset)
print("Correlation rendundancy measure applied.")

# For all 5 classifiers
for c in range(1, 6):
    # Structure to hold results of classification
    cm_derivations = {
        'FP': 0,
        'FN': 0,
        'TP': 0,
        'TN': 0,
        'misclassification': 0,
        'misclassification_per_run': [],
        'sensitivity': 0,
        'specificity': 0
    }

    # Run "n_runs" tests
    for i in range(0, n_runs):
        # Variables
        misclassification_per_run = 0

        # Apply K-fold: splitting the dataset
        kf = KFold(n_splits=n_subsets, shuffle=True)

        # TODO: REMEMBER TO SHUFFLE TESTS
        # K-fold Executions
        for idx_train, idx_test in kf.split(data.dataset["data"], data.dataset["target"]):
            # Train data
            x_train = [data.dataset["data"][idx] for idx in idx_train]
            x_train = np.asarray(x_train).astype(np.float64)
            y_train = [data.dataset["target"][idx] for idx in idx_train]

            # Test data
            x_test = [data.dataset["data"][idx] for idx in idx_test]
            x_test = np.asarray(x_test).astype(np.float64)
            y_test = [data.dataset["target"][idx] for idx in idx_test]

            # Check the classifier chosen to call the right method
            # Minimum distance classifier (MDC)
            if c == 1:
                str = "Minimun distance classifier"
                cm = minimum_distance_classifier(x_train, y_train, x_test, y_test)
            # Fisher Discriminant Analisys (Fisher LDA)
            elif c == 2:
                str = "Fisher LDA"
                cm = fisher_discriminant_analisys(x_train, y_train, x_test, y_test)
            # K-Nearest Neighbors (KNN)
            elif c == 3:
                str = "K nearest neighbors with K=3"
                constant_value = 3
                cm = k_nearest_neighbors(x_train, y_train, x_test, y_test, constant_value)
            # Bayes Classifier
            elif c == 4:
                str = "Naive-Bayes"
                cm = bayes_classifier(x_train, y_train, x_test, y_test)
            # Support Vector Machines
            elif c == 5:
                str = "Support Vector Machines with C=1"
                constant_value = 1
                cm = support_vector_machines(x_train, y_train, x_test, y_test, constant_value)

            # Results
            # Calculates TP, TN, FP, FN and update the dictionary
            cm_derivations = cm_derivations_calculation(cm, cm_derivations)

            # Calculates general misclassification
            cm_derivations['misclassification'] += misclassification(cm_derivations)

            # Calculates misclassification for each run
            misclassification_per_run += misclassification(cm_derivations)

            # Calculates sensitivity
            cm_derivations['sensitivity'] += sensitivity(cm_derivations)

            # Calculates specificity
            cm_derivations['specificity'] += specificity(cm_derivations)

        # Save results per run
        misclassification_per_run /= n_subsets
        cm_derivations['misclassification_per_run'].append(misclassification_per_run)

    # End results calculations
    cm_derivations['misclassification'] = (cm_derivations['misclassification'] / (n_runs * n_subsets))
    cm_derivations['sensitivity'] = cm_derivations['sensitivity'] / (n_runs * n_subsets)
    cm_derivations['specificity'] = cm_derivations['specificity'] / (n_runs * n_subsets)

    print("RESULTS FOR: ", str)
    print("False Positives: ", cm_derivations["FP"])
    print("False Negatives: ", cm_derivations["FN"])
    print("True Positives: ", cm_derivations["TP"])
    print("True Positives: ", cm_derivations["TN"])
    print("Average misclassification: ", cm_derivations["misclassification"])
    print("Sensitivity: ", cm_derivations["sensitivity"])
    print("Specificity: ", cm_derivations["specificity"])
    print("Misclassification per run: ", cm_derivations["misclassification_per_run"])
    print("----------------------------------------------------------------------------------------------------------")
