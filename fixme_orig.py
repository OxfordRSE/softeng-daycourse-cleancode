def add(a,b):
    return a+b

def subtract ( a , b ):
 return a -  b

def multiply(a, b ):
  result= a*b
  return result

def divide(a,b):
    if b!=0:
      return a/b
    else:
       return None

def is_even(n):
  if n%2==0: return True
  else:
   return False

def say_hello(name):print("Hello "+name)

if __name__ == '__main__':
    print(add(2, 3))          # Expected output: 5
    print(subtract(5, 3))     # Expected output: 2
    print(multiply(4, 5))     # Expected output: 20
    print(divide(10, 2))       # Expected output: 5.0
    print(is_even(4))          # Expected output: True
    say_hello("Alice")         # Expected output: Hello Alice
