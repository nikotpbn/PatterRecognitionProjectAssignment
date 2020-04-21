# Imports
# General
from model.dataset import Dataset
from model.rp_methods import kbest, kruskal_wallis, feature_reduction
# Views
from view.data_import import DataImport as ViewDataImport
from view.feature_selection_and_reduction import FeatureSelectionAndReduction as ViewFeatureSelectionAndReduction
from view.pca_utilization import PCAUtilization as ViewPCAUtilization


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
        # ----

        # Screens processing
        # Destroy pca_utilization_view
        self.feature_selection_view.dismiss()
        # Create the new screen: ????

    def run_pca(self):
        pass

    def classifiers(self):
        pass


# Run Program
if __name__ == "__main__":
    data = Controller()
    data.start()
