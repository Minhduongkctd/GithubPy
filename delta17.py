def delta(n):
    if n <= 17:
        return 17 - n
    else:
        return(n - 17) * 2

    print(delta(n))

#Question 17 Test whether a number is within 100 of 1000 or 2000

def test_numb(a):
    return ((abs(1000 - a ) <= 100) or(abs(2000 - a) <= 100))

#Question 18 calculate the sum of three given number, if the values are equal then return thrice of their sum

def sum_thrice(a, b, c):
    sum = a + b + c
    if a == b == c:
        sum = sum*3
    return sum

