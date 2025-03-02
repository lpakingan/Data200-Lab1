# from Student
# old functionality for dictionary storage that were replaced w/ linked list functions
def get_students(self):
    student_data = {}
    with open('student.csv', newline = '') as csvfile:
        students = csv.reader(csvfile)
        next(students)
        for student in students:
            student_info = [student[1], student[2], student[3], student[4], student[5]]
            student_data[student[0]] = student_info
            return student_data
        
def display_records(self):
        '''displays student records'''
        students = self.get_students()
        for student in students:
            print(f'''
                    Name: {students[student][0]} {students[student][1]}
                    Email: {student}
                    Courses: {students[student][2]}
                    Grade: {students[student][3]}
                    Mark: {students[student][4]}
                    ''')
            
def add_new_student(self, student): # student from add_student()
        '''add a new student into the system'''
        students = self.get_students()
        if student.email_address not in students:
            students[student.email_address] = [student.first_name, student.last_name, None, None, None]
            print(f'Successfully added {student.first_name} {student.last_name} to the system!')
        else:
            print('Student is already in system!')