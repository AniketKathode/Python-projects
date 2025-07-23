def larger(arr, n):
    max = arr[0]
    for i in range(n):
        if max > arr[i]:
            max= arr[i]
    return max

def Evenodd(res):
    if res%2==0:
        print("The larger in the array is even : ",res)
    else:
        print("the larger number in the array is odd : ",res)
    
        
def oddeven(arr):
    counteven =0
    countodd =0
    for num in arr:
        if num%2==0:
            counteven+=1
        else:
            countodd+=1
    return countodd, counteven
        
    

if __name__=="__main__":
    arr=[1020,65,46,45,43]
    n=len(arr)
    res= larger(arr,n)
    a=Evenodd(res)
    print(res)
    b= oddeven(arr)
    print(b)