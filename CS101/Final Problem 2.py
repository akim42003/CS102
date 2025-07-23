def get_diff(w1, w2) -> str:
    
    location = 0
    
    for entry in range(len(w1)):
        if w1[entry] != w2[entry]:
            location += 1
    return location


def main():
    w1: str = input("Enter a word: ")
    w2: str = input(f"Enter a word with {len(w1)} letters: ")
    print(f"The words differ at {get_diff(w1, w2)} locations.")

main()