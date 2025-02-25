import getpass

class LoginUser:
    '''user class that includes a user's login information for the application'''
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def login(self):
        '''checks the login details of the current user and logs them in if correct'''

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
        self.courses = [] # has-many variable; calls from Course
        self.grades = [] # has-many variable; calls from Grade

    def display_records(self):
        '''displays student records'''
    
    def add_new_student(self, student): # student from add_student()
        '''add a new student into the system'''
    
    def delete_student(self, last_name):
        '''delete a student in the system using their last name'''

    def check_my_grades(self, last_name):
        '''checks a student's grades using their last name'''

    def update_student_record(self, last_name):
        '''updates a student's record'''

    def check_my_marks(self, last_name):
        '''checks a student's marks using their last name'''


class Course:
    '''course class that includes information regarding a course's id, credits, name'''
    def __init__(self, course_id, credits, course_name):
        self.course_id = course_id
        self.credits = credits
        self.course_name = course_name

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

    def add_new_professor(self, professor): # professor from add_professor()
        '''add a new professor into the system'''
    
    def delete_professor(self, name):
        '''delete a professor using their name'''

    def modify_professor_details(self, name):
        '''modify a professor in the system using their name'''

    def show_course_details_by_professor(self, name):
        '''show a professor's course using their name'''
    
class Grades:
    '''grades class that includes information regarding a specific grade for a student'''
    def __init__(self, id, grade, marks):
        self.id = id
        self.grade = grade
        self.marks = marks

    def display_grade_report(self):
        '''displays a report of all the grades'''
    
    def add_new_grade(self, grade): # grade from add_grade()
        '''add a new grade into the system'''

    def delete_grade(self, id):
        '''delete a grade using its id'''

    def modify_grade(self, id):
        '''change a grade using its id'''


# HELPER FUNCTIONS
def add_student():
    '''gets student details for add_new_student()'''
    first_name = input('Enter first name of student: ')
    last_name = input('Enter last name of student: ')
    email_address = input('Enter email of student: ')
    return first_name.strip(), last_name.strip(), email_address.strip()

def add_course():
    '''gets course details for add_new_course()'''
    course_id = input('Enter id of the course: ') # maybe randomly generate if a number?
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
    '''gets grade detauks for add_new_grade()'''
    id = input('Enter id of the grade: ') # could be number?
    grade = input('Enter the grade: ') # could be float percentage or letter?
    marks = input('Enter marks: ') # get clarification on what this is
    return id.strip(), float(grade.strip()), marks.strip()
