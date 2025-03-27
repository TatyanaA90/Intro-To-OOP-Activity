# add your get_student_with_more_classes function here!
def get_student_with_more_classes(student1, student2):
    num1 = student1.get_num_classes()
    num2 = student2.get_num_classes()

    if num1 == num2:
        return "The students have the same number of classes."
    
    elif num1 > num2:
        return student1.name  
    
    else:
        return student2.name
