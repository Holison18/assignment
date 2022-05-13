"""
    Index number = 3021920
    Name = Kobina Akofi-Holison
    Program = Computer Engineering
    course = COE 251
"""

print("Name: Kobina Akofi-Holison\nIndex No.:3021920")
print()

# Question 1
# Euclidean Algorithm
# To calculate the greatest common divisor of two numbers

def gcd(m,n):
    x = m
    y = n
    while y!=0:
        mod = x % y
        x = y
        y = mod
    print("The GCD of",m,"and",n,"is",x) 
print("_______THE GREATEST COMMON DIVISOR_________")
gcd(int(input("Enter the first number\n>>> ")),int(input("Enter the second number\n>>> ")))
print()





# Question 2. 
# converting number in different bases to base 10

def converting_to_base_10(number,numberbase):
    arr = []
    carry_over = 0
    m = 0
    digit_in_base_10 = number

    # while loop to iterate over the value of the number we want to find it's number base 
    while digit_in_base_10 > 0:
        carry_over = digit_in_base_10 % numberbase
        arr.append(carry_over)
        digit_in_base_10 = int((digit_in_base_10 - carry_over)/numberbase)
    arr.reverse() # reverse the content of arr

    answer = "" #stor answer in an empty string
    for i in arr:
        answer += str(i)
    print(f"Therefore {number} in base {numberbase} is {answer}")

print("_____CONVERTING FROM BASE 10 TO OTHER BASES_______")
converting_to_base_10(int(input("Enter the number\n>>> ")),int(input("Enter the base\n>>> ")))
print()



# Question 3
# adding numbers in other bases

def adding_numbers(num1,num2,numberbase):
    #create empty arrays for num1 and num2 and reverse their content
    num3 = list(num1)
    num3.reverse
    num4 = list(num2)
    num4.reverse

    result = []
    carry_over = 0

    for i in range(len(num1)):
        if len(num1) == len(num2):
            d = (int(num3[i]) + int(num4[i]) + carry_over)/numberbase
            to_store_in_sum = int(int(num3[i]) + int(num4[i]) + carry_over - (numberbase * int(d)))
            result.append(to_store_in_sum)
            carry_over = int(d)
        else:
            print("The numbers should have the same number of digits")
            break
    result.reverse()

    answer = ""
    for digit in result:
        answer += str(result[digit])
    print(f"{num1} + {num2} is {answer}")
print("____ADDITION OF NUMBER BASES______")
adding_numbers(input("Enter the first number\n>>> "),input("Enter second number\n>>> "),int(input("Enter the base\n>>> ")))