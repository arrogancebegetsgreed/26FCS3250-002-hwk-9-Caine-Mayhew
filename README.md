# Overview

The goal of this assignment is to have you write white-box unit tests. White-box is a type of test where the internal structure of the code is evaluated. 

# Instructions

Clear all of the test cases in **test_loan**. You can either write your tests using unittest or pytest. 

## Test Case #1

* pre-condition: a loan of an amount < Loan.MIN_LOAN_AMOUNT is instantiated 
* post-condition: an exception is raised

## Test Case #2

* pre-condition: a loan of an amount > Loan.MAX_LOAN_AMOUNT is instantiated 
* post-condition: an exception is raised
  
## Test Case #3

* pre-condition: a loan for a number of years < Loan.MIN_YEARS is instantiated 
* post-condition: an exception is raised
    
## Test Case #4

* pre-condition: a for a number of years > Loan.MAX_YEARS is instantiated 
* post-condition: an exception is raised
    
## Test Case #5

* pre-condition: a loan for an interest rate equal to Loan.MIN_INTEREST_RATE is instantiated 
* post-condition: an exception is raised
   
## Test Case #6

* pre-condition: a loan for an interest rate equal to Loan.MAX_INTEREST_RATE is instantiated 
* post-condition: an exception is raised
  
## Test Case #7

* pre-condition: a valid loan is intantiated
* post-condition: all of the internal values of the loan (loan_amount, years, interest_rate, monthly_payment, remaining_balance, and months_remaining) are correct

## Test Case #8

* pre-condition: a valid loan is intantiated; then an invalid payment (below the monthly payment) is attempted
* post-condition: an exception is raised

## Test Case #9

* pre-condition: a valid loan is intantiated; then an invalid payment (above the remaining balance) is attempted
* post-condition: an exception is raised

## Test Case #10

* pre-condition: a valid loan is intantiated; then a valid payment (equal to montly payment) is attempted
* post-condition: remaining_balance and months_remaining are correctly updated to reflect the payment

## Test Case #11

* pre-condition: a valid loan is intantiated; then a valid payment (equal to the remaining balance) is attempted
* post-condition: remaining_balance and months_remaining are correctly updated to reflect the payment
