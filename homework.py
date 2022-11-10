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