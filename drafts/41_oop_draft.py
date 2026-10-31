class Student:
    def __init__(self, name: str, age: int, grade: int) -> None:
        self.name = name
        self.age = age
        self.grade = grade


class Course:
    def __init__(self, name: str, max_students: int) -> None:
        self.name = name
        self.max_students = max_students

        self.students: list[Student] = []

    def add_student(self, student: Student) -> bool:
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self) -> float:
        value = 0
        for student in self.students:
            value += student.grade
        return value / len(self.students)


def main() -> None:
    s1 = Student("Tim", 19, 95)
    s2 = Student("Bill", 19, 75)
    s3 = Student("Jill", 19, 65)

    course = Course("Science", 2)
    course.add_student(s1)
    course.add_student(s2)
    print(course.add_student(s3))  # False
    print(course.get_average_grade())  # 85.0


if __name__ == "__main__":
    main()
