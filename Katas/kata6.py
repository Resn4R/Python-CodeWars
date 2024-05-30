'''
fizzbuzz 
if n % 3 = fiz
if n % 5 = buzz
if n % 3 and 5 = fizzbuzz
'''


def isfizzbuzz(num: int) -> str:
    if num%3 == 0 and num%5 == 0: return "fizzbuzz"
    elif num%5 == 0: return "buzz"
    elif num%3 == 0: return "fizz"
    else: return str(num)