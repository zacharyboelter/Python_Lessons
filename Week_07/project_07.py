# Project 7
#Zachary Boelter

# 1
def GetStudentData(StudentID):

    StudentName = input("Enter student name: ")
    GPA = input("Enter GPA: ")
    Major = input("Enter major: ")

    return StudentName, GPA, Major

# 2
def DisplayStudentData():

    print("\nStudent Data:")
    for student in main_student_list:
        print(student)

# 3
main_student_list = []

# 4
while True:
    id_input = input("Enter student ID (or type 'quit' to finish): ")
    
    if id_input.lower() == 'quit':
        break

    # 5
    name, gpa, major = GetStudentData(id_input)

    # 6
    student_record = [id_input, name, gpa, major]
    main_student_list.append(student_record)

# 7
DisplayStudentData()