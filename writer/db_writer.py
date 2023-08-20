from module.database import Database
from writer.data_writer import BaseWriter


class DbWriter(BaseWriter):

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self,  data_arr):
        try:
            db = Database()
            db.bulk_insert(data_arr)
        except BaseException as e:
            raise e
