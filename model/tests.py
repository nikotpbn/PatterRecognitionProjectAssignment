import numpy as np
from model.dataset import Dataset
from sklearn.model_selection import KFold
from model.rp_methods import kruskal_wallis, redundancy_measure
from model.rp_methods import cm_derivations_calculation, misclassification, sensitivity, specificity, performance_measurement
from model.rp_methods import bayes_classifier, support_vector_machines, \
    k_nearest_neighbors, minimum_distance_classifier, fisher_discriminant_analisys


def test_dataset(dataset=1, scenario=1, n_runs=3, n_subsets=3):
    # Load data object
    data = Dataset()

    # Choose dataset to be tested

    data.choose_data(dataset)
    print(data.database_selected_str, "data loaded.")

    # Pre-process data for scenario A
    data.scenario_pre_processing(scenario)
    print("Finished pre-processing data for", data.scenario_selected_str)

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
        performance = {
            'fp': 0,
            'fn': 0,
            'tp': 0,
            'tn': 0,
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
                    prediction = minimum_distance_classifier(x_train, y_train, x_test, y_test)
                # Fisher Discriminant Analisys (Fisher LDA)
                elif c == 2:
                    str = "Fisher LDA"
                    prediction = fisher_discriminant_analisys(x_train, y_train, x_test, y_test)
                # K-Nearest Neighbors (KNN)
                elif c == 3:
                    str = "K nearest neighbors with K=3"
                    constant_value = 3
                    prediction = k_nearest_neighbors(x_train, y_train, x_test, y_test, constant_value)
                # Bayes Classifier
                elif c == 4:
                    str = "Naive-Bayes"
                    prediction = bayes_classifier(x_train, y_train, x_test, y_test)
                # Support Vector Machines
                elif c == 5:
                    str = "Support Vector Machines with C=1"
                    constant_value = 1
                    prediction = support_vector_machines(x_train, y_train, x_test, y_test, constant_value)


                # Calculates TP, TN, FP, FN and update the dictionary
                performance = performance_measurement(y_test, prediction, data.scenario, performance)
                print("#####################################  RESULTS #####################################")
                print("True Positives: ", performance["tp"])
                print("True Negatives: ", performance["tn"])
                print("False Positives: ", performance["fp"])
                print("False Negatives: ", performance["fn"])
                print("Accuracy: ", performance['accuracy'])
                print("True Positive Rate (TPR | Sensitivity): ", performance['sensitivity'])
                print("True Negative Rate (TNR | Specificity): ", performance['specificity'])
                print("Misclassification per fold: ", performance['misclassification_per_run'])
                print("####################################################################################")

            # Save results per run
            misclassification_per_run /= n_subsets
            performance['misclassification_per_run'].append(misclassification_per_run)

        # Calculate average misclassification
        performance['avg_misclassification'] /= n_subsets

    performance['avg_misclassification'] /= n_runs

# Test dataset phone-accel, Scenario A, with 3 runs and 3 kfold subsets
print("Test dataset phone-accel, Scenario A, with 3 runs and 3 kfold subsets")
test_dataset(1, 1, 3, 3)
print("##############################################################################################################")


# print("Test dataset watch-accel, Scenario B, with 5 runs and 2 kfold subsets")
# Test dataset watch-accel, Scenario B, with 5 runs and 2 kfold subsets
# test_dataset(3, 2, 1, 3)
