import os
import time

# Init --------------------------------------------------------------------
os.system("clear")
ending = "Ending."
mat = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, "x"]]

for i in range(4):
    print()
    for j in range(4):
        print(f"{mat[i][j]:<4}",end=" ")

print("\n")

number = int(input("Entry with a number: "))

# -------------------------------------------------------------------------

# Loop process
while True:
    os.system("clear")
    time.sleep(0.01)

    # Change numbers -------------

    #Find number
    #for i in range(4):
    #    for j in range(4):


    #-----------------------------

    for i in range(4):
        print()
        for j in range(4):
            print(f"{mat[i][j]:<4}",end=" ")

    print("\n")

    # Ending process
    if number == -1:
        for e in range(8):
            os.system("clear")
            ending += "."
            print(ending, "\n")
            time.sleep(0.2)
        break

    number = int(input("Entry with a number: "))


os.system("clear")
