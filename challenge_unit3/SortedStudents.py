class Student:
    def __init__(self,name,roll_number,cgpa):
        self.name=name
        self.roll_number=roll_number
        self.cgpa=cgpa

def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda student: student.cgpa,reverse=True)
    return sorted_students
students=[
    Student("paramaguru","2k22431",7.1),
    Student("sarath","2k224448",8.9),
    Student("abhishek","2k22401",9.1),
    Student("vasanthM","2k22459",9.8)
    ]
sorted_students=sort_students(students)
for student in sorted_students:
    print("Name:{}. Roll Number:{}. CGPA:{}".format(student.name,student.roll_number,student.cgpa))
    

        
