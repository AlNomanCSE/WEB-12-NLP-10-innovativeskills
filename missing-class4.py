# my_list= [1,2,3,4,5]
# mixed_list = [1,2,3,True,"Noman",[1,2,3]]
# empty_list = []
# print(type(empty_list))
# print(len(my_list))

fruits = ["apple","banana","mango","orange","grape"]
# print(fruits[0:2])
# print(fruits[0:4:2])
# print(fruits[-1])

# fruits[1:3] = ["x","y"]
# print(fruits)

list_one = ["apple","banana"]
list_one.append("mango")
# print(list_one)
# list_one.insert(1,"new_fruit")
# print(list_one)
list_two= ["orange","grape","banana"]
list_one.extend(list_two)
# print(list_one)

# list_one.remove("apple")
# list_one.pop(1)
# print(list_one)
# del list_one[0]
# print(list_one)


# print("mango" in list_one)
# print(list_one.index("mango"))
# print(list_one.count("banana"))

# my_list = [1,2,45,-10,-2,0]
# my_list.sort(reverse=True)
# print(my_list)

# original = [1,2,3,4]

# new_list = original.copy()

# print(original)
# print(new_list)

# new_list[1:2] = [12]

# print(original)
# print(new_list)

# nested_list = [[1,2,3],[4,5,6],[7,8,9]]
# print(nested_list[1][1])

# flat = [x for x in range(1,10)]

# print(flat)


my_tuple = (1,3)
# print(len(my_tuple))
# single_tuple = (10,) 
# print(type(single_tuple))

colors = ("red","green","blue","red")
# print(colors[2])
# print(colors.count("red"))

person = "noman",30,"dhaka"
print(person)

name,_,city = person
print(city)

