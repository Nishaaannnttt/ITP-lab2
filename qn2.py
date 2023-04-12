#    TAKING INPUTS 
x=int(input("enter the starting number of organsims: "))
y=int(input("enter the average percentage increase: "))
z=int(input("enter how many days of data should be inserted: "))

#   GIVING A CONDITION TOI ONLY EXECUTE WHEN PROVIDED POSITIVE VALUES 
if (x>0 and y>0 and z>0):
    i=1        # SINCE WE HAVE TO START AT DAY 1
    while(i<=z):
        print("day",i,":",x)        #   PRINTED AHEAD OF CALCULATION TO GET DAY 1 AS THE INPUTED AMOUNT 
        x=(x+(y/100)*x)              
        i=i+1            #  ITERATES UNTL IT MEETS THE Z DATA 
else:
    print("please enter the valid positive values")      # EXECUTES THIS WHEN NEAGTIVE VALUES ARE GIVEN 
    









