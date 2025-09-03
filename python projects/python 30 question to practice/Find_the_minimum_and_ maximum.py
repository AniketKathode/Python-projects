def minimum(n):
    minimum = n[0]
    for i in n:
        if i < minimum:
            minimum = i
    return minimum
    
def ismax(n):
    maximum = n[0]
    for i in n:
        if i > maximum:
            maximum = i
    return maximum

def sum(a,b):
    return a+b
    


if __name__ == "__main__":
    n = [1,-4,12,-25,50]
    a = minimum(n)
    b = ismax(n)
    c = sum(a,b)
    print("The minimum number in the array is : ",a)
    print("The maximum number in the array is : ",b)
    print("The maximum number in the array is : ",c)

