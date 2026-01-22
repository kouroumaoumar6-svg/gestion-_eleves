class Student:
    def __init__(self, id=None, first_name="", last_name="", class_name="", phone=""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name
        self.phone = phone

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, {self.class_name})"
