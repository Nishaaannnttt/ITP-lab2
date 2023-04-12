my_numbers=[1,2,3,4,5,6,7,8,9,10]     #   DECLARING AND INITIALIZING THE LIST
new_list=[]                     # new list to store the elements 
print(my_numbers)               # just to print the list at first 
for i in my_numbers:
    print(i)                   # to print the elemets of the lsit 
    
    
    if i>5:                        # GIVNG CONDITIONS 
        new_list.append(i)          # ADDING THE NUMBERS THAT ARE GREATER THAN 5 
print(new_list)

      # --------ANOTHER    WAY -----------

# new_list=[i for i in my_numbers if i>5]       # new condition to print the new list form existing elements
# print(new_list)                         





                   