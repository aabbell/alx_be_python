monthly_income =  int(input("Enter your monthly income:"))
monthly_expenses =  int(input("Enter your total monthly expenses:")) 
monthly_savings =  monthly_income - monthly_expenses
interset = savings * 12 * 0.05
ProjectedSavings = monthly_savings * 12 + interset

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${int(ProjectedSavings)}.")