class Student:
    def __init__(self, first_name, last_name, age, group, course):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.group = group
        self.course = course

    def get_info(self):
        return f"Ism: {self.first_name}, Familiya: {self.last_name}, Yosh: {self.age}, Guruh: {self.group}, Kurs: {self.course}"


student1 = Student("James", "Doe", 20, "Group-123", "Frontend")
student2 = Student("John", "Doe", 14, "Back-777", "Backend")
student3 = Student("Andrew", "Doe", 18, "Group-456", "Design")


print(student2.get_info())
