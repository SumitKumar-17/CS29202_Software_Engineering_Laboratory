# The file  classes.py contains the classes for the different types of users in the system.


class Person:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        self.isAdmin = False


class Student(Person):
    def __init__(self, user_id, password, student_type):
        super().__init__(user_id, password)
        self.student_type = student_type


class Teacher(Person):
    def __init__(self, user_id, password):
        super().__init__(user_id, password)


class UGStudent(Student):
    def __init__(self, user_id, password):
        super().__init__(user_id, password, student_type="UG")


class PGStudent(Student):
    def __init__(self, user_id, password):
        super().__init__(user_id, password, student_type="PG")
