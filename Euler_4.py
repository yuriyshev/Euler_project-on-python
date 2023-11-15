'''
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(num:int) -> bool:
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False
    
x = list(range(999,99,-1))
y = x

palindromic_numbers = []
for i in x:
    for j in y:
        x = i*j
        if is_palindrome(x):
            palindromic_numbers.append(x)
            break

print(max(palindromic_numbers))


