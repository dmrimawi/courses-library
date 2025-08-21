class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_info(self):
        return f"Student name is {self.name}, and the id is {self.id}"
