# file = open('Test.txt')
#
# file.close()

# Read the file and store all the lines in the list
with open('Test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open("Test.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)
