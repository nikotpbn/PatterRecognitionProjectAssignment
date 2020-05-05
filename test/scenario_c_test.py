from model.tests import test_dataset, new_sheet

# Variables
scenario = 3
n_runs = 2
n_subsets = 3
pca = 0

# Create a new file
path, worksheet = new_sheet(scenario)

# write and save results
print("Starting test for dataset 1...")
worksheet = test_dataset(path=path,
                         dataset=1,
                         scenario=scenario,
                         n_runs=n_runs,
                         n_subsets=n_subsets,
                         k=3,
                         c=1,
                         pca=pca)
worksheet.save(path)
print("finished.")

print("Starting test for dataset 2...")
worksheet = test_dataset(path=path,
                         dataset=2,
                         scenario=scenario,
                         n_runs=n_runs,
                         n_subsets=n_subsets,
                         k=3,
                         c=1,
                         pca=pca)
worksheet.save(path)
print("finished.")

print("Starting test for dataset 3...")
worksheet = test_dataset(path=path,
                         dataset=3,
                         scenario=scenario,
                         n_runs=n_runs,
                         n_subsets=n_subsets,
                         k=3,
                         c=1,
                         pca=pca)
worksheet.save(path)
print("finished.")

print("Starting test for dataset 4...")
worksheet = test_dataset(path=path,
                         dataset=4,
                         scenario=scenario,
                         n_runs=n_runs,
                         n_subsets=n_subsets,
                         k=3,
                         c=1,
                         pca=pca)
worksheet.save(path)
print("finished.")

