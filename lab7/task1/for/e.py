x = int(input())

x_str = str(x)

sum_of_digits = 0

for digit in x_str:
    sum_of_digits += int(digit)

print(sum_of_digits)