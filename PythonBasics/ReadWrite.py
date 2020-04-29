file = open("Test.txt")
# print(file.read(9))

# print(file.readline())
# print(file.readline())


# Print line by line using readline method

# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

file.close()
