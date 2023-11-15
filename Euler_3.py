'''
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

N = 600_851_475_143

def is_prime(num: int) -> bool:
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            return False
    return True

def main():
    global N
    factors = []
    count = 2
    while N != 1:
        if N % count == 0 and is_prime(count):
            N /= count
            factors.append(count)
        else:
            count += 1
    print(f'Ответ: {count}')
    print(f'Делители: {factors}')


main()


"""
Подсмотрел решение в youtube: https://www.youtube.com/watch?v=eDAMTAz52ss
"""

