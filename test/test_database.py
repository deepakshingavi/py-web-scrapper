import unittest

from module.database import Database


class TestDatabase(unittest.TestCase):

    def test_connect(self):
        db = Database()
        assert db.connect()

    def test_read(self):
        db = Database()
        assert db.read("image")

    def test_insert(self):
        db = Database()
        data = {'image_name': 'image-1', 'total_downloads': '10k', 'total_stars': '10',
                'total_pulls': '10k'}
        assert db.insert(data)

    def test_bulk_insert(self):
        db = Database()
        data_arr = [
            {'image_name': 'image-1', 'total_downloads': '10k', 'total_stars': '10', 'total_pulls': '10k'},
            {'image_name': 'image-2', 'total_downloads': '20k', 'total_stars': '30', 'total_pulls': '20k'}
        ]
        assert db.bulk_insert(data_arr)

    def test_delete(self):
        db = Database()
        assert db.delete('image-1')
