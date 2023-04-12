# #   TAKING INPUt FROM THE USER 
# x=int(input("enter the number of years: "))
# for i in range(x):
#     total_rainfall=0       #  INITIALISING THE RAINFALL AMOUNT
#     for j in range(12):     # NESTED LOOPING TO ASK FOR THE RAINFALL IN 12 MONTHS AND ITERATING THEM 
#         j=0
#         rain=int(input("enetr the rainfall amount for the month :",j+1 ))
#         # rain+=1
#         j=j+1
#     total_rainfall=total_rainfall+rain   # will kepp on adding the new data per month entered
#     print("the total rainfall is: ",total_rainfall)
#     print("the average is: ",total_rainfall/12)
#     i=i+1
    
    

x=int(input("enter the number of years "))
years=0

while(x<=years):
  i=0
  j=0
  total=0
  while (i<12):
    print("month ",i+1)
    j=int(input("enter the rainfall per month "))
    total=total+j
    i+=1
  print("total: ",total,"")
  print("average :",total/12)
  years=years+1 
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
