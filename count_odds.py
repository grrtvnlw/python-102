# Add the odd numbers between 0 and 5000

# Setup
result = 0


# Work!
# Let's look at the numbers from 0 to 5000
num = 0
while num <= 5000:
    is_odd = num % 2 != 0
    if is_odd:
        print(num)
        result = result + num
    num = num + 1
    # num += 1


# Return/print the result
print(result)
