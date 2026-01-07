import sys

# Read arguments
total_cart_value = float(sys.argv[1])
membership = sys.argv[2].lower()
extra = float(sys.argv[3])  # if needed

discount = 0

if membership == "gold":
    discount = 0.20
elif membership == "silver":
    discount = 0.10 if total_cart_value > 1000 else 0.05
elif membership == "regular":
    discount = 0.05 if total_cart_value > 2000 else 0

final_amount = total_cart_value - (total_cart_value * discount)
tax = final_amount * 0.18
final_bill = final_amount + tax

print(f"Final Bill Amount: {final_bill}")