#find_prime.py
# to find the nth prime number effieciently

import math
''' Function to determine if a number is prime
    Input: interger k
    Output: true if k is prime, else false
'''
def is_prime(k):


    if k == 0:
        return True
    elif k % 2 == 0:
        return False
    else:
        temp = int(math.sqrt(k)+1)
        for i in range(3, temp, 2):
            if k % i == 0:
                return False
        return True



#main
n = int(input("Enter n: "))

# find nth prime number
count = 0
num = 1
if n == 1:
    num = 2
else:
    while count < n:
        num = num + 2
        if is_prime(num):
            count = count + 1


#Display result
print(num)
