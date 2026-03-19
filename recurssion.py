# 1.Print 1 to N using Recursion
# def printname(n):
#     if n>0:
#         print('jaya')
#         printname(n-1)
# printname(3)

# 2.Print N to 1 using Recursion
# def printnto1(n):
#     if n>0:
#         print(n)
#         printnto1(n-1)
# printnto1(10)

# 3.Sum of first N Natural Numbers
def sumofnnaturalnums(n):
    if n>0:
        if n==1:
            return 1
        else:
            return n+sumofnnaturalnums(n-1)
print(sumofnnaturalnums(7))

        

    
