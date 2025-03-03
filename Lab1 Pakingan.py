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
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.marks = [] # has-many variable; calls from Grade
        self.course_ids = [] # has-many variable; calls from Course
        self.grades = [] # has-many variable; calls from Grade
    
    def get_students(self):
        # linked list method
        student_data = LinkedList()
        with open('student.csv', newline = '') as csvfile:
            students = csv.reader(csvfile)
            next(students)
            for student in students:
                student_data.add_new(student)
            return student_data

    def display_records(self):
        '''displays student records'''
        # linked list method
        students = self.get_students()
        students.print()
    
    def add_new_student(self, student): # student from add_student()
        '''add a new student into the system'''
        # linked list method
        students = self.get_students()
        student_info = [student.email_address, student.first_name, student.last_name, None, None, None]
        student_exists = False
        if students.check_head():
            c1 = students.head
            while c1 is not None:
                if c1.data[0] != student.email_address:
                    c1 = c1.next
                    print('Checking next...')
                else: 
                    print('Student already exists!')
                    student_exists = True
                    break
        else:
            students.add_first(student_info)
            add_to_file('student.csv', student_info)
            print(f'{student.first_name} {student.last_name} successfully added! (First student added)')
            students.print()

        if not student_exists:
            students.add_new(student_info)
            add_to_file('student.csv', student_info)
            print(f'{student.first_name} {student.last_name} successfully added! (Another student added)')
            students.print()

    def delete_student(self, email_address):
        '''delete a student in the system using their email address'''
        students = self.get_students()
        student_exists = False
        prev_student = None
        if students.check_head():
            c1 = students.head
            while c1 is not None:
                if c1.data[0] == email_address:
                    print(f'Deleting {c1.data[1]} {c1.data[2]} from the system...')
                    if prev_student is None: # checking if first node; if so, move head to the next node
                        student_exists = True
                        students.head = c1.next
                        # write_to_file('student.csv', students)
                        students.print()
                        break
                    else: # if not first node, point previous node to the node after this one
                        student_exists = True
                        prev_student.next = c1.next
                        # write_to_file('student.csv', students)
                        students.print()
                        break
                prev_student = c1
                c1 = c1.next

        else:
            print('No students in system!')

        if not student_exists:
            print('No student found with the entered email address!')

    def check_my_grades(self, email_address):
        '''checks a student's grades using their email address'''

    def update_student_record(self, email_address):
        '''updates a student's record'''

    def check_my_marks(self, email_address):
        '''checks a student's marks using their email address'''


class Course:
    '''course class that includes information regarding a course's id, credits, name'''
    def __init__(self, course_id, credits, course_name, course_description):
        self.course_id = course_id
        self.credits = credits
        self.course_name = course_name
        self.course_description = course_description

    def display_courses(self):
        '''displays all courses'''

    def add_new_course(self, course): # course from add_course()
        '''add a new course'''

    def delete_course(self, id):
        '''delete a course using its id'''
    
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

    def add_at_index(self, data, newdata):
        '''add node at a specific index'''
        flag = False
        if self.check_head(): 
            c1 = self.head 
            while c1 is not None: 
                if c1.data == data: 
                    print(f'Adding new node with data of {newdata} at node {data}...')
                    nn = Node(newdata) 
                    nn.next = c1.next 
                    c1.next = nn 
                    flag = True 
                    break
                else: 
                    c1 = c1.next
            
        else:
            print("List is empty!")

        if not flag:
            print("No data element found in the linked list!")


    def delete_node(self, data):
        '''delete the linked list's node with specific data'''
        flag = False
        if self.check_head(): 
            c1 = self.head 
            while c1 is not None: 
                if c1.data == data: 
                    print(f'Deleting node with data of {data}... \n')
                    current.next = c1.next
                    flag = True 
                    break
                current = c1
                c1 = c1.next
        else:
            print("List is empty!")

        if not flag:
            print("No data element found in the linked list!")


# HELPER FUNCTIONS
def add_student():
    '''gets student details for add_new_student()'''
    first_name = input('Enter first name of student: ')
    last_name = input('Enter last name of student: ')
    email_address = input('Enter email of student: ')
    return first_name.strip(), last_name.strip(), email_address.strip()

def add_course():
    '''gets course details for add_new_course()'''
    course_id = input('Enter id of the course: ') # i.e. DATA200
    credits = input('Enter the number of credits of the course: ')
    course_name = input('Enter the name of the course: ')
    return course_id.strip(), int(credits.strip()), course_name.strip()

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

def write_to_file(file, data): 
    '''rewrite to given file with data'''
    with open(file, 'w', newline = '') as writingfile:
        writer = csv.writer(writingfile)
        writer.writerows(data)

if __name__ == "__main__":

    # logging in
    email_address = input("Enter your email_address: ")
    password = getpass.getpass("Enter your password: ")
    login = LoginUser(email_address.strip(),password.strip())
    login.login()

    # displaying student records
    records = Student(first_name = None, last_name = None, email_address = None)
    records.display_records()

    # adding new student
    first_name, last_name, email_address = add_student()
    new_student = Student(first_name, last_name, email_address)
    new_student.add_new_student(new_student)

    # deleting student
    email_address = input('Enter the email address of the student to be deleted: ')
    delete_student = Student(first_name = None, last_name = None, email_address = None)
    delete_student.delete_student(email_address)