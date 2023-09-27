# Asking user to input the price of the package and the distance.

package_price = float(input("\nPlease enter the price of the package:")) 

distance = float(input("Please enter the distance in Kms:"))  


# Declaring the variables and ask user to input their choice

air = 0.36

freight = 0.25

delivery_choice = input("Enter 'a' for air or 'f' for freight :")

full_insurance = 50

lim_insurance = 25

insurance_choice = input("Enter 'f' for full insurance or 'l' for limited:")

gift = 15

no_gift = 0

gift_option= input("Enter 'g' for gift or 'n' for no gift:")

priority_del = 100

stand_del = 20

delivery_speed = input("Enter 'p' for priority or 's' for standard delivery :")

# Calculate the final cost

if delivery_choice == "a":
   delivery_cost = (distance * air)
   
elif delivery_choice =="f":
    delivery_cost = (distance * freight)
    
elif insurance_choice == "f":
    fee_cost = full_insurance

elif insurance_choice == "l":
    fee_cost = lim_insurance

elif gift_option == "g":
    fee_cost = gift

elif gift_option == "n":
    fee_cost = no_gift

elif delivery_speed == "p":
    fee_cost = priority_del

elif delivery_speed == "s":
    fee_cost = stand_del
    
final_cost = delivery_choice + fee_cost
print(final_cost)