n = int(input("enter the number : "))
 # rigth angle traingle right aligned
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*i , end="")
    print()