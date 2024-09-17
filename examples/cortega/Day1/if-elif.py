# if, else, elif
# basic syntax 
# statement variable expresion value
import time
print("\nAssing values to false")

condition = True
if condition ==  True:
    print(f"condition is met because variable condition {condition} equals to  True")


print("\nReassing values to false")
condition = False
if condition == True:
    print(f"contition is true: {condition}")
else:
    print(f"Exeucution else because condition is actually false: {condition}")
    
 
condition = 32
print("\n Reassing values to integer 32")
if condition > 100:
    print(f"contition is : {condition}")
elif condition < 100:
    print(f"elif condition is met bacase condition is less than a 100 : {condition}")    
