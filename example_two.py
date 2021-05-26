is_male= False
is_tall= True

#Using the OR statement
if is_male or is_tall:
    #If is_male is true or is_tall is true print the following
    print("You are a male or you are tall, or both!")
else:
    #If both is_male and is_tall are false, print the following:
    print("You are neither a male or tall!")

#Using the AND statement
if is_male and is_tall:
    #If is_male is true or is_tall is true print the following
    print("You are a male and you are tall")
else:
    #If both is_male and is_tall are false, print the following:
    print("You are either not a male or are not tall, or neither!")
