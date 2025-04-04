class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades
        self.average = sum(grades.values()) / len(grades)

    def to_dict(self):
        student_dict = {
            "name": self.name,
            "group": self.group,
            "average": self.average,
        }
        student_dict.update(self.grades)
        return student_dict
