# This one is like your scirpt in argv 

def print_two(*args) :
    arg1 , arg2 = args
    print(f"arg1 : {arg1} , arg2 : {arg2}")

# OK! that *args is actually pointless, we can just do this 
def print_two_again(arg1 , arg2) :
    print(f"arg1 : {arg1} , arg2 : {arg2}")

# This just print one argument 
def print_one(arg1) :    
    print(f"arg1 : {arg1}")

#This one takes no argument
def print_none() :
    print("I got nothin' .")

#Printing out all the function's taken arguments
print_two("MO", "Boustt")
print_two_again("mo", "boustt")
print_one("moboustt")
print_none()        
