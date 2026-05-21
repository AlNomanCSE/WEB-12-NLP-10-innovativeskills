# student = {
#     "name": "Noman",
#     "age": 30,
#     "gap": 7.20,
#     "is_active": True,
#     "marks": [85, 72, 90],
#     "address": {"city": "Khulna", "state": "Bangladesh"},
#     (1, 2): 5,
# }

# CRUD
# print(student["ad"])
# print(student.get("marks"))

# student = {"name": "Noman"}

# student["is_active"]= "Yes"
# print(student)

student = {"name": "Noman", "age": 30, "is_active": "Yes"}

# student.update({"age": "25", "name": "Abdullah"})

# student["is_active"] = "Yes"

# student.setdefault("email", "abdullahalnomancse@gmail.com")

# print(student.pop("email"))
# print(student)


# print(type(student.keys()))
# print(student.values())
# print(type(student.values()))
# print(student.items())

# for k, v in student.items():
#     print(f"{k} = {v}")

# for k in student:
#     print(f"{k} = {student[k]}")

# print("name" in student)
# print("noman" in student.values())

# squares = {x: x**2 for x in range(1, 4)}
# print(squares)

# names = ["Noman", "Tanvir", "Oni"]
# marks = [85, 82, 80]

# print({x: y for x, y in zip(names, marks)})
x = dict()
print(type(x))
