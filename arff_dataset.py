import glob
import pathlib
import re
import numpy

# Dúvidas:
# 1) Qual dataset usar?
# 2) assignment da o exemplo de dividir os dataset em 4 partes (cell e smart: acel, giro), tem q ser assim? dado o
# objetivo o melhor n seria por atividades?
# 3) No final provavelmente vamos excluir as msms features do artigo que vem no datset so q temos q justificar com as
# tecnicas correto?
# 4) Optamos por fazer com o python e vamos utilizar a biblioteca indicada (scikit-learn), ela cobre todas as areas
# necessarias? Teremos que usar algumas outra para complementar?


class Dataset:
    # Attributes
    dataset = {
        "phone": {
            "accel": {
                "data": {},
                "target": {},
                "title": {}
            },
            "gyro": {
                "data": {},
                "target": {},
                "title": {}
            }
        },
        "watch": {
            "accel": {
                "data": {},
                "target": {},
                "title": {}
            },
            "gyro": {
                "data": {},
                "target": {},
                "title": {}
            }
        }
    }

    def add_data(self, data_files, device, sensor):
        # Variable
        file_number = 1
        data = []
        target = []
        title = []

        # Read each data in vector data_files
        for data_file in data_files:
            file = open(data_file)
            # Variable to control the lines in the file, to separate the sample to the titles
            line = 1
            # Read each line in each file
            for sample in file:
                if 4 <= line <= 94 and file_number == 1:
                    # Search for titles of each attribute
                    found = re.search('"(.+?)"', sample).group(1)
                    title.append(found)
                elif line > 97 and sample is not None:
                    # Work in each sample in the file
                    read = sample.split(",")
                    # Add the first value in the sample (activity) in the vector target
                    target.append(read[0])
                    # Eliminate the target (activity - first value) and the subject (individual - last value) from the
                    # sample
                    read.pop(0)
                    read.pop(-1)
                    # Add the vector read in the vector data
                    data.append(read)
                line += 1
            file_number += 1

        # Add the data read into the dataset attribute
        self.dataset[device][sensor]["data"] = numpy.asarray(data)
        self.dataset[device][sensor]["target"] = numpy.asarray(target)
        self.dataset[device][sensor]["title"] = numpy.asarray(title)

    def __init__(self):
        # Info
        print("Preparing paths...")

        # Path to the project file
        current_dir = pathlib.Path().absolute()

        # Paths to accelerometer and gyroscope dataset's
        phone_accel_paths = "%s/wisdm-dataset/arff_files/phone/accel/*.arff" % current_dir
        phone_gyro_paths = "%s/wisdm-dataset/arff_files/phone/gyro/*.arff" % current_dir
        watch_accel_paths = "%s/wisdm-dataset/arff_files/watch/accel/*.arff" % current_dir
        watch_gyro_paths = "%s/wisdm-dataset/arff_files/watch/gyro/*.arff" % current_dir

        # Load files
        phone_accel = glob.glob(phone_accel_paths)
        phone_gyro = glob.glob(phone_gyro_paths)
        watch_accel = glob.glob(watch_accel_paths)
        watch_gyro = glob.glob(watch_gyro_paths)

        # Read data
        # Phone-accelerometer data
        print("Reading phone-accelerometer...")
        self.add_data(phone_accel, "phone", "accel")

        # Phone-gyroscope data
        print("Reading phone-gyroscope...")
        self.add_data(phone_gyro, "phone", "gyro")

        # Watch-accelerometer data
        print("Reading watch-accelerometer...")
        self.add_data(watch_accel, "watch", "accel")

        # Watch-gyroscope data
        print("Reading watch-gyroscope...")
        self.add_data(watch_gyro, "watch", "gyro")
