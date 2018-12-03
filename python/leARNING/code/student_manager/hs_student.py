# Class inheritance
class HighSchoolStudent(Student):
    school_name = "Springfield High"

    def get_school_name(self):
        return "This is a High School Student"

    def get_name_capitalize(self):
        orig_value = super().get_name_capitalize()
        return orig_value + "HS"
