initial_bal=float(input("Enter the initial balance in your bank account: "))
deposit=float(input("Enter the amount to be deposited: "))

print(f"Initial Balance: {initial_bal:.2f}")
new_bal=initial_bal+deposit
print(f"New Balance after deposit of {deposit:.2f}: {new_bal:.2f}")


withdrawal=float(input("Enter the amount to be withdrawn: "))
if withdrawal>new_bal:
    print("Insufficient funds for this withdrawal.")   
else:
    new_bal-=withdrawal
    print(f"New Balance after withdrawal of {withdrawal:.2f}: {new_bal:.2f}")

