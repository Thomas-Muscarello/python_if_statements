is_male= False
is_tall= False

#Using else if (aka: ELIF)
if is_male and is_tall:
    #If is_male is true and is_tall is true print the following
    print("You are a male and you are tall!")
elif is_male and not(is_tall):
    #If is_male is true but is_tall is false, print the following:
    print("You are a male, but not tall!")
elif is_tall and not(is_male):
    #If is_male is false but is_tall is true, print the folowing:
    print("You are tall but not a male!")
else:
    #If both are false, print the following:
    print("You are neither a male, nor tall.")



