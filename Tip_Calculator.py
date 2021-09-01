print("welcome to tip calculator")
total_bill = int(input("what is total bill? "))
split = int(input("How many people to split bill? "))
tip = int(input("what percentage tip you want to give? 10, 20, 30, 40, 50, or specify yourself "))

final_bill = total_bill + tip/100 * total_bill

payable_amount = final_bill / split


print(f"Total bill including tip {final_bill}")
print(f"Each person should pay {payable_amount}")


