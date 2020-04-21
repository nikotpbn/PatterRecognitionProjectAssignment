# Imports
# General
from model.dataset import Dataset
from model.rp_methods import kbest, kruskal_wallis, feature_reduction, pca_analisys, run_pca
# Views
from view.data_import import DataImport as ViewDataImport
from view.feature_selection_and_reduction import FeatureSelectionAndReduction as ViewFeatureSelectionAndReduction
from view.pca_utilization import PCAUtilization as ViewPCAUtilization
from view.pca_graphics import PCAGraphics as ViewPCAGraphics
from view.choose_classifier import ChooseClassifier as ViewChooseClassifier


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

    # Create first screen: screen to select the database and the scenario to be used.
    def start(self):
        # Create the first screen
        self.data_import_view = ViewDataImport()
        self.data_import_view.show(self)

    # Pre-process the data in order of the chosen database and scenario. Create second screen: screen to choose the
    # feature selection method and the number of features to be select in this method.
    def data_import(self, database, scenario):
        # Data processing
        # Set the chosen database and scenario attribute, and select the right dataset to be used in the project.
        self.data.choose_data(database)
        # Data scenario pre-processing
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

    def run_pca_analisys(self):
        # Data processing
        # Run the PCA analisys
        explained_variance_, x_values, singular_values_ = pca_analisys(self.data.dataset)

        # Screens processing
        # Destroy pca_utilization_view
        self.pca_utilization_view.dismiss()
        # Create the new screen: pca_graphics_view
        self.pca_graphics_view = ViewPCAGraphics()
        self.pca_graphics_view.show(self, explained_variance_, x_values, singular_values_)

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

    def apply_classifier(self, n_run, n_subsets, classifier, constant_value):
        print(n_run)
        print(n_subsets)
        print(classifier)
        print(constant_value)


# Run Program
if __name__ == "__main__":
    data = Controller()
    data.start()
