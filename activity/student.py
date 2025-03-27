# add your Student class here!
class Student:
  def __init__(self, name, grade, courses):
    self.name = name
    self.grade = grade
    self.courses = courses
  
  def add_class(self, class_name):
    self.courses.append(class_name)
    return self.courses
  
  def get_num_classes(self):
    return len(self.courses)

  def summary(self):
    num_courses = self.get_num_classes()
    print(f"{self.name} is a {self.grade} enrolled in {num_courses} classes")


