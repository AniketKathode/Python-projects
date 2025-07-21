def EvenOdd(arr):
    counteven=0
    countodd=0
    for num in arr:
        if num%2==0:
            counteven+=1
        else:
            countodd+=1
    return countodd, counteven
# if __name__=="__main__":
#     arr=[10,20,2,3,5,7,8]
#     ans= EvenOdd(arr)
#     print(ans)
    
if __name__=="__main__":
    n= int(input("Enter the element you want to add in the arr : "))
    arr=[]
    for i in range(n):
        ele=int(input(f"Enter the element in array : "))
        arr.append(ele)
    ans= EvenOdd(arr)
    print(ans)