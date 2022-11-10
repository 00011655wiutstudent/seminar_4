#using existing code
n = input("Enter any number you want:")
n = int(n)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)


#using my own code
n = int(input("Enter number: "))
if n >= 0:
    print("Blastoff!")
else:
    while n <= 0:
        print(n)
        n = n + 1

# Python program to iterate over characters of a string

# Code #1
string_name = "geeksforgeeks"

# Iterate over the string
for element in string_name:
    print(element, end=' ')
print("\n")

# Code #2
string_name = "GEEKS"

# Iterate over index
for element in range(0, len(string_name)):
    print(string_name[element])

# Python program to iterate over characters of a string

string_name = "Geeks"

# Iterate over the string
for i, v in enumerate(string_name):
    print(v)