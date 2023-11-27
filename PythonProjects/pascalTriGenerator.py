from math import factorial


# WARNING: After around row 15, the triangle gets wonky due to the large numbers generated in the triangle
n = int(input('Enter until what row you want to generate the triangle: '))

for i in range(n):
    for j in range(n-i+1):
        # for left spacing
        print(end=' ')
    
    for j in range(i+1):
        # This uses the nCr or Combination formula
        #nCr = n! / r!(n - r)!
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=' ')

    # for new line
    print()
