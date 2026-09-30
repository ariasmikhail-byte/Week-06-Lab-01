# Mikhail Arias
# CMP 131
# Week 6
# Lab 1
# Software Discounter
# 9/30/2026

print("======== Discounter ========")
units_purchased = int(input("Units Purchased"))
if units_purchased <= 0:
    print("Error Can't Calculate!")
else:
    print("Continue On")
print("------- Original Cost -------")
Original_cost = units_purchased * 99.00
print(f"${Original_cost:.2f}")
# Getting the Discount
if units_purchased < 10:
    discount_rate = 0.00
elif units_purchased <= 19:
    discount_rate = 0.20
elif units_purchased <= 49:
    discount_rate = 0.30
elif units_purchased <= 99:
    discount_rate = 0.40
else:
    discount_rate = 0.50
print("---- Discount Amount ----")
Discount_amount = Original_cost * discount_rate
print(f"${Discount_amount:.2f}")

# Getting final price 
Final_Price = Original_cost - Discount_amount
print("------ Final Price -------")
print(f"${Final_Price:.2f}")

print("====== Purchase Report ======") 
print(f"Number of Units Purchased: {units_purchased}")
print(f"Price Per Unit: $99.00")
print(f"Discount Percentage: ")