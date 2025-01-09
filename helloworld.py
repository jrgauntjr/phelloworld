def world():
    print("Hello World")
def nreapeatworld(n):
    while n != 0:
        print("Hello World")
        n = n - 1

print("How many times would you like to print Hello World?")
number = input()
if int(number) == 1:
    world()
else:
    nreapeatworld(int(number))
