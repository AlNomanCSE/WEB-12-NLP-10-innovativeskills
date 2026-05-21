# makes1 = [85, 71, 90]
# avg1 = sum(makes1) / len(makes1)
# print(f"Avg 1: {avg1}")


# makes2 = [40, 78, 70]
# avg2 = sum(makes1) / len(makes1)
# print(f"Avg 2: {avg1}")


# make3 = [40, 78, 70]
# avg3 = sum(makes1) / len(makes1)
# print(f"Avg 3: {avg1}")

# print("Hello")


# def show_result(marks):
#     avg = sum(marks) / len(marks)
#     print(f"Avg : {avg}")


# show_result([85, 71, 90])
# show_result([40, 78, 70])
# show_result([40, 80, 30])


# def greet(name):
#     print(f"Hello there {name}!")
# greet("Noman")


# def my_sum(num1, num2=100):
#     return num1 + num2


# my_result = my_sum(12, 20)
# print(my_result)


# my_sum(-1, 10)
# my_sum(-12, 10)


# def student_info(name, age, gpa):
#     print(f"Name:-{name} age:-{age} gpa:-{gpa}")


# student_info("Abdullah Al Noman", 30, 7.20)


# def my_number(onukguloNumber):
#     return onukguloNumber[0], onukguloNumber[1], onukguloNumber[2]


# my_list = my_number([1, 2, 3])
# print(my_list)


# print(type(my_list))


# def create_profile(n, a, g, c, ct="Khulna"):
#     return {"Name": n, "Age": a, "Gender": g, "Country": c, "City": ct}


# new_profile = create_profile("Noman", 30, "M", "Bangladesh")
# print(new_profile["Name"])


# def add(*vpa):
#     return sum(num)


# my_sum = add(1, 2, 3, 12, 1, 3)
# print(my_sum)


# def create_profile(**vka):
#     return vka


# my_dict = create_profile(name="Noman", age=30)
# print(my_dict)

# LEGB - scope;

# x = "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#         print("inner x :", x)
#     inner()
#     print("outer x :", x)
# outer()
# print("global x:", x)

# g = "9.81"


# def my_func():
#     g = 212.12
#     print(g)


# my_func()

# print(g)

# count = 0


# def my_func():
#     global count
#     count += 1
#     print(count)


# my_func()

# print(count)


# def square(num):
#     return num**2
# print(square(2))

square = lambda num: num**2
print(square(2))
