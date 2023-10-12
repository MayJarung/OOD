def odd_list(al):
    odd_numbers = []

    for number in al:
        if number % 2 == 1:
            odd_numbers.append(number)

    return odd_numbers

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
# print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)