from writer.data_writer import BaseWriter
import csv


class CsvWriter(BaseWriter):

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self,  data_arr):
        csv_file = None
        try:
            csv_file = open(self.file_name, 'w')
            writer = csv.writer(csv_file)

            # Writing the Headers for the CSV File
            writer.writerow(['Image Name', 'Downloads', 'Stars', 'Pulls'])

            for image_info in data_arr:
                writer.writerow(image_info)
        except BaseException as e:
            raise e
        finally:
            if csv_file:
                csv_file.close()
