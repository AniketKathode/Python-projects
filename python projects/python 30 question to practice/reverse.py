# for login purpose



# def reverse(n):
#     rev=0
#     while n>0:
#         digit=n%10
#         rev= rev*10+digit
#         n //=10
#     return rev
# if __name__=="__main__":
#     ans= reverse(12345654)
#     print(ans)



# for digit opr simplr use    
def reverse(n):
    return n[::-1]
a= reverse(str(512))
print(a)