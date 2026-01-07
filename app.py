def calculate_final_amount(bill, member):
    member = member.lower()
    discount = 0

    if member == "gold":
        discount = 0.20
    elif member == "silver":
        discount = 0.10 if bill > 1000 else 0.05
    elif member == "regular":
        discount = 0.05 if bill > 2000 else 0

    discounted_amount = bill - (bill * discount)
    gst = discounted_amount * 0.18
    final_amount = discounted_amount + gst

    return round(final_amount, 2)


# 👇 Only runs when executed directly, NOT during pytest import
if __name__ == "__main__":
    bill = float(input("Enter total cart value: "))
    member = input("Enter membership type (Gold/Silver/Regular): ")

    result = calculate_final_amount(bill, member)
    print("Final payable amount:", result)
