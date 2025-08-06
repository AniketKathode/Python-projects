# def isprime(n):
#     if n<= 1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# if __name__=="__main__":
#     n=int(input("Enter the number : "))
#     if isprime(n):
#         print(f"Enter number {n} is prime")
#     else:
#         print(f"The nuber is not prime")





def prime(n):
    if n <=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

if __name__=="__main__":
    star=int(input("ENter the star number : "))
    end=int(input("ENter the star number : "))
    count=0
    for n in range(star,end+1):
        if prime(n):
            print(n, end=' ')
            count +=1
    print("\n total {count}", count)