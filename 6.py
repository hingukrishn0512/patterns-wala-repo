#     *
#    ***
#   *****
#    ***
#     *


rows = int(input("enter the number of rows : "))

for i in range(rows+1):
    print(" "*(rows-i),end="")
    print("*"*(2*i+1), end="")
    print()
for i in range(rows-1,-1,-1):
      print(" " * (rows-i) + "*" * (2*i+1))
