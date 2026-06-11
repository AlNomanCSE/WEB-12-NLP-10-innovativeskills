class Student:
    school = "ABC University"
    _count = 0

    def __init__(self, name, age, address, marks):
        self.name = name
        self.age = age
        self.address = address
        self.marks = marks
        Student._count += 1

    def average(self):
        return sum(self.marks) / len(self.marks)

    # def __str__(self):
    #     return f"Student: {self.name} | {self.age} | {self.address}"

    @classmethod
    def get_count(cls):
        return f"Total: {cls._count}"


s1 = Student("Noman", 30, "Address", [85, 72, 90])
s2 = Student("X", 20, "KJS", [85, 72, 90])
s3 = Student("Y", 40, "LKJD", [85, 72, 90])

print(s1)
print(s2)
print(s3)


# class Demo:
#     value = 100


# d1 = Demo()
# d1.value = 999

# print(d1.value)
# print(Demo.value)
