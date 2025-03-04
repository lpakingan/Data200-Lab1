import getpass
import csv

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
                    if c1.data[1] == self.password:
                        print("You are now logged in!")
                        login_exists = True
                        break
                    else:
                        print("Incorrect password!")
                        login_exists = True
                        break
                else: 
                    print('Checking next...')
                    c1 = c1.next

        if not login_exists:
            print('The email address is not associated with an account!')
                
        # insert code for encrypting/decrypting password

    def logout(self):
        '''logs the current user out of the system'''

    def change_password(self, email_address):
        '''changes a user's password using their email'''

    def encrypt_password(self, email_address):
        '''encrypts a user's password using their email'''

    def decrypt_password(self, email_address):
        '''decrypts a user's password usign their email'''


class Student:
    '''student class that includes information regarding a student's name, email, grades/marks'''
    def __init__(self, first_name, last_name, email_address, course_ids = None, grades = None, marks = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.course_ids = course_ids
        self.grades = grades
        self.marks = marks
    
    @staticmethod
    def get_students():
        # linked list method
        student_ll = LinkedList()
        with open('student.csv', newline = '') as csvfile:
            students = csv.reader(csvfile)
            header = next(students)
            for student in students:
                student_ll.add_new(student)

        # array method
        student_list = []
        c1 = student_ll.head
        while c1:
            student_list.append(c1.data)
            c1 = c1.next
        
        return student_ll, student_list, header

    @staticmethod
    def display_records():
        '''displays student records'''
        # linked list method
        students_ll = Student.get_students()[0]
        students_ll.print()
    
    def add_new_student(self, student): # student from add_student()
        '''add a new student into the system'''
        # linked list method
        students_ll = self.get_students()[0]
        student_info = [student.email_address, student.first_name, student.last_name, None, None, None]
        student_exists = False
        if students_ll.check_head():
            c1 = students_ll.head
            while c1 is not None:
                if c1.data[0] != student.email_address:
                    c1 = c1.next
                    print('Checking next...')
                else: 
                    print('Student already exists!')
                    student_exists = True
                    break
        else:
            students_ll.add_first(student_info)
            add_to_file('student.csv', student_info)
            print(f'{student.first_name} {student.last_name} successfully added! (First student added)')
            students_ll.print()

        if not student_exists:
            students_ll.add_new(student_info)
            add_to_file('student.csv', student_info)
            print(f'{student.first_name} {student.last_name} successfully added! (Another student added)')
            students_ll.print()

    def delete_student(self, email_address):
        '''delete a student in the system using their email address'''
        # linked list method
        students_ll, student_list, header = self.get_students()
        try:
            students_ll.delete_node(email_address)
            write_to_file_ll('student.csv', header, students_ll)
        except Exception as e:
            print(f'Error deleting student: {e}!')

    def check_my_grades(self):
        '''lets student check their own grades'''
        # array method
        student_list = self.get_students()[1]
        for student in student_list:
            if student[0] == self.email_address:
                print(f"You currently have a {self.grades} in {self.course_ids}")

    def update_student_record(self, new_grade, new_mark):
        '''updates a student's record by using their email address'''
        # array method
        students_ll, student_list, header = self.get_students()
        for student in student_list:
            if student[0] == self.email_address:
                student[4] = new_grade 
                self.grades = new_grade
                student[5] = new_mark 
                self.marks = new_mark
        write_to_file_array('student.csv', header, student_list)
        print(f'The grade and mark for {self.first_name} {self.last_name} has been updated to {self.grades} ({self.marks}%)')

    def check_my_marks(self):
        '''lets student check their own marks'''
        # array method
        student_list = self.get_students()[1]
        for student in student_list:
            if student[0] == self.email_address:
                print(f"You currently have a mark of {self.marks}% in {self.course_ids}")

class Course:
    '''course class that includes information regarding a course's id, credits, name'''
    def __init__(self, course_id, credits, course_name, course_description):
        self.course_id = course_id
        self.credits = credits
        self.course_name = course_name
        self.course_description = course_description
    
    @staticmethod # static to call outside of course object
    def get_courses():
        # linked list method
        course_ll = LinkedList()
        with open('course.csv', newline = '') as csvfile:
            courses = csv.reader(csvfile)
            header = next(courses)
            for course in courses:
                course_ll.add_new(course)

        # array method
        course_list = []
        c1 = course_ll.head
        while c1:
            course_list.append(c1.data)
            c1 = c1.next
        
        return course_ll, course_list, header

    @staticmethod # static to call out of course object
    def display_courses():
        '''displays all courses'''
        courses_ll = Course.get_courses()[0]
        courses_ll.print()

    def add_new_course(self, course): # course from add_course()
        '''add a new course'''
        courses_ll = Course.get_courses()[0]
        course_info = [course.course_id, course.credits, course.course_name, course.course_description]
        course_exists = False
        if courses_ll.check_head():
            c1 = courses_ll.head
            while c1 is not None:
                if c1.data[0] != course.course_id:
                    c1 = c1.next
                    print('Checking next...')
                else: 
                    print('Course already exists!')
                    course_exists = True
                    break
        else:
            courses_ll.add_first(course_info)
            add_to_file('course.csv', course_info)
            print(f'{course.course_id} successfully added! (First course added)')
            courses_ll.print()

        if not course_exists:
            courses_ll.add_new(course_info)
            add_to_file('course.csv', course_info)
            print(f'{course.course_id} successfully added! (Another course added)')
            courses_ll.print()

    def delete_course(self, id):
        '''delete a course using its id'''
        courses_ll, course_list, header = self.get_courses()
        try:
            courses_ll.delete_node(id)
            write_to_file_ll('course.csv', header, courses_ll)
        except Exception as e:
            print(f'Error deleting student: {e}!')
    
class Professor:
    '''professor class that includes information regarding a professor's name, email, rank'''
    def __init__(self, name, email_address, rank):
        self.name = name
        self.email_address = email_address
        self.rank = rank
        self.course_id = '' # has-a variable; differs for each professor instance

    def professors_details(self):
        '''displays all professors'''

    def add_new_professor(self, email_address): # professor from add_professor()
        '''add a new professor into the system'''
    
    def delete_professor(self, email_address):
        '''delete a professor using their email address'''

    def modify_professor_details(self, email_address):
        '''modify a professor in the system using their email address'''

    def show_course_details_by_professor(self, email_address):
        '''show a professor's course using their email address'''
    
class Grades:
    '''grades class that includes information regarding a specific grade for a student'''
    def __init__(self, id, grade, mark):
        self.id = id # email address to match with the student it is assigned to?
        self.grade = grade
        self.mark = mark

    def display_grade_report(self):
        '''displays a report of all the grades'''
    
    def add_new_grade(self, grade): # grade from add_grade()
        '''add a new grade into the system'''

    def delete_grade(self, id):
        '''delete a grade using its id'''

    def modify_grade(self, id):
        '''change a grade using its id'''

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
        
        print("The linked list size is", count)

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
                        break
                    else: # if not first node, point previous node to the node after this one
                        flag = True
                        prev_node.next = c1.next
                        break
                prev_node = c1
                c1 = c1.next
        else:
            print("There are currently no values to delete!")

        if not flag:
            print(f"{data} was not found in the system!")

# HELPER FUNCTIONS
def add_student():
    '''gets student details for add_new_student()'''
    first_name = input('Enter first name of student: ')
    last_name = input('Enter last name of student: ')
    email_address = input('Enter email of student: ')
    return first_name.strip(), last_name.strip(), email_address.strip()

def get_student():
    '''get one student's details'''
    student_list = Student.get_students()[1]
    email_address = input('Enter the email of the student: ')
    for student in student_list:
        if student[0] == email_address:
            current_student = Student(student[1], student[2], student[0], student[3], student[4], student[5])
            return current_student
    else:
        print('No student found with the email!')
        return None

def add_course():
    '''gets course details for add_new_course()'''
    course_id = input('Enter id of the course: ') # i.e. DATA200
    credits = input('Enter the number of credits of the course: ')
    course_name = input('Enter the name of the course: ')
    course_description = input('Enter the description of the course: ')
    return course_id.strip(), int(credits.strip()), course_name.strip(), course_description.strip()

def add_professor():
    '''gets professor details for add_new_professor()'''
    name = input('Enter the name of the professor: ')
    email_address = input('Enter the email of the professor: ')
    rank = input('Enter the rank of the professor: ')
    return name.strip(), email_address.strip(), int(rank.strip())

def add_grade():
    '''gets grade details for add_new_grade()'''
    id = input('Enter id of the grade: ') # could be number?
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

if __name__ == "__main__":
    ####### LOGINUSER
    # logging in
    email_address = input("Enter your email_address: ")
    password = getpass.getpass("Enter your password: ")
    login = LoginUser(email_address.strip(),password.strip())
    login.login()

    ####### STUDENT
    # displaying student records
    Student.display_records()

    # adding new student
    first_name, last_name, email_address = add_student()
    new_student = Student(first_name, last_name, email_address)
    new_student.add_new_student(new_student)

    # deleting student
    email_address = input('Enter the email address of the student to be deleted: ')
    delete_student = Student(first_name = None, last_name = None, email_address = None)
    delete_student.delete_student(email_address)

    # student checking grades/marks and update
    current_student = get_student()
    current_student.check_my_grades()
    current_student.check_my_marks()
    current_student.update_student_record('B', '85')

    ####### COURSES
    # displaying courses
    Course.display_courses()

    # adding new course
    course_id, course_name, course_credits, course_description = add_course()
    new_course = Course(course_id, course_credits, course_name, course_description)
    new_course.add_new_course(new_course)

    # deleting course
    course_id = input('Enter the course id to be deleted: ')
    delete_course = Course(course_id = None, credits = None, course_name = None, course_description = None)
    delete_course.delete_course(course_id)

    