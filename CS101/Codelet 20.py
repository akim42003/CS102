from random import randint

def max_indices(grid, threshold):
    indices = []
    new_count = 0
    for row in grid:
        count = 0
        for entry in row:
            if entry > threshold:
                count += 1
            if count > new_count:
                new_count = count
   
    for row in grid:
        final_count = 0
        for data in row:
            if data>threshold:
                final_count += 1
        if final_count == new_count:
            indices.append(grid.index(row))
    return indices

def main():
    # Create the grid:
    num_rows = int(input("Enter a number of rows: "))
    num_cols = int(input("Enter a number of columns: "))
    grid = []
    for row in range(num_rows):
        new_row = []
        for col in range(num_cols):
            new_row.append(randint(1, 9))
        grid.append(new_row)
            
    
    # Print the grid:
    for row in range(num_rows):
        for number in grid[row]:
            print(number, end = " ")
        print()

    threshold = int(input("Enter a threshold: "))
    
    print("the indices of the desired rows are ", max_indices(grid, threshold))
main()