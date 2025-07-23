from random import randint

def pop_front(numbers):
    front = numbers[0]
    numbers.remove(front)
    return front, numbers

def main():
    numbers = [randint(1, 9) for i in range(10)]
    print(f"numbers: {numbers} \n")
    front, numbers = pop_front(numbers)
    print(f"front: {front}")
    print(f"numbers: {numbers}")

main()