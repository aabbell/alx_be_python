monthlyIncome =  int(input("Enter your monthly income:"))
monthlyExpenses =  int(input("Enter your total monthly expenses:")) 
monthlySavings =  monthlyIncome - monthlyExpenses
interset = savings * 12 * 0.05
ProjectedSavings = monthlySavings * 12 + interset

print(f"Your monthly savings are ${monthlySavings}.")
print(f"Projected savings after one year, with interest, is: ${int(ProjectedSavings)}.")