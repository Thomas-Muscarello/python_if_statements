#Comparing Numbers
def max_num(x,y,z):
    #Use a comparison operator to print the largest number.
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

print(max_num(5,4,3))