list = [0,1,"roger", 2, 3]
# List of values defined

print(list[0])  # should print 0

print(list[2])  # roger

print(list[1:4])  # 1 roger 2

list.insert(0, "trivedi")
print(list)  # trivedi, 0, 1, roger, 2, 3

list.append("last item")
print(list[6])  # last item

print(list)  # trivedi, 0, 1, roger, 2, 3, last item

list[0] = 'TRIVEDI'
print(list)  # TRIVEDI, 0, 1, roger, 2, 3, last item

del list[2]
print(list)  # TRIVEDI, 0, roger, 2, 3, last item

print(list[-1])

# Tuple = same as list but immutable

lst = (1, 2, "ankit", 4.6)

print(lst[1:4])

# lst[2] = "ANKIT"

print(lst)

# Dictionary
dic = {"a": 212, 2: "azt", "c": "lpf"}

print(dic["a"])
print(dic[2])
print(dic["c"])

dict = {}

dict["first name"] = "ANKIT"

dict["last name"] = "TRIVEDI"

print(dict)

dict["gender"] = "Male"

print(dict)

print(dict["first name"])

print(dict["last name"])

print(dict["gender"])
