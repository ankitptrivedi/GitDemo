
greeting = "Morning!"
a = 0.5
if greeting == "Morning":
    print("We got a match for Greeting!")
else:
    print("No match for Greeting...")

if a == .5:
    print("We have a match for a")
else:
    print("No match for a...")

print("if else condition check complete")

# for loop

obj = [0, 1, 1, 2, 3, 5, 8, 13]
for i in obj:
    print(i*2)
print("Print of fibonacci series complete")

# sum of first 5 natural numbers 1+2+3+4+5 = 15
# range (i,j) -> i to j -1
sums = 0
for j in range(1, 6):
    sums = sums + j
print(sums)
print("print of sum of j complete")

for k in range(1, 10, 3):
    print(k)
print("Print of k complete")

for m in range(10):
    print(m)
print("Print of m complete")
