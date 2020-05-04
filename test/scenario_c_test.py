from model.tests import test_dataset, new_sheet

# Create a new file
path, worksheet = new_sheet(3)

# write and save resuts
worksheet = test_dataset(path, 1, 3, 50, 10)
worksheet.save(path)

worksheet = test_dataset(path, 2, 3, 50, 10)
worksheet.save(path)

worksheet = test_dataset(path, 3, 3, 50, 10)
worksheet.save(path)

worksheet = test_dataset(path, 4, 3, 50, 10)
worksheet.save(path)
