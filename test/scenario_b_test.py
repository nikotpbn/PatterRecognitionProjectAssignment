from model.tests import test_dataset, new_sheet

# Create a new file
path, worksheet = new_sheet(2)

# write and save resuts
worksheet = test_dataset(path, 1, 2, 2, 3)
worksheet.save(path)

worksheet = test_dataset(path, 2, 2, 2, 3)
worksheet.save(path)

worksheet = test_dataset(path, 3, 2, 2, 3)
worksheet.save(path)

worksheet = test_dataset(path, 4, 2, 2, 3)
worksheet.save(path)
