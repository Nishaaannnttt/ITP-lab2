   
x=int(input("enter the number of years "))       # taking the input ffrom user 
years=0            #   initializing  the value  
i=0
total=0
while(years<=x):       # giving condition to run code in loop
  while (i<12):          # a nested loop to ask for month rainfall
    print("month ",i+1)
    j=int(input("enter the rainfall per month "))
    i+=1
    # j+=1
    total=total+j           # adds the value with entered amount 
  print("total: ",total)
  print("average monthly rainfall:",total/12,"inches")
  years=years+1

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
