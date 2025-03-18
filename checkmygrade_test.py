import unittest
import random
from checkmygrade_main import *

class TestCheckMyGrade (unittest.TestCase):
    '''test cases for the above class methods'''
    def test_01_add_students(self):
        '''unit test for checking the successful addition of 1000 sturent records (using linked list)'''
        self.courses = ['DATA200', 'DATA201', 'DATA202', 'DATA203', 'DATA204']

        pre_added_students = get_data('student.csv')[1] # to keep the index of the actual data
        real_data_rows = len(pre_added_students)
        
        for i in range (0, 1000):
            first_name = 'firstname' + str(i)
            last_name = 'lastname' + str(i)
            email_address = last_name + '@myschool.edu'
            course_ids = random.choice(self.courses)
            grades = None # this will be modified in a future test
            marks = random.randint(40,100)
            test_student = Student(first_name, last_name, email_address, course_ids, grades, marks)
            test_student.add_new_student(test_student)
            post_added_students = get_data('student.csv')[1]
        
        self.assertEqual((len(post_added_students)), (real_data_rows + 1000))
        print('1000 students successfully added!')

    def test_02_modify_students(self):
        '''unit test for modifying grades of students; replaces the None values for grades of previous test with actual grades'''
        for i in range (0, 1000):
            last_name = 'lastname' + str(i)
            email_address = last_name + '@myschool.edu'
            test_student = get_student(email_address)

            new_mark = random.randint(40,100)
            if new_mark < 60:
                new_grade = 'F'
            elif 60 <= new_mark <= 64:
                new_grade = 'D-'
            elif new_mark == 65:
                new_grade = 'D'
            elif 66 <= new_mark <= 69:
                new_grade = 'D+'
            elif 70 <= new_mark <= 74:
                new_grade = 'C-'
            elif new_mark == 75:
                new_grade = 'C'
            elif 76 <= new_mark <= 79:
                new_grade = 'C+'
            elif 80 <= new_mark <= 84:
                new_grade = 'B-'
            elif new_mark == 85:
                new_grade = 'B'
            elif 86 <= new_mark <= 89:
                new_grade = 'B+'
            elif 90 <= new_mark <= 94:
                new_grade = 'A-'
            elif new_mark == 95:
                new_grade = 'A'
            elif 96 <= new_mark <= 100:
                new_grade = 'A+'
            test_student.update_student_record(new_grade, new_mark)
        
        self.assertIsNotNone(test_student.grades) # checks to see if the student grades are no longer None
        print('Student grades were modified!')
    
    def test_03_delete_students(self):
        '''unit test for deleting the 1000 sturent records (using linked list)'''
        pre_deleted_students = get_data('student.csv')[1] 
        pre_deleted_students_length = len(pre_deleted_students)
        
        for i in range (0, 1000):
            last_name = 'lastname' + str(i)
            email_address = last_name + '@myschool.edu'
            test_student = Student(first_name = None, last_name = None, email_address = None, course_ids = None, grades = None, marks = None)
            test_student.delete_student(email_address)
            post_deleted_students = get_data('student.csv')[1]
        
        self.assertEqual((len(post_deleted_students)), (pre_deleted_students_length - 1000), 'After 1000 students inserted') 
        print('1000 students were deleted!')

    def test_04_load_file(self):
        '''unit test for checking to see if students from student.csv file were successfully loaded'''
        students_from_file = get_data('student.csv')[0] 
        self.assertGreater(students_from_file.size(), 0)
        print('Student loaded from file successfully')
    
    def test_05_search_from_loaded_file(self):
        '''unit test for timing searches of certain students'''
        print('Searching for students...')
        starting_time_1 = time.time()
        searched_student_1 = get_student('mae@myschool.edu') # get_student inherently calls loads the file (uses get_data function)
        print(f'Amount of time it took to find {searched_student_1.first_name} {searched_student_1.last_name}: {(time.time() - starting_time_1)} seconds')

        starting_time_2 = time.time()
        searched_student_2 = get_student('smart@myschool.edu')
        print(f'Amount of time it took to find {searched_student_2.first_name} {searched_student_2.last_name}: {(time.time() - starting_time_2)} seconds')
    
    def test_06_sort_students(self):
        '''unit test for sorting students by email (asc and desc order)'''
        starting_time_1 = time.time()
        Student.sort_students('email', 'default') # ascending/default
        print(f'Amount of time it took to sort in ascending order: {(time.time() - starting_time_1)} seconds')

        starting_time_2 = time.time()
        Student.sort_students('email', 'reverse') # descending
        print(f'Amount of time it took to sort in ascending order: {(time.time() - starting_time_2)} seconds')

    def test_07_add_delete_course(self):
        '''unit test that checks if a course has been added/modified/deleted'''
        # add course
        test_course = Course('DATA1000',3,'Data Test Course', 'Test course')
        test_course.add_new_course(test_course)

        courses = get_data('course.csv')[1]
        course_ids = [course[0] for course in courses]

        self.assertIn('DATA1000', course_ids) 
        print('Course added successfully!')
    
        # delete course
        test_course.delete_course('DATA1000')
        updated_courses = get_data('course.csv')[1]
        updated_course_ids = [course[0] for course in updated_courses]
        self.assertNotIn('DATA1000', updated_course_ids) 
        print('Course deleted successfully!')

    def test_08_add_modify_delete_professor(self):
        '''unit test that checks if a professor has been added/modified/deleted'''
        # add professor
        test_professor = Professor('professor@myschool.edu', 'Test Professor', 'Lecturer', 'DATA1000')
        test_professor.add_new_professor(test_professor)

        professors = get_data('professor.csv')[1]
        professor_ids = [professor[0] for professor in professors]

        self.assertIn('professor@myschool.edu', professor_ids) 
        print('Professor added successfully!')

        # modify professor
        test_professor.modify_professor_details('Tenured Lecturer')
        self.assertIsNot('Lecturer', test_professor.rank) # check if the professor object's rank was modified
        print('Professor updated successfully!')
    
        # delete professor
        test_professor.delete_professor('professor@myschool.edu')
        updated_professors = get_data('professor.csv')[1]
        updated_professor_ids = [professor[0] for professor in updated_professors]
        self.assertNotIn('professor@myschool.edu', updated_professor_ids) 
        print('Professor deleted successfully!')

if __name__ == '__main__':
    unittest.main()