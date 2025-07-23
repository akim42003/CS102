from random import randint

def get_sum(grid, ulc, lrc):
    total = 0
    
    for i in range(ulc[1], lrc[1]+1):
        for j in range(ulc[0], lrc[0]+1):
            total += grid[j][i]
    print(total)
    return total 
def main():
    grid = [[randint(0, 4) for x in range(5)] for y in range(4)]
    for row in grid: 
        print(row)
    ulc = input("Enter row & col for the upper left corner: ")
    ulc = tuple(map(lambda x: int(x), ulc.split(" ")))
    lrc = input("Enter row & col for the lower right corner: ")
    lrc = tuple(map(lambda x: int(x), lrc.split(" ")))
    print(f"The sum of the subgrid is {get_sum(grid, ulc, lrc)}")
    
main()
