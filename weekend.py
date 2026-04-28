def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

def is_palindrome(text):
    if text==text[::-1]:
        return True
    else:
        return False

def is_prime(x):

    for i in range(2,x):
        if x%i==0:
            print("Not a prime")
            break
    else:
        print("prime")
def info(**kwargs):
    for i ,j in kwargs.items():
        print(i,":",j)