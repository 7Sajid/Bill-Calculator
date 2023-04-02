print("***Welcome to The Bill Separation Calculator***")
bill = float(input("What Is Your Total Bill Amount in BDT :- "))
tip = int (input("How Much Tip do You Want to Give in BDT (5%,10%,12% or 15%) :- "))
People = int (input("How many People to split the Bill ? :- "))
bill_as_percent = tip /100 
total_tip_amount = bill * bill_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / People
final_amount = round(bill_per_person, 2)
print(f"Each Person Should Pay Total amount {final_amount} Taka")