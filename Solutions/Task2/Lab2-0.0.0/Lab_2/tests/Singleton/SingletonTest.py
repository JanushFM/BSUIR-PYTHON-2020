import unittest
from Lab_2.code.Singleton.Singleton import MetaSingleton


class TestSingleton(unittest.TestCase):

    def test(self):
        class Database(metaclass=MetaSingleton):
            connection = None
            data_base = []

            def make_connection(self, url):
                if self.connection is None:
                    self.connection = url

            def add_object(self, obj):
                self.data_base.append(obj)

            def get_all_data(self):
                return self.data_base

        db1 = Database()
        db1.make_connection("https://JanushPC")
        db1.add_object({"Janush": 19})

        db2 = Database()  # db2 == db1
        db2.make_connection("https://NewUser")
        db2.add_object({"New User": 0})

        self.assertEqual(db1 == db1, True)
        self.assertEqual(db1.get_all_data() == db2.get_all_data(), True)

if __name__ == '__main__':
    unittest.main()
