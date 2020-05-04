import numpy as np
import pathlib
from openpyxl import Workbook
from openpyxl import load_workbook
from model.dataset import Dataset
from sklearn.model_selection import KFold
from model.rp_methods import kruskal_wallis, redundancy_measure
from model.rp_methods import performance_measurement
from model.rp_methods import bayes_classifier, support_vector_machines, \
    k_nearest_neighbors, minimum_distance_classifier, fisher_discriminant_analisys


def test_dataset(path, dataset=1, scenario=1, n_runs=3, n_subsets=3):
    # Variables
    data = Dataset()
    runs_performance = {}

    # File Variables
    wb = load_workbook(path)
    ws = wb.active
    row = ws.max_row+1
    ws.title = 'Test Results'

    # Select test data
    data.choose_data(dataset)
    print(data.database_selected_str, "data loaded.")

    # Pre-process data
    data.scenario_pre_processing(scenario)
    print("Finished pre-processing data for", data.scenario_selected_str)

    # Apply Kruskal-Wallis
    data.set_feature_selection_method(2)
    data.dataset = kruskal_wallis(data.dataset, 91)
    print("Finished applying kruskal-wallis feature selection method.")

    # Apply Correlation redundancy measure
    data.dataset, unused_label = redundancy_measure(data.dataset)
    print("Correlation rendundancy measure applied.")
    print("Begining tests...this might take a while")

    # For all 5 classifiers
    for c in range(1, 3):
        # Variable to hold all runs for all classifiers
        runs_performance[c] = {}

        # Run "n_runs" tests
        for i in range(0, n_runs):
            # Structure to hold results of classification
            performance = {
                'fp': 0,
                'fn': 0,
                'tp': 0,
                'tn': 0,
                'accuracy': 0,
                'avg_misclassification': 0,
                'misclassification_per_fold': [],
                'sensitivity': 0,
                'specificity': 0
            }

            # Create dict to save run results
            runs_performance[c][i] = {}

            # Apply K-fold: splitting the dataset
            kf = KFold(n_splits=n_subsets, shuffle=True)

            # K-fold Executions
            for idx_train, idx_test in kf.split(data.dataset["data"], data.dataset["target"]):
                # Classification prediction
                prediction = []

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
                performance = performance_measurement(y_test, prediction, scenario, performance)
                # print_performance(performance)

            # Calculate averages
            performance['avg_misclassification'] /= n_subsets
            performance['sensitivity'] /= n_subsets
            performance['specificity'] /= n_subsets
            performance['accuracy'] /= n_subsets

            # Add values into the sheet
            ws.cell(column=1, row=row, value=dataset)
            ws.cell(column=2, row=row, value=i)
            ws.cell(column=3, row=row, value=np.array2string(performance['fp']))
            ws.cell(column=4, row=row, value=np.array2string(performance['fn']))
            ws.cell(column=5, row=row, value=np.array2string(performance['tp']))
            ws.cell(column=6, row=row, value=np.array2string(performance['tn']))
            ws.cell(column=7, row=row, value=np.array2string(performance['accuracy']))
            ws.cell(column=8, row=row, value=np.array2string(performance['avg_misclassification']))
            ws.cell(column=9, row=row, value=np.array2string(performance['sensitivity']))
            ws.cell(column=10, row=row, value=np.array2string(performance['specificity']))
            ws.cell(column=11, row=row, value=c)
            row += 1

            # Save performance measurement per run
            runs_performance[c][i]["performance"] = performance
            runs_performance[c][i]["scenario"] = scenario

    print("Finished")

    # For debug
    # for classifier in runs_performance:
    #     for run in runs_performance[classifier]:
    #         print("Classifier ", classifier, " run", run)
    #         print(runs_performance[classifier][run])

    return wb


def new_sheet(scenario):
    wb = Workbook()
    ws = wb.active
    ws.title = 'Tests results'

    filename = "tests_results_scenario_%s.xlsx" % scenario
    current_dir = pathlib.Path().absolute().parent
    path = "%s/temp/%s" % (current_dir, filename)

    # Sheet Layout
    ws.column_dimensions['A'].width = 10
    ws.column_dimensions['B'].width = 7
    ws.column_dimensions['C'].width = 7
    ws.column_dimensions['D'].width = 7
    ws.column_dimensions['E'].width = 7
    ws.column_dimensions['F'].width = 7
    ws.column_dimensions['G'].width = 21
    ws.column_dimensions['H'].width = 21
    ws.column_dimensions['I'].width = 21
    ws.column_dimensions['J'].width = 21
    ws.column_dimensions['K'].width = 7

    # Column headers
    ws['A1'] = 'dataset'
    ws['B1'] = 'run_id'
    ws['C1'] = 'fp'
    ws['D1'] = 'fn'
    ws['E1'] = 'tp'
    ws['F1'] = 'tn'
    ws['G1'] = 'accuracy'
    ws['H1'] = 'avg_misclassification'
    ws['I1'] = 'sensitivity'
    ws['J1'] = 'specificity'
    ws['K1'] = 'classifier'
    wb.save(path)

    return path, wb

