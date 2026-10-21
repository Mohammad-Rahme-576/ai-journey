bill = float(input("Enter the bill amount: "))
tip_perc = float(input(("Enter the tip percentage: ")))
people = int(input("Enter the number of people: "))

tip = bill * tip_perc / 100
total = bill + tip
per_person = total / people

print(f"Tip amount: ${tip:.2f}")
print(f"Total amount: ${total:.2f}")
print(f"Amount per person: ${per_person:.2f}")