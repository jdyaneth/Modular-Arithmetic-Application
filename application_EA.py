import math

# ACCESSABILITY 

menu = ['1. GCD using Euclidean Algorithm', '2. Bézout coefficients using Extended Euclidean Algorithm', '3. Multiplicative inverse of a modulo n', '4. Integer Factorization', '5. Prime Counter [π(x) function]', '6. Remainder and Quotient', '7. End program']

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

seperator = "-" * 30

# 
# 
# 

# ALGORITHMS

# Substraction-based version of Euclidean Algorithm (Euclid's original version)
def gcd_2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Using Extended Euclidean Algorithm to Calculate Bézout coefficients
def extended_gcd(a, b):
    s = 0;    old_s = 1
    r = b;    old_r = a
         
    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
    
    if b != 0 :
        bezout_t = (old_r - old_s * a) // b
    else:
        bezout_t = 0

    print("Greatest Common Divisor of the given 2 numbers:", old_r)

    return (old_s, bezout_t) 
     

# The multiplicative inverse of a modulo n
def inverse(a, n):
    t = 0;     newt = 1
    r = n;     newr = a

    while newr != 0 :
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt) 
        (r, newr) = (newr, r - quotient * newr)

    if r > 1 :
        return "a is not invertible"
    if t < 0 :
        t = t + n

    return t


# Trial Division Algorithm for integer factorization
def trial_division(n: int) -> list[int]:
    w = []
    while n % 2 == 0:
        w.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            w.append(f)
            n //= f
        else:
            f += 2
    if n != 1: w.append(n)
    # Only odd number is possible
    return w


# Remainder and Quotient
def mod(b, m):
    remain = b % m
    quotient = b // m
    return f"Remainder is {remain}", f"Quotient is {quotient}"

# π(x) function to count primes
def pi(x):
    prime_count = x/ math.log(x)
    return prime_count

# 
# 
# 
# 

# LINKED LIST

# Double Linked List to store the history of operations

# Class for linkedlist node
class Node:
    def __init__(self, data=None, next=None):
        self.prev = None
        self.data = data
        self.next = None


# Class for linkedlist
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None
        else:
            self.head = new_node

    def clear(self):
        self.head = None
        self.tail = None


    def to_string(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next
        return ' <--> '.join(nodes)


class Factors:
    def __init__(self, integer, factors):
        self.integer = integer
        self.factors = factors

    def integer(self):
        return self.integer

    def factors(self):
        return self.factors

    def __str__(self):
        return f"Integer:{self.integer}, Factors:{self.factors}"
    
class Coefficients:
    def __init__(self, integers, coefficients):
        self.integers = integers
        self.coefficients = coefficients

    def integers(self):
        return self.integers

    def coefficients(self):
        return self.coefficients

    def __str__(self):
        return f"Integers:{self.integers}, Coefficients:{self.coefficients}"

class Inverses:
    def __init__(self, modulo, inverse):
        self.modulo = modulo
        self.inverse = inverse

    def modulo(self):
        return self.modulo

    def inverse(self):
        return self.inverse

    def __str__(self):
        return f"Inverse of {self.modulo} is {self.inverse}"

class GCD:
    def __init__(self, integers, gcd):
        self.integers = integers
        self.gcd = gcd

    def integers(self):
        return self.integers

    def gcd(self):
        return self.gcd

    def __str__(self):
        return f"Integers:{self.integers}, GCD:{self.gcd}"

#
#
#
    
dllist = DoubleLinkedList()


#
#
#
# APPLICATION

def Euclidean_Alg():
    print(MAGENTA + "WELCOME TO MODULAR ARITHMETIC APPLICATION !" + RESET)
    print(GREEN + "Press '8' to VIEW result history" + RESET)
    print(RED + "Press '9' to CLEAR result history" + RESET)
    while True:
        print(CYAN + seperator + RESET)
        for option in menu:
                print
                print("\t" + option)

        choice = input(BLUE + "Select option 1-7 >> " + RESET)

        if choice == '1':
             num1 = int(input("Enter 1st number: "))
             num2 = int(input("Enter 2nd number: "))
             answer = gcd_2(num1, num2)
             dllist.add_node(GCD([num1,num2], answer))
             print(GREEN + f"Greatest Common Devisor of '{num1}' and '{num2}' is >>> {answer}" + RESET)
        elif choice == '2':
             num1 = int(input("Enter 1st number: "))
             num2 = int(input("Enter 2nd number: "))
             answer = extended_gcd(num1, num2)
             dllist.add_node(Coefficients([num1,num2], answer))
             print(GREEN + f"Bézout coefficients of '{num1}' and '{num2}' is >>> {answer}" + RESET)
        elif choice == '3':
             print("Enter 'a' and 'n' so that  at≡1(mod n)")
             num1 = int(input("Enter number for 'a': "))
             num2 = int(input("Enter number for 'n': "))
             answer = inverse(num1, num2)
             dllist.add_node(Inverses(f"a={num1}_n={num2}", answer))
             print(GREEN + f"Multiplicative inverse of '{num1}' modulo '{num2}' is >>> {answer}" + RESET)
        elif choice == '4':
             num1 = int(input("Enter the integer you want to factorize: "))
             answer = trial_division(num1)
             print(GREEN + f"Factors of integer '{num1}' is >>> {answer}" + RESET)
             dllist.add_node(Factors(num1, answer))
             if len(answer) == 1:
                 print(GREEN + f"'{num1}' is a PRIME " + RESET)
        elif choice == '5':
             num1 = int(input("Count primes upto: "))
             answer = pi(num1)
             print(RED + "Please note that this is an approximate value ! The real value may be different ! The bigger the input is, the better the approximation is !" + RESET)
             print(GREEN + f"There are approximately '{answer}' number of primes between 0 to {num1}" + RESET)
        elif choice == '6':
             print("Enter 'b' and 'm' so that  b(mod m)")
             num1 = int(input("Enter number for 'b': "))
             num2 = int(input("Enter number for 'm': "))
             answer = mod(num1, num2)
             print(GREEN + f"When {num1}(mod {num2}) >>> {answer}" + RESET)
        elif choice == '7':
             print(RED + "PROGRAM ENDED !" + RESET)
             break
        elif choice == '8':
            print(f"History >>> '{dllist.to_string()}'")
        elif choice == '9':
            dllist.clear()
            print(RED + "History cleared !" + RESET)

Euclidean_Alg()