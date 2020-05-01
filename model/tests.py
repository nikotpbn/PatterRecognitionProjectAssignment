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

        performance_test = {
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
            misclassification_per_run2 = 0

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
                print(cm)

                # Calculates TP, TN, FP, FN and update the dictionary
                performance = cm_derivations_calculation(cm, performance)
                performance_test = performance_measurement(cm, scenario, performance_test)

                # Calculates general misclassification
                performance['misclassification'] += misclassification(performance)
                performance_test["misclassification"] += misclassification(performance_test)

                # Calculates misclassification for each run
                misclassification_per_run += misclassification(performance)
                misclassification_per_run2 += misclassification(performance_test)

                # Calculates sensitivity
                performance['sensitivity'] += sensitivity(performance)
                performance_test["sensitivity"] += sensitivity(performance_test)

                # Calculates specificity
                performance['specificity'] += specificity(performance)
                performance_test["specificity"] += specificity(performance_test)

            # Save results per run
            misclassification_per_run /= n_subsets
            misclassification_per_run2 /= n_subsets
            performance['misclassification_per_run'].append(misclassification_per_run)
            performance_test["misclassification_per_run"].append(misclassification_per_run2)

        # End results calculations
        performance['misclassification'] = (performance['misclassification'] / (n_runs * n_subsets))
        performance['sensitivity'] = performance['sensitivity'] / (n_runs * n_subsets)
        performance['specificity'] = performance['specificity'] / (n_runs * n_subsets)

        performance_test["misclassification"] = (performance_test["misclassification"] / (n_runs * n_subsets))
        performance_test["sensitivity"] = performance_test["sensitivity"] / (n_runs * n_subsets)
        performance_test["specificity"] = performance_test["specificity"] / (n_runs * n_subsets)

        print("ACTUAL RESULTS FOR : ", str)
        print("Average misclassification: ", performance["misclassification"])
        print("Sensitivity: ", performance["sensitivity"])
        print("Specificity: ", performance["specificity"])
        print("Misclassification per run: ", performance["misclassification_per_run"])
        print("------------------------------------------------------------------------------------------------------")
        print("NEW RESULTS FOR: ", str)
        print("Average misclassification: ", performance_test["misclassification"])
        print("Sensitivity: ", performance_test["sensitivity"])
        print("Specificity: ", performance_test["specificity"])
        print("Misclassification per run: ", performance_test["misclassification_per_run"])

# Test dataset phone-accel, Scenario A, with 3 runs and 3 kfold subsets
# print("Test dataset phone-accel, Scenario A, with 3 runs and 3 kfold subsets")
# test_dataset(1, 1, 3, 3)
#
# print("##############################################################################################################")

print("Test dataset watch-accel, Scenario B, with 5 runs and 2 kfold subsets")
# Test dataset watch-accel, Scenario B, with 5 runs and 2 kfold subsets
test_dataset(3, 2, 1, 3)
