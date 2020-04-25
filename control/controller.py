# Imports
# Own methods
from model.dataset import Dataset
from model.rp_methods import kbest, kruskal_wallis, feature_reduction, pca_analysis, run_pca, \
    minimum_distance_classifier, fisher_discriminant_analisys, bayes_classifier, k_nearest_neighbors, \
    support_vector_machines, cm_derivations_calculation, misclassification, sensitivity, specificity
# Views
from view.data_import import DataImport as ViewDataImport
from view.feature_selection_and_reduction import FeatureSelectionAndReduction as ViewFeatureSelectionAndReduction
from view.pca_utilization import PCAUtilization as ViewPCAUtilization
from view.pca_graphics import PCAGraphics as ViewPCAGraphics
from view.choose_classifier import ChooseClassifier as ViewChooseClassifier
from view.result import Result as ViewResult
# Third-party
from sklearn.model_selection import KFold
import numpy as np


# Class controller
class Controller:
    # Construct method
    def __init__(self):
        # Attributes
        # General
        self.data = Dataset()
        # Views
        self.data_import_view = None
        self.feature_selection_view = None
        self.feature_selection_view = None
        self.pca_utilization_view = None
        self.pca_graphics_view = None
        self.choose_classifier_view = None
        self.results_view = None

    # Create first screen: screen to select the database and the scenario to be used.
    def start(self):
        # Screens processing
        # Create the first screen
        self.data_import_view = ViewDataImport()
        self.data_import_view.show(self)

    # Pre-process the data in order of the chosen database and scenario. Create second screen: screen to choose the
    # feature selection method and the number of features to be select in this method.
    def data_import(self, database, scenario):
        # Data processing
        # Set the chosen database and scenario attribute, and select the right dataset to be used in the project.
        self.data.choose_data(database)
        # Data scenario pre-processing and controller variable assignment
        self.scenario = scenario
        self.data.scenario_pre_processing(scenario)

        # Screens processing
        # Destroy data_import_view
        self.data_import_view.dismiss()
        # Create the new screen: feature_selection_view
        self.feature_selection_view = ViewFeatureSelectionAndReduction()
        self.feature_selection_view.show(self)

    # Apply the chosen feature selection. Create the third screen: screen to decide to use or not use PCA
    def feature_selection_and_reduction(self, feature_selection_method, number_feature):
        # Data processing
        # Set the chosen feature selection method to be used.
        self.data.set_feature_selection_method(feature_selection_method)
        # feature selection
        # self.data.dataset = feature_selection(self.data.dataset, feature_selection_method, number_feature)
        # K-best method
        if feature_selection_method == 1:
            self.data.dataset = kbest(self.data.dataset, number_feature)
        # Kruskal_Wallis method
        if feature_selection_method == 2:
            self.data.dataset = kruskal_wallis(self.data.dataset, number_feature)
        # feature reduction method
        self.data.dataset, features_excluded = feature_reduction(self.data.dataset)
        self.data.set_features_excluded_by_feature_reduction(features_excluded)

        # Screens processing
        # Destroy feature_selection_view
        self.feature_selection_view.dismiss()
        # Create the new screen: pca_utilization_view
        self.pca_utilization_view = ViewPCAUtilization()
        self.pca_utilization_view.show(self, number_feature)

    # Method to Execute the PCA analisys in order to show the two PCA graphics in the screen
    def run_pca_analisys(self):
        # Data processing
        # Run the PCA analisys
        explained_variance_, x_values, singular_values_ = pca_analysis(self.data.dataset)

        # Screens processing
        # Destroy pca_utilization_view
        self.pca_utilization_view.dismiss()
        # Create the new screen: pca_graphics_view
        self.pca_graphics_view = ViewPCAGraphics()
        self.pca_graphics_view.show(self, explained_variance_, x_values, singular_values_)

    # Execute the PCA if the user chosen to use it and then prepare the screen that show the classifier options
    def choose_classifier(self, n_features):
        # Data processing
        # Apply PCA if the the function call came from run_pca_analisys
        if n_features != 0:
            self.data.dataset = run_pca(self.data.dataset, n_features)

        # Screens processing
        # Destroy pca_graphics_view
        if n_features != 0:
            self.pca_graphics_view.dismiss()
        else:
            self.pca_utilization_view.dismiss()
        # Create the new screen: choose_classifier_view
        self.choose_classifier_view = ViewChooseClassifier()
        self.choose_classifier_view.show(self)

    # Core method that run the chosen classifier and prepare the result the be show
    def apply_classifier(self, n_runs, n_subsets, classifier, constant_value):
        # Variables
        tests_results = {}
        results = {
            'Misclassification': 0,
            'Sensitivity': 0,
            'Specificity': 0
        }
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

        # Run the classification in order of the numbers of run chosen by the user
        for i in range(0, n_runs):
            # Variables
            misclassification_per_run = 0

            # Apply K-fold: splitting the dataset
            kf = KFold(n_splits=n_subsets)

            # K-fold Executions
            for idx_train, idx_test in kf.split(self.data.dataset["data"], self.data.dataset["target"]):
                # Train data
                x_train = [self.data.dataset["data"][idx] for idx in idx_train]
                x_train = np.asarray(x_train).astype(np.float64)
                y_train = [self.data.dataset["target"][idx] for idx in idx_train]

                # Test data
                x_test = [self.data.dataset["data"][idx] for idx in idx_test]
                x_test = np.asarray(x_test).astype(np.float64)
                y_test = [self.data.dataset["target"][idx] for idx in idx_test]

                # Check the classifier chosen to call the right method
                # Minimum distance classifier (MDC)
                if classifier == 1:
                    cm = minimum_distance_classifier(x_train, y_train, x_test, y_test)
                # Fisher Discriminant Analisys (Fisher LDA)
                elif classifier == 2:
                    cm = fisher_discriminant_analisys(x_train, y_train, x_test, y_test)
                # K-Nearest Neighbors (KNN)
                elif classifier == 3:
                    cm = k_nearest_neighbors(x_train, y_train, x_test, y_test, constant_value)
                # Bayes Classifier
                elif classifier == 4:
                    cm = bayes_classifier(x_train, y_train, x_test, y_test)
                # Support Vector Machines
                elif classifier == 5:
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

        # Just tests
        print(cm_derivations)

        # Screens processing
        # Destroy pca_utilization_view
        self.choose_classifier_view.dismiss()
        # Create the new screen: pca_graphics_view
        self.results_view = ViewResult()
        self.results_view.show(self, classifier, cm_derivations)

    # Method to run the C-value or K-value test and prepare the screen show the graphic of this test
    # TODO: Test run to discovery the best C-value or K-value
    def test_k_and_c_value(self, classifier):
        print("test_k_and_c_value: ", classifier)
        return 8


# Run Program
if __name__ == "__main__":
    data = Controller()
    data.start()
