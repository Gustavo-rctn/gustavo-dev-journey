# System Inputs
loan_amount = float(input('Enter desired loan amount ($): '))
monthly_income = float(input('Enter your monthly income ($): '))
installments = int(input('Enter number of monthly installments: '))

# Core Business Calculations
monthly_installment = loan_amount / installments
maximum_allowed_installment = monthly_income * 0.30

# Risk Assessment & Validation
if monthly_installment > maximum_allowed_installment:
    exceeded_amount = monthly_installment - maximum_allowed_installment
    print('\n[STATUS: LOAN DENIED]')
    print(f'Monthly installment: ${monthly_installment:.2f}')
    print(f'Maximum allowed limit (30% of income): ${maximum_allowed_installment:.2f}')
    print(f'The installment exceeds your credit limit by: ${exceeded_amount:.2f}')
else:
    print('\n[STATUS: LOAN APPROVED]')
    print(f'Monthly installment: ${monthly_installment:.2f}')
    print('The installment fits within your financial margin.')