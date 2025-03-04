# from LoginUser
# old functionality for array storage
def login(self):
        '''checks the login details of the current user and logs them in if correct'''
        with open('login.csv', newline = '') as csvfile:
            logins = csv.reader(csvfile)
            next(logins)
            login_data = [login for login in logins]
        
        for login in login_data:
            if self.email_address == login[0]:
                print("You are now logged in!") if self.password == login[1] else print("Wrong password!")
            else:
                print("Email does not exist!")
                
        # insert code for encrypting/decrypting password


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

def delete_student(self, email_address): # consolidated into delete_node()
    '''delete a student in the system using their email address'''
    # linked list method
    students_ll, student_list, header = self.get_students()
    student_exists = False
    prev_student = None
    if students_ll.check_head():
        c1 = students_ll.head
        while c1 is not None:
            if c1.data[0] == email_address:
                print(f'Deleting {c1.data[1]} {c1.data[2]} from the system...')
                if prev_student is None: # checking if first node; if so, move head to the next node
                    student_exists = True
                    students_ll.head = c1.next
                    write_to_file_ll('student.csv', header, students_ll)
                    break
                else: # if not first node, point previous node to the node after this one
                    student_exists = True
                    prev_student.next = c1.next
                    write_to_file_ll('student.csv', header, students_ll)
                    break
            prev_student = c1
            c1 = c1.next

    else:
        print('No students in system!')

    if not student_exists:
        print('No student found with the entered email address!')
    else:
        students_ll.print()

# from Course
def delete_course(self, id): # consolidated into delete_node()
    '''delete a course using its id'''
    courses_ll, course_list, header = self.get_courses()
    course_exists = False
    prev_course = None
    if courses_ll.check_head():
        c1 = courses_ll.head
        while c1 is not None:
            if c1.data[0] == id:
                print(f'Deleting {c1.data[0]} from the system...')
                if prev_course is None: 
                    course_exists = True
                    courses_ll.head = c1.next
                    write_to_file_ll('course.csv', header, courses_ll)
                    break
                else: 
                    course_exists = True
                    prev_course.next = c1.next
                    write_to_file_ll('course.csv', header, courses_ll)
                    break
            prev_course = c1
            c1 = c1.next

    else:
        print('No courses in system!')

    if not course_exists:
        print('No course found with the entered course id')
    else:
        courses_ll.print()