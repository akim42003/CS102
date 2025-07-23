from random import randint

def get_sorted(numbers):
    
    count = [0]*12 
    sorted_lists = []
    sorted_numbers = []
    for num in numbers:
        count[num]+=1
    for data in range(len(count)):
        sorted_lists.append([data]*count[data])

    for entry in sorted_lists:
       sorted_numbers += entry

    return sorted_numbers
            

def main():
    numbers = [randint(0, 9) for x in range(12)]
    print(f"numbers: {numbers}")
    sorted_numbers = get_sorted(numbers)
    print(f"sorted:  {sorted_numbers}")

main()


