# add your get_student_with_more_classes function here!

def get_student_with_more_classes(student_1, student_2):
    return student_1.name if len(student_1.classes) > len(student_2.classes) else student_2.name
    