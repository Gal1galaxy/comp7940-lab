# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
    for i in range(2, x):
        # your code here
        if x % i == 0:
            print(i)

    return x
