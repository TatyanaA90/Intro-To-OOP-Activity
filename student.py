# add your Student class here!
class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes
    
    def add_class(self, class_to_add):
        self.classes.append(class_to_add)

        return self.classes

    def get_num_classes(self):
        num_classes = 0

        for student_class in self.classes:
            num_classes += 1
        
        return num_classes
    
    def summary(self):
        return f"{self.name.capitalize()} is a {self.grade} in {self.get_num_classes()} classes"
    
