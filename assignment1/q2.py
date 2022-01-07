#all values are in $
gross_income=int(input("enter gross income:")) #gross income must be entered to the nearest penny
no_of_dependents=int(input("enter no. of dependents:"))
standard_deduction=10000
dependent_deduction=3000

taxable_income=gross_income-standard_deduction-(dependent_deduction*no_of_dependents)
tax=taxable_income*0.2
print("your income tax is",tax)
                   
