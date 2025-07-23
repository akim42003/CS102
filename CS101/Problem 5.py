def main():
    rows = int(input("Enter a number of rows: "))
    cols = int(input("Enter a number of columns: "))

    beads = [["."] * cols for i in range(rows)]

    # Ask the user to input the number of beads in each column
    for y in range(cols):
        count = int(input("How many beads are in column " + str(y+1) + "? "))
        for x in range(count):
#             print(beads[x][y])
            beads[x][y] = "o"
  
    # Print the resulting grid of beads
#     print(beads)
    for index in range(len(beads)):
        row = beads[len(beads)-index-1]
        print("".join(row))
#         print("".join(row))

main()
