

ItemsInCart = 0

if ItemsInCart != 2:
    # raise Exception("Total cart items mismatch")
    pass

assert(ItemsInCart == 0)

# try and catch

try:
    with open('file.txt', 'r') as reader:
        reader.read()

except:
    print('File not found')

try:
    with open('Test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("End of process")