
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def isreverse(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    

    if rev%2==0:
        print("the reverse nuber is even")
    else:
        print("the number is not reverse number")
    return rev

def fab(n):
    if n<0:
        return False
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fab(n-1) + fab(n-2)




if __name__ == "__main__":
    n = int(input("Enter the number : "))
    if isprime(n):
        print("The number is prime")
    else:
        print("The number is not prime")
        
    a = isreverse(n)
    print("Reversed number:", a)

    start = int(input("Enter the start number : "))
    end = int(input("Enter the end of series : "))
    count=0
    for n in range(start,end+1):
        if isprime(n):
            print(n, end=' ')
            count +=1
    print(f"\nThe count of prime number : ", count)
    
    b= fab(n)
    print(b)