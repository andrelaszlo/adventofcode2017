with open('1-input.txt') as f:
    data = f.read().strip()

input = [int(c) for c in data]

def get_sum(digits, offset):
    total = 0
    for index, digit in enumerate(digits):
        next_index = (index+offset) % len(digits)
        next_digit = digits[next_index]
        if digit == next_digit:
            total += digit
    return total

print("Answer (part 1):", get_sum(input, 1))
print("Answer (part 2):", get_sum(input, len(input)//2))
