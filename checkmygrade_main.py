import csv
import getpass
import shutil
import time
import statistics
from encdyc import PasswordEncryptDecrypt

class LoginUser:
    '''user class that includes a user's login information for the application'''
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def get_logins(self):
        login_data = LinkedList()
        with open('login.csv', newline = '') as csvfile:
            logins = csv.reader(csvfile)
            next(logins)
            for login in logins:
                login_data.add_new(login)
            return login_data

    def login(self):
        '''checks the login details of the current user and logs them in if correct'''
        # linked list method
        logins = self.get_logins()
        login_exists = False
        if logins.check_head():
            c1 = logins.head
            while c1 is not None:
                if c1.data[0] == self.email_address:
                    encrypted_password = self.encrypt_password(self.password)
                    if encrypted_password == c1.data[1]:
                        print('You are now logged in!')
                        login_exists = True
                        return True, c1.data[0], c1.data[2]
                    else:
                        print("Unable to login! Returning to login screen...")
                        login_exists = True
                        return False, None, None
                else: 
                    c1 = c1.next

        if not login_exists:
            print('The email address is not associated with an account!')
            return False, None, None

    def logout(self):
        '''logs the current user out of the system'''
        return False

    def change_password(self):
        '''changes a user's password'''
        logins_ll, login_list, header = get_data('login.csv')
        for login in login_list:
            if login[0] == self.email_address:
                new_password = getpass.getpass("Enter your new password: ")
                encrypted_new_password = self.encrypt_password(new_password)
                login[1] = self.password = encrypted_new_password
        write_to_file_array('login.csv', header, login_list)
        print(f'Your password has been updated! Please try logging in with your new password...')
        return False

    def encrypt_password(self, password):
        '''encrypts a user's password'''
        preencrypted_password = PasswordEncryptDecrypt(4)
        encrypted_password = preencrypted_password.encrypt(password)
        return encrypted_password

    def decrypt_password(self, password):
        '''decrypts a user's password'''
        predecrypted_password = PasswordEncryptDecrypt(4)
        decrypted_password = predecrypted_password.decrypt(password)
        return decrypted_password

class Student:
    '''student class that includes information regarding a student's name, email, grades/marks'''
    def __init__(self, first_name, last_name, email_address, course_ids, grades, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.course_ids = course_ids
        self.grades = grades
        self.marks = marks

    @staticmethod
    def display_records():
        '''displays student records'''
        # array method
        print('Displaying students...')
        students_list = get_data('student.csv')[1]
        for student in students_list:
            course_list = student[3].split('|')
            grades_list = student[4].split('|')
            marks_list = student[5].split('|')
            print(f'''
                  {student[0]}
                  {student[1]} {student[2]}
                  Course(s): {course_list}
                  Grade(s): {grades_list}
                  Mark(s): {marks_list}
                  ''')
    
    def add_new_student(self, student): # student from add_student()
        '''add a new student into the system'''
        # linked list method
        print(f'Checking system to add {student.first_name} {student.last_name}...')
        students_ll = get_data('student.csv')[0]
        student_info = [student.email_address, student.first_name, student.last_name, student.course_ids, student.grades, student.marks]
        exists = students_ll.check_for_data_in_ll(self.email_address)

        if students_ll.size() == 0:
            students_ll.add_first(student_info)
            add_to_file('student.csv', student_info)
            print(f'{student.first_name} {student.last_name} successfully added! (First student added)')

        if not exists:
            students_ll.add_new(student_info)
            add_to_file('student.csv', student_info)
            print(f'{student.first_name} {student.last_name} successfully added! (Another student added)')

    def delete_student(self, email_address):
        '''delete a student in the system using their email address'''
        # linked list method
        students_ll, student_list, header = get_data('student.csv')
        try:
            print(f'Checking system to delete student associated with email {email_address}...')
            students_ll.delete_node(email_address)
            write_to_file_ll('student.csv', header, students_ll)
        except Exception as e:
            print(f'Error deleting student: {e}!')

    def check_my_grades(self):
        '''lets student check their own grades'''
        # array method
        student_list = get_data('student.csv')[1]
        for student in student_list:
            if student[0] == self.email_address:
                course_list = self.course_ids.split('|')
                print(f'{self.email_address} is currently taking {len(course_list)} courses.')
                print('Showing grades...')
                grades_list = self.grades.split('|')
                for idx, course in enumerate(course_list):
                    print(f"{course}: {grades_list[idx]}")

    def update_student_record(self, new_grade, new_mark):
        '''updates a student's record by using their email address'''
        # array method
        students_ll, student_list, header = get_data('student.csv')
        for student in student_list:
            if student[0] == self.email_address:
                student[4] = self.grades = new_grade 
                student[5] = self.marks = new_mark 
        write_to_file_array('student.csv', header, student_list)
        print(f'The grade and mark for {self.first_name} {self.last_name} has been updated to {new_grade} ({new_mark}%)')

    def check_my_marks(self):
        '''lets student check their own marks'''
        # array method
        student_list = get_data('student.csv')[1]
        for student in student_list:
            if student[0] == self.email_address:
                course_list = self.course_ids.split('|')
                print(f'{self.email_address} is currently taking {len(course_list)} courses.')
                print('Showing marks...')
                marks_list = self.marks.split('|')
                for idx, course in enumerate(course_list):
                    print(f"{course}: {marks_list[idx]}%")

    @staticmethod
    def sort_students(by, order):
        '''sorts students either by email or grade'''
        start_time = time.time()
        student_list = get_data('student.csv')[1]
        grades_list = Grades.get_grades()
        sorted_list = sorted(student_list, key = lambda x: x[0]) if by == 'email' else sorted(grades_list, key = lambda x: x[2])
        if order == 'reverse':
            sorted_list = sorted_list[::-1]
        for data in sorted_list:
            print(f'''
                  {data}
                  ''')
        print(f'Sorting time: {time.time() - start_time} seconds')
        
class Course:
    '''course class that includes information regarding a course's id, credits, name'''
    def __init__(self, course_id, credits, course_name, course_description):
        self.course_id = course_id
        self.credits = credits
        self.course_name = course_name
        self.course_description = course_description

    @staticmethod # static to call out of course object
    def display_courses():
        '''displays all courses'''
        print('Displaying courses...')
        courses_list = get_data('course.csv')[1]
        for course in courses_list:
            print(f'''
                  {course[0]}
                  Name: {course[1]}
                  Credits: {course[2]}
                  Description: {course[3]}
                  ''')

    def add_new_course(self, course): # course from add_course()
        '''add a new course'''
        print(f'Checking system to add {course.course_id}...')
        courses_ll = get_data('course.csv')[0]
        course_info = [course.course_id, course.credits, course.course_name, course.course_description]
        exists = courses_ll.check_for_data_in_ll(self.course_id)

        if courses_ll.size() == 0:
            courses_ll.add_first(course_info)
            add_to_file('course.csv', course_info)
            print(f'{course.course_id} successfully added! (First course added)')

        if not exists:
            courses_ll.add_new(course_info)
            add_to_file('course.csv', course_info)
            print(f'{course.course_id} successfully added! (Another course added)')

    def delete_course(self, id):
        '''delete a course using its id'''
        courses_ll, course_list, header = get_data('course.csv')
        try:
            print(f'Checking system to delete course associated with the course id {id}...')
            courses_ll.delete_node(id)
            write_to_file_ll('course.csv', header, courses_ll)
        except Exception as e:
            print(f'Error deleting course: {e}!')
    
class Professor:
    '''professor class that includes information regarding a professor's name, email, rank'''
    def __init__(self, email_address, name, rank, course_id):
        self.name = name
        self.email_address = email_address
        self.rank = rank
        self.course_id = course_id

    @staticmethod
    def professors_details():
        '''displays all professors'''
        print('Displaying professor details...')
        professors_list = get_data('professor.csv')[1]
        for professor in professors_list:
            print(f'''
                  {professor[0]}
                  {professor[1]}
                  Rank: {professor[2]}
                  Currently Teaching: {professor[3]}
                  ''')

    def add_new_professor(self, professor): # professor from add_professor()
        '''add a new professor into the system'''
        print(f'Checking system to add {professor.name}...')
        professors_ll = get_data('professor.csv')[0]
        professor_info = [professor.email_address, professor.name, professor.rank, professor.course_id]
        exists = professors_ll.check_for_data_in_ll(self.email_address)

        if professors_ll.size() == 0:
            professors_ll.add_first(professor_info)
            add_to_file('professor.csv', professor_info)
            print(f'{professor.name} successfully added! (First professor added)')

        if not exists:
            professors_ll.add_new(professor_info)
            add_to_file('professor.csv', professor_info)
            print(f'{professor.name} successfully added! (Another professor added)')
    
    def delete_professor(self, email_address):
        '''delete a professor using their email address'''
        professors_ll, professor_list, header = get_data('professor.csv')
        try:
            print(f'Checking system to delete professor associated with the email {email_address}...')
            professors_ll.delete_node(email_address)
            write_to_file_ll('professor.csv', header, professors_ll)
        except Exception as e:
            print(f'Error deleting professor: {e}!')

    def modify_professor_details(self, new_rank):
        '''modify a professor in the system using their email address'''
        professors_ll, professor_list, header = get_data('professor.csv')
        for professor in professor_list:
            if professor[0] == self.email_address:
                professor[2] = self.rank = new_rank
        write_to_file_array('professor.csv', header, professor_list)
        print(f'The rank for {self.name} has been updated to {self.rank}')

    def show_course_details_by_professor(self):
        '''show a professor's course using their email address'''
        start_time = time.time()
        professor_list = get_data('professor.csv')[1]
        course_list = get_data('course.csv')[1]
        if self.email_address:
            for professor in professor_list:
                if professor[0] == self.email_address:
                    for course in course_list:
                        if professor[3] == course[0]:
                            print(f'''
                                Showing course details for {professor[1]}:
                                ID: {course[0]}
                                Name: {course[1]}
                                Credits: {course[2]}
                                Description: {course[3]}
                                '''
                            )
        print(f'Search time: {time.time() - start_time} seconds')

class Grades:
    '''grades class that includes information regarding a specific grade for a student'''
    def __init__(self, grade_id, grade, mark, course_id = None):
        self.grade_id = grade_id # email address to match with the student it is assigned to
        self.grade = grade
        self.mark = mark

    @staticmethod
    def get_grades():
        students = get_data('student.csv')[1]
        grade_data = []
        for student in students:
            student_courses = student[3].split('|')
            student_grades = student[4].split('|')
            student_marks = student[5].split('|')
            for idx, course in enumerate(student_courses):
                grade_data.append([student[0], student_grades[idx], student_marks[idx], course])
        return grade_data
    
    @staticmethod
    def display_grade_report():
        '''displays a report of all the grades for students'''
        grades = Grades.get_grades()
        for grade in grades:
            grade_id = grade[0]
            grade_id = Grades(grade[0], grade[1], grade[2], grade[3])
            print(f'{grade_id.grade_id}: {grade_id.grade} / {grade_id.mark}% / {grade[3]}')

    @staticmethod
    def display_grades_by_course(course):
        start_time = time.time()
        grades = Grades.get_grades()
        course_grades = []
        for grade in grades:
            if grade[3] == course:
                course_grades.append(grade[2])
                print(f'{grade[0]}: {grade[1]} ({grade[2]}%)')
        
        print(f'There are {len(course_grades)} students in {course}.\n')
        print(f'Search time: {time.time() - start_time} seconds')

    @staticmethod
    def get_course_average(course):
        course_grades = []
        grades = Grades.get_grades()
        for grade in grades:
                if grade[3] == course:
                    course_grades.append(int(grade[2]))
        class_average = sum(course_grades) / len(course_grades)
        return class_average
    
    @staticmethod
    def get_course_median(course):
        course_grades = []
        grades = Grades.get_grades()
        for grade in grades:
                if grade[3] == course:
                    course_grades.append(int(grade[2]))
        class_median = statistics.median(course_grades)
        return class_median

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    '''linked list class that allows for efficient insertion/deletion/sorting of data'''
    def __init__(self):
        self.head = None
    
    def check_head(self):
        return True if self.head is not None else False
    
    def check_for_data_in_ll(self, data):
        if self.check_head():
            c1 = self.head
            while c1 is not None:
                if c1.data[0] == data:
                    print(f'{data} already exists in the system!')
                    return True
                else:
                    c1 = c1.next
                    
            return False
    
    def add_first(self, data):
        '''add first node if linked list is empty'''
        if self.head is None: 
            self.head = Node(data)
        else:
            c1 = self.head 
            self.head = Node(data) 
            self.head.next = c1 

    def add_new(self, data):
        '''add node at last position'''
        if self.head is None:
            self.head = Node(data)
        else:
            c1 = self.head
            while c1.next is not None:
                c1 = c1.next 
            c1.next = Node(data) 

    def print(self):
        '''print the  linked list'''
        if self.check_head(): 
           c1 = self.head
        if self.head is not None:
            c1 = self.head
            while c1 is not None:
                print(c1.data)
                c1 = c1.next 

    def size(self):
        '''get the size of linked list'''
        count=0
        c1 = self.head
        while c1:
            c1 = c1.next
            count = count + 1
        return count

    def delete_node(self, data):
        '''delete the linked list's node with specific data'''
        flag = False
        prev_node = None
        if self.check_head(): 
            c1 = self.head 
            while c1 is not None: 
                if c1.data[0] == data: 
                    print(f'Deleting {data}... \n')
                    if prev_node is None: # checking if first node; if so, move head to the next node
                        flag = True 
                        self.head = c1.next
                        print(f'{data} successfully deleted!')
                        break
                    else: # if not first node, point previous node to the node after this one
                        flag = True
                        prev_node.next = c1.next
                        print(f'{data} successfully deleted!')
                        break
                prev_node = c1
                c1 = c1.next
        else:
            print("There are currently no values to delete!")

        if not flag:
            print(f"{data} was not found in the system!")

# HELPER FUNCTIONS
def get_data(file):
    # linked list method
    data_ll = LinkedList()
    with open(file, newline = '') as csvfile:
        dataset = csv.reader(csvfile)
        header = next(dataset)
        for data in dataset:
            data_ll.add_new(data)

    # array method
    data_list = []
    c1 = data_ll.head
    while c1:
        data_list.append(c1.data)
        c1 = c1.next
    
    return data_ll, data_list, header

def add_student():
    '''gets student details for add_new_student()'''
    first_name = input('Enter first name of student: ')
    last_name = input('Enter last name of student: ')
    email_address = input('Enter email of student: ')
    course_ids = input('Enter the course that the student is enrolled in: ')
    grades = input('Enter the grade the student has in the course: ')
    marks = input('Enter the mark in integer form of the student: ')
    return first_name.strip(), last_name.strip(), email_address.strip(), course_ids.strip(), grades.strip(), marks.strip()

def get_student(email_address):
    '''get one student's details'''
    start_time = time.time()
    student_list = get_data('student.csv')[1]
    for student in student_list:
        if student[0] == email_address:
            current_student = Student(student[1], student[2], student[0], student[3], student[4], student[5])
            print(f'Search time: {time.time() - start_time} seconds')
            return current_student
    else:
        print('No student found with the email!')
        return None

def get_professor(email_address):
    '''get one professor's details'''
    start_time = time.time()
    professor_list = get_data('professor.csv')[1]
    for professor in professor_list:
        if professor[0] == email_address:
            current_professor = Professor(professor[0], professor[1], professor[2], professor[3])
            print(f'Search time: {time.time() - start_time} seconds')
            return current_professor
    else:
        print('No professor found with the email!')
        return None

def add_course():
    '''gets course details for add_new_course()'''
    course_id = input('Enter id of the course: ') # i.e. DATA200
    str_credits = input('Enter the number of credits of the course: ')
    course_name = input('Enter the name of the course: ')
    course_description = input('Enter the description of the course: ')
    try:
        credits = int(str_credits)
        if credits > 0:
            return course_id.strip(), credits, course_name.strip(), course_description.strip()
        else:
            print('Credits must be a non-zero/non-negative number!')
    except ValueError:
        print('Credits are invalid! Enter a valid integer!')

def add_professor():
    '''gets professor details for add_new_professor()'''
    name = input('Enter the name of the professor: ')
    email_address = input('Enter the email of the professor: ')
    rank = input('Enter the rank of the professor: ')
    course_id = input('Enter the course id of the course the professor teaches: ')
    return email_address.strip(), name.strip(), rank.strip(), course_id.strip()

def add_grade():
    '''gets grade details for add_new_grade()'''
    id = input('Enter id of the grade: ') 
    grade = input('Enter the grade: ') # letter grade 
    mark = input('Enter mark: ') # integer percentage
    return id.strip(), grade.strip(), int(mark.strip())

def add_to_file(file, data): 
    '''add new line to given file with data'''
    with open(file, 'a', newline = '') as writingfile:
        writer = csv.writer(writingfile)
        writer.writerow(data)

def write_to_file_array(file, header, data): 
    '''rewrite to given file with data using array'''
    with open(file, 'w', newline = '') as writingfile:
        writer = csv.writer(writingfile)
        writer.writerow(header)
        writer.writerows(data)

def write_to_file_ll(file, header, data): 
    '''rewrite to given file with data using linked list'''
    formatted_data = []
    formatted_data.append(header)
    c1 = data.head

    while c1:
        formatted_data.append(c1.data)
        c1 = c1.next

    with open(file, 'w', newline = '') as writingfile:
        writer = csv.writer(writingfile)
        writer.writerows(formatted_data)

def checkmygrade_main_menu():
    while True:
        columns = shutil.get_terminal_size().columns
        print(__file__)
        print('================================='.center(columns))
        print('Welcome to CheckMyGrade'.center(columns))
        print('================================'.center(columns))
        print('\n CheckMyGrade Menu:')
        print('1. Login')
        print('2. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            print('Logging in...')
            email_address = input('Enter your email address: ')
            password = getpass.getpass('Enter your password: ')
            current_user = LoginUser(email_address.strip(), password.strip())
            status, email_address, role = current_user.login()
            print(status, email_address, role) 
            if status:
                if role == 'student':
                    current_student = get_student(current_user.email_address)
                    while True:
                        print(__file__)
                        print('================================='.center(columns))
                        msg='''Welcome to CheckMyGrade'''
                        print(msg.center(columns))
                        msg2='''Student Portal'''
                        print(msg2.center(columns))
                        print('================================'.center(columns))
                        print('\n CheckMyGrade Main Menu:')
                        print('1. Check my grade')
                        print('2. Check my mark')
                        print("3. Compare my mark against course average")
                        print('4. Change my password')
                        print('5. Logout')
                        choice = input('Enter what you would like to do: ')
                        if choice == '1':
                            print('Checking your grade...')
                            current_student.check_my_grades()
                        elif choice == '2':
                            print('Checking your mark...')
                            current_student.check_my_marks()
                        elif choice == '3':
                            print('Getting information for comparison...')
                            course_ids = current_student.course_ids.split('|')
                            marks = current_student.marks.split('|')
                            for idx, course in enumerate(course_ids):
                                print(f'Class {idx+1}: {course}')
                                print(f'Your mark: {marks[idx]}%')
                                course_average = Grades.get_course_average(course)
                                print(f'Average: {course_average:1f}%')
                                course_median = Grades.get_course_median(course)
                                print(f'Median: {course_median}%')
                        elif choice == '4':
                            print('Changing your password...')
                            current_user.change_password()
                        elif choice == '5':
                            print('Logging out...')
                            current_user.logout()
                            break
                        else:
                            print('Enter a valid choice!')
                elif role == 'professor':
                    current_professor = get_professor(current_user.email_address)
                    while True:
                        print(__file__)
                        print('================================='.center(columns))
                        msg='''Welcome to CheckMyGrade'''
                        print(msg.center(columns))
                        msg2='''Professor Portal'''
                        print(msg2.center(columns))
                        print('================================'.center(columns))
                        print('\n CheckMyGrade Main Menu:')
                        print('1. Check my course')
                        print('2. Get grade report for my course')
                        print('3. Change student grades/marks')
                        print('4. Change my password')
                        print('5. Logout')
                        choice = input('Enter what you would like to do: ')
                        if choice == '1':
                            print('Retrieving your course details...')
                            current_professor.show_course_details_by_professor()
                        elif choice == '2':
                            print(f'Getting grade report for your course ({current_professor.course_id})...')
                            Grades.display_grades_by_course(current_professor.course_id)
                            course_average = Grades.get_course_average(current_professor.course_id)
                            print(f'Course average: {course_average}%')
                            course_median = Grades.get_course_median(current_professor.course_id)
                            print(f'Course median: {course_median}')
                        elif choice == '3':
                            print('Showing list of students in your course...')
                            Grades.display_grades_by_course(current_professor.course_id)
                            student_email = input('Enter the email of the student you would like to edit: ')
                            update_student = get_student(student_email)
                            if update_student:
                                course_list = update_student.course_ids.split('|')
                                grades_list = update_student.grades.split('|')
                                marks_list = update_student.marks.split('|')
                                idx = course_list.index(current_professor.course_id)
                                updated_mark = input(f'Enter the new mark for {update_student.first_name} {update_student.last_name}: ')
                                if isinstance(int(updated_mark), int):
                                    if 0 <= int(updated_mark) <= 100:
                                        updated_grade = input(f'Enter the new grade for {update_student.first_name} {update_student.last_name}: ')
                                        new_grade = update_student.grades.replace(grades_list[idx], updated_grade)
                                        new_mark = update_student.marks.replace(marks_list[idx], updated_mark)
                                        update_student.update_student_record(new_grade, new_mark)
                                    else:
                                        print('New mark must be valid (between 0 to 100!)')         
                                else:
                                    print(f'The current grade and mark for {update_student.first_name} {update_student.last_name} is {update_student.grades} ({update_student.marks}%)')
                                    new_mark = input(f'Enter the new mark for {update_student.first_name} {update_student.last_name}: ')
                                    if isinstance(int(new_mark), int):
                                        if 0 <= int(new_mark) <= 100:
                                            new_grade = input(f'Enter the new grade for {update_student.first_name} {update_student.last_name}: ')
                                            update_student.update_student_record(new_grade, new_mark)
                                        else:
                                            print('New mark must be valid (between 0 to 100!)')
                                    else:
                                        print('Please enter a valid integer!')
                            else:
                                print('Please try again!')
                        elif choice == '4':
                            print('Changing your password...')
                            current_user.change_password()
                        elif choice == '5':
                            print('Logging out...')
                            current_user.logout()
                            break
                        else:
                            print('Enter a valid choice!')
                elif role == 'admin':
                    while True:
                        print(__file__)
                        print('================================='.center(columns))
                        msg='''Welcome to CheckMyGrade'''
                        print(msg.center(columns))
                        msg2='''Admin Portal'''
                        print(msg2.center(columns))
                        print('================================'.center(columns))
                        print('1. Show student options')
                        print('2. Show professor options')
                        print('3. Show course options')
                        print('4. Logout')
                        choice = input('Enter what you would like to do: ')
                        if choice == '1':
                            student_screen = True
                            while student_screen:
                                print(__file__)
                                print('================================='.center(columns))
                                msg='''Welcome to CheckMyGrade'''
                                print(msg.center(columns))
                                msg2='''Admin Portal (Student Screen)'''
                                print(msg2.center(columns))
                                print('================================'.center(columns))
                                print('1. Display all students')
                                print('2. Sort students')
                                print('3. Search students')
                                print('4. Get all grades')
                                print('5. Add student')
                                print('6. Modify student grade/mark')
                                print('7. Delete student')
                                print('8. Go back')
                                student_choice = input('Enter what you would like to do: ')
                                if student_choice == '1':
                                    print('Retrieving all students...')
                                    Student.display_records()
                                elif student_choice == '2':
                                    print('Sort students...')
                                    print('''How would you like to sort?
                                            1. By student ID (email address) 
                                            2. By student ID (email address) (reversed)
                                            3. By grade
                                            4. By grade (descending)
                                            ''')
                                    sort_by = input('Enter number of how you would like to sort: ')
                                    if sort_by == '1':
                                        Student.sort_students('email', 'default')
                                    elif sort_by == '2':
                                        Student.sort_students('email', 'reverse')
                                    elif sort_by == '3':
                                        Student.sort_students('grade', 'default')
                                    elif sort_by == '4':
                                        Student.sort_students('grade', 'reverse')
                                    else:
                                        print('Incorrect input for sorting!')
                                elif student_choice == '3':
                                    print('Search for student...')
                                    student_id = input('Enter student email: ')
                                    searched_student = get_student(student_id)
                                    if searched_student:
                                        print(f'Displaying information for {searched_student.first_name} {searched_student.last_name}')
                                        course_list = searched_student.course_ids.split('|')
                                        print(f'{searched_student.email_address} is currently taking {len(course_list)} courses.')
                                        grades_list = searched_student.grades.split('|')
                                        marks_list = searched_student.marks.split('|')
                                        for idx, course in enumerate(course_list):
                                            print(f'{course}')
                                            print(f"{grades_list[idx]} ({marks_list[idx]}%)")
                                            course_average = Grades.get_course_average(course)
                                            print(f'Above average ({course_average}%)') if int(marks_list[idx]) >= course_average else print(f'Below average ({course_average}%)')
                                elif student_choice == '4':
                                    print('Displaying all grades...')
                                    Grades.display_grade_report()
                                elif student_choice == '5':
                                    print('Adding student...')
                                    first_name, last_name, email_address, course_ids, grades, marks = add_student()
                                    new_student = Student(first_name, last_name, email_address, course_ids, grades, marks)
                                    new_student.add_new_student(new_student)
                                elif student_choice == '6':
                                    print('Modifying student...')
                                    student_id = input('Enter the email of the student you would like to edit: ')
                                    update_student = get_student(student_id)
                                    if update_student:
                                        course_list = update_student.course_ids.split('|')
                                        grades_list = update_student.grades.split('|')
                                        marks_list = update_student.marks.split('|')
                                        if len(course_list) > 1:
                                            for idx, course in enumerate(course_list):
                                                print(f'{idx + 1}. {course}: {grades_list[idx]} ({marks_list[idx]}%)')
                                            modify_grade = input('Enter the number of the course you would like to update the grade/mark for: ')
                                            if 0 < int(modify_grade) < len(course_list):
                                                updated_mark = input(f'Enter the new mark for {update_student.first_name} {update_student.last_name}: ')
                                                if isinstance(int(updated_mark), int):
                                                    if 0 <= int(updated_mark) <= 100:
                                                        updated_grade = input(f'Enter the new grade for {update_student.first_name} {update_student.last_name}: ')
                                                        new_grade = update_student.grades.replace(grades_list[int(modify_grade)-1], updated_grade)
                                                        new_mark = update_student.marks.replace(marks_list[int(modify_grade)-1], updated_mark)
                                                        update_student.update_student_record(new_grade, new_mark)
                                                    else:
                                                        print('New mark must be valid (between 0 to 100!)')
                                                else:
                                                    print('Please enter a valid integer!')
                                            else:
                                                print('Invalid number selected!')
                                        else:
                                            print(f'The current grade and mark for {update_student.first_name} {update_student.last_name} is {update_student.grades} ({update_student.marks}%)')
                                            new_mark = input(f'Enter the new mark for {update_student.first_name} {update_student.last_name}: ')
                                            if isinstance(int(new_mark), int):
                                                if 0 <= int(new_mark) <= 100:
                                                    new_grade = input(f'Enter the new grade for {update_student.first_name} {update_student.last_name}: ')
                                                    update_student.update_student_record(new_grade, new_mark)
                                                else:
                                                    print('New mark must be valid (between 0 to 100!)')
                                            else:
                                                print('Please enter a valid integer!')
                                    else:
                                        print('Please try again!')
                                elif student_choice == '7':
                                    print('Deleting student...')
                                    email_address = input('Enter the email address of the student to be deleted: ')
                                    delete_student = Student(first_name = None, last_name = None, email_address = None, course_ids = None, grades = None, marks = None)
                                    delete_student.delete_student(email_address)
                                elif student_choice == '8':
                                    print('Returning to option screen...')
                                    student_screen = False
                                else:
                                    print('Invalid choice!')
                        elif choice == '2':
                            professor_screen = True
                            while professor_screen:
                                print(__file__)
                                print('================================='.center(columns))
                                msg='''Welcome to CheckMyGrade'''
                                print(msg.center(columns))
                                msg2='''Admin Portal (Professor Screen)'''
                                print(msg2.center(columns))
                                print('================================'.center(columns))
                                print('1. Display all professors')
                                print('2. Search course details by professor')
                                print('3. Get grade report for professor')
                                print('4. Add professor')
                                print('5. Modify professor')
                                print('6. Delete professor')
                                print('7. Go back')
                                professor_choice = input('Enter what you would like to do: ')
                                if professor_choice == '1':
                                    print('Retrieving all professors...')
                                    Professor.professors_details()
                                elif professor_choice == '2':
                                    professor_id = input('Enter email of the professor to get their course details: ')
                                    current_professor = get_professor(professor_id)
                                    if current_professor:
                                        current_professor.show_course_details_by_professor()
                                elif professor_choice == '3':
                                    professor_id = input('Enter email of the professor to get their course grade report: ')
                                    current_professor = get_professor(professor_id)
                                    if current_professor:
                                        Grades.display_grades_by_course(current_professor.course_id)
                                        course_average = Grades.get_course_average(current_professor.course_id)
                                        print(f"The average for {current_professor.name}'s course is {course_average}%")
                                elif professor_choice == '4':
                                    print('Adding professor...')
                                    email_address, name, rank, course_id = add_professor()
                                    new_professor = Professor(email_address, name, rank, course_id)
                                    new_professor.add_new_professor(new_professor)
                                elif professor_choice == '5':
                                    print('Update professor details...')
                                    email_address = input('Enter the email address of the professor you wish to modify: ')
                                    update_professor = get_professor(email_address)
                                    if update_professor:
                                        new_rank = input(f'Enter the new rank of {update_professor.name}: ')
                                        update_professor.modify_professor_details(new_rank)
                                    else:
                                        print('Professor not found! Make sure you entered their email correctly.')
                                elif professor_choice == '6':
                                    print('Deleting professor...')
                                    email_address = input('Enter the email address of the professor to be deleted: ')
                                    delete_professor = Professor(email_address = None, name = None, rank = None, course_id = None)
                                    delete_professor.delete_professor(email_address)
                                elif professor_choice == '7':
                                    print('Returning to option screen...')
                                    professor_screen = False
                                else:
                                    print('Invalid choice!')
                        elif choice == '3':
                            course_screen = True
                            while course_screen:
                                print(__file__)
                                print('================================='.center(columns))
                                msg='''Welcome to CheckMyGrade'''
                                print(msg.center(columns))
                                msg2='''Admin Portal (Course Screen)'''
                                print(msg2.center(columns))
                                print('================================'.center(columns))
                                print('1. Display all courses')
                                print('2. Get grade report for course')
                                print('3. Add course')
                                print('4. Delete course')
                                print('5. Go back')
                                course_choice = input('Enter what you would like to do: ')
                                if course_choice == '1':
                                    print('Retrieving all courses...')
                                    Course.display_courses()
                                elif course_choice == '2':
                                    course_id = input('Enter the course id of the course you would like to get a grade report for: ')
                                    Grades.display_grades_by_course(course_id)
                                elif course_choice == '3':
                                    print('Adding course...')
                                    course_id, course_name, course_credits, course_description = add_course()
                                    new_course = Course(course_id, course_credits, course_name, course_description)
                                    if new_course:
                                        new_course.add_new_course(new_course)
                                    else:
                                        print('Issue adding course! Make sure you are entering the course details correctly.')
                                elif course_choice == '4':
                                    print('Deleting course...')
                                    course_id = input('Enter the course id to be deleted: ')
                                    delete_course = Course(course_id = None, credits = None, course_name = None, course_description = None)
                                    delete_course.delete_course(course_id)
                                elif course_choice == '5':
                                    print('Returning to option screen...')
                                    course_screen = False
                                else:
                                    print('Invalid choice!')
                        elif choice == '4':
                            print('Logging out...')
                            current_user.logout()
                            break
                        else: 
                            print('Enter a valid choice!')
                        
        elif choice == '2':
            print('Exiting CheckMyGrade... Goodbye!')
            break
        else:
            print('Invalid choice! Please try again.')

if __name__ == '__main__':
    # uncomment out to run unit tests
    # unittest.main()
    checkmygrade_main_menu()

           