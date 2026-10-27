'''
CS 3250 - Software Dev. Methods and Tools
Instructor: Thyago Mota
Student:
Description: Homework 09 - White-box (Unit) Testing
'''
 
class Loan: 
    '''
    A class to model a loan with the ability to compute monthly payments, make payments, and query the loan status. 
    '''

    MIN_LOAN_AMOUNT   = 10000
    MAX_LOAN_AMOUNT   = 1000000
    MIN_YEARS         = 1
    MAX_YEARS         = 30
    MIN_INTEREST_RATE = 0
    MAX_INTEREST_RATE = 1

    '''
    A loan is defined by its amount [MIN_LOAN_AMOUNT, MAX_LOAN_AMOUNT], number of years [MIN_YEARS, MAX_YEARS], and interest rate (MIN_INTEREST_RATE, MAX_INTEREST_RATE). A loan also controls its monthly payment, remaining balance, and months of payment remaining.  
    '''
    def __init__(self, loan_amount, years, interest_rate):
        if loan_amount < Loan.MIN_LOAN_AMOUNT or loan_amount > Loan.MAX_LOAN_AMOUNT: 
            raise ValueError(f'Loan amount must be between {Loan.MIN_LOAN_AMOUNT} and {Loan.MAX_LOAN_AMOUNT} dollars.')
        if years < Loan.MIN_YEARS or years > Loan.MAX_YEARS: 
            raise ValueError(f'Number of years must be between {Loan.MIN_YEARS} and {Loan.MAX_YEARS}.')
        if interest_rate <= Loan.MIN_INTEREST_RATE or interest_rate >= Loan.MAX_INTEREST_RATE:
            raise ValueError(f'Interest rate must be greater than {Loan.MIN_INTEREST_RATE} and no more than {Loan.MAX_INTEREST_RATE}.')
        self.__loan_amount = loan_amount
        self.__years = years
        self.__interest_rate = interest_rate
        self.__monthly_payment = self.__calculate_monthly_payment()
        self.__remaining_balance = loan_amount
        self.__months_remaining = self.__years * 12

    '''
    Helper method to compute the monthly payment of the loan. 
    '''
    def __calculate_monthly_payment(self):
        monthly_interest_rate = self.__interest_rate / 12
        num_payments = self.__years * 12
        monthly_payment = (self.__loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
        return monthly_payment
    
    '''
    Accessor method to return the loan amount. 
    '''
    @property
    def loan_amount(self): 
        return self.__loan_amount
    
    '''
    Accessor method to return the number of years of the loan. 
    '''
    @property
    def years(self): 
        return self.__years
    
    '''
    Accessor method to return the interest rate of the loan. 
    '''
    @property
    def interest_rate(self): 
        return self.__interest_rate
    
    '''
    Accessor method to return the monthly payment. 
    '''
    @property
    def monthly_payment(self): 
        return self.__monthly_payment
    
    '''
    Accessor method to return the number of months remaining 
    '''
    @property
    def months_remaining(self): 
        return self.__months_remaining
    
    '''
    Accessor method to return the remaining balance.
    '''
    @property
    def remaining_balance(self): 
        return self.__remaining_balance
    
    '''
    Processes a payment towards the loan. The amount must be at least the monthly payment and cannot exceed the remaining balance. If the remaining balance is zeroed after the payment, months_remaining should be zeroed as well. 
    '''
    def make_payment(self, amount):
        if amount < self.__monthly_payment:
            raise ValueError('Payment amount must be at least the monthly payment.')
        if amount > self.__remaining_balance: 
            raise ValueError('Payment amount cannot exceed the reamining balance.')
        self.__remaining_balance -= amount
        self.__months_remaining -= 1
        if abs(self.__remaining_balance) < 0.001: 
            self.__months_remaining = 0

# just a driver "test"
if __name__ == '__main__':
    loan = Loan(600000, 30, 0.025)
    print(f'Monthly Payment: {loan.monthly_payment}')
    print(f'Loan amount: {loan.loan_amount}')
    print(f'Years: {loan.years}')
    print(f'Interest rate: {loan.interest_rate}')
    print(f'Months remaining: {loan.months_remaining}')
    print(f'Remaining balance: {loan.remaining_balance}')
