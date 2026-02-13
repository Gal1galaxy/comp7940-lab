# Write a program to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

# your code here
def print_factor(x):
    # your code here
    for i in range(2, x):
        # your code here
        if x % i == 0:
            print(i)

    return x

if __name__ == '__main__':
    for num in l:
        print(f"Factor of {num}:")
        x = num
        print_factor(x)
        print("\n")
