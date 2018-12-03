# Class

```python
# Parent class of HighSchoolStudent below
class Student:
    # static property
    school_name = "Sprinfield Elementary"

    # constructor
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.namej

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


# Inherit class
class HighSchoolStudent(Student):
    # override static property
    school_name = "Springfield High"

    # override parent method
    def get_school_name(self):
        return "This is a High School Student"

    # call parent method with super()
    def get_name_capitalize(self):
        orig_value = super().get_name_capitalize()
        return orig_value + "HS"

```


