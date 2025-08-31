def revese(n):
    if isinstance(n,int):
        rev = 0
        while n>0:
            digit = n % 10
            rev = rev * 10 + digit
            n //=10
        return rev
    elif isinstance(n,str):
        if ' ' in n:
            words = n.split()
            words.reverse()
            return " ".join(words)
        else:    
            return n[::-1]
    
def simple_reverse(n):
    return n[::-1]


if __name__== "__main__":
    n = input("enter the number : ")
    m = revese(n)
    sim = simple_reverse(n)
    print(m)
    print(sim)