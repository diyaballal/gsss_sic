def is_composite(n):
    if n < 4:  
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

num = input("Enter a number: ")

# Convert digits to list of integers
digits = [int(d) for d in num]

# 1. Sum of even placed digits (considering index starting from 1 on the left)
sum_even_place = sum(digits[i] for i in range(len(digits)) if (i+1) % 2 == 0)

# 2. Sum of odd placed EVEN digits
sum_odd_place_even = sum(digits[i] for i in range(len(digits)) if (i+1) % 2 == 1 and digits[i] % 2 == 0)

# 3. 2nd smallest digit
unique_digits = sorted(set(digits))
second_smallest = unique_digits[1] if len(unique_digits) > 1 else "Not possible"

# 4. 2nd biggest digit
second_biggest = unique_digits[-2] if len(unique_digits) > 1 else "Not possible"

# 5. Sum of composite digits
sum_composite = sum(d for d in digits if is_composite(d))

print("1. Sum of Even placed digits:", sum_even_place)
print("2. Sum of Odd placed Even digits:", sum_odd_place_even)
print("3. 2nd Smallest digit:", second_smallest)
print("4. 2nd Biggest digit:", second_biggest)
print("5. Sum of Composite digits:", sum_composite)
