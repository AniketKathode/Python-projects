def largest(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max= arr[i]
    return max

if __name__=='__main__':
    n=int(input("Enter the number of element you want to put in array : "))
    arr=[]
    for i in range(n):
        num=int(input(f"Enter the {i+1} : "))
        arr.append(num)
    ans = largest(arr,n)
    print(ans)