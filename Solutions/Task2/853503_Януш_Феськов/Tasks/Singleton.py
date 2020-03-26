class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


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

print("Data from db1:", db1.get_all_data())
print("Data from db2:", db2.get_all_data())
