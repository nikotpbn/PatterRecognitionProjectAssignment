from model.tests import test_dataset, new_sheet

# Variables
scenario = 1
n_runs = 50
n_subsets = 10
pca = 0

# Create a new file
path, worksheet = new_sheet(scenario)

# write data for "Accelerometer from phone" dataset
print("Starting test for dataset 1: phone-accel...")
worksheet = test_dataset(path=path,
                         dataset=1,
                         scenario=scenario,
                         n_runs=n_runs,
                         n_subsets=n_subsets,
                         k=3,
                         c=13,
                         pca=pca)
worksheet.save(path)
print("finished.")

# write data for "Gyroscope from phone" dataset
print("Starting test for dataset 2: phone-gyro...")
worksheet = test_dataset(path=path,
                         dataset=2,
                         scenario=scenario,
                         n_runs=n_runs,
                         n_subsets=n_subsets,
                         k=3,
                         c=3,
                         pca=pca)
worksheet.save(path)
print("finished.")

# write data for "Accelerometer from watch" dataset
print("Starting test for dataset 3: watch-accel...")
worksheet = test_dataset(path=path,
                         dataset=3,
                         scenario=scenario,
                         n_runs=n_runs,
                         n_subsets=n_subsets,
                         k=9,
                         c=19,
                         pca=pca)
worksheet.save(path)
print("finished.")

# write data for "Gyroscope from watch" dataset
print("Starting test for dataset 4: watch gyro...")
worksheet = test_dataset(path=path,
                         dataset=4,
                         scenario=scenario,
                         n_runs=n_runs,
                         n_subsets=n_subsets,
                         k=7,
                         c=11,
                         pca=pca)
worksheet.save(path)
print("finished.")

