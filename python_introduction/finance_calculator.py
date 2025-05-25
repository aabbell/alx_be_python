income =  int(input("Enter your monthly income:"))
expenses =  int(input("Enter your total monthly expenses:")) 
savings =  income - expenses
interset = savings * 12 * 0.05
ProjectedSavings = savings * 12 + interset

print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${int(ProjectedSavings)}.")