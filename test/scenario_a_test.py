from model.tests import test_dataset, new_sheet

# Create a new file
path, worksheet = new_sheet(1)

# write and save resuts
worksheet = test_dataset(path, 1, 1, 2, 3)
worksheet.save(path)

worksheet = test_dataset(path, 2, 1, 2, 3)
worksheet.save(path)

worksheet = test_dataset(path, 3, 1, 2, 3)
worksheet.save(path)

worksheet = test_dataset(path, 4, 1, 2, 3)
worksheet.save(path)

