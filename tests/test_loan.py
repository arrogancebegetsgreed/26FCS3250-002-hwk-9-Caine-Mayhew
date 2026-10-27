'''
CS 3250 - Software Dev. Methods and Tools
Instructor: Thyago Mota
Student:
Description: Homework 09 - White-box (Unit) Testing
'''
import pytest
import loan


def test_case_1_invalid_loan_amount_below_min():
    # Test case 1: Invalid loan amount below minimum
    with pytest.raises(ValueError, match="Loan amount must be between 10000 and 1000000. Below minimum loan amount."):
        loan.Loan(5000, 10, 0.05)  # Loan amount below minimum

def test_case_2_invalid_loan_amount_above_max():
    # Test case 2: Invalid loan amount above maximum
    with pytest.raises(ValueError, match="Loan amount must be between 10000 and 1000000. Above maximum loan amount."):
        loan.Loan(2000000, 10, 0.05)  # Loan amount above maximum

def test_case_3_invalid_years_below_min():
    # Test case 3: Invalid number of years below minimum
    with pytest.raises(ValueError, match="Number of years must be between 1 and 30. Below minimum years."):
        loan.Loan(50000, 0, 0.05)  # Years below minimum

def test_case_4_invalid_years_above_max():
    # Test case 4: Invalid number of years above maximum
    with pytest.raises(ValueError, match="Number of years must be between 1 and 30. Above maximum years."):
        loan.Loan(50000, 40, 0.05)  # Years above maximum

def test_case_5_invalid_interest_rate_below_min():
    # Test case 5: Invalid interest rate below minimum
    with pytest.raises(ValueError, match="Interest rate must be greater than 0 and no more than 1. Below minimum interest rate."):
        loan.Loan(50000, 10, -0.01)  # Interest rate below minimum

def test_case_6_invalid_interest_rate_above_max():
    # Test case 6: Invalid interest rate above maximum
    with pytest.raises(ValueError, match="Interest rate must be greater than 0 and no more than 1. Above maximum interest rate."):
        loan.Loan(50000, 10, 1.5)  # Interest rate above maximum

def test_case_7_valid_loan():
    # Test case 7: Valid loan parameters
    loan_amount = 50000
    years = 10
    interest_rate = 0.05
    my_loan = loan.Loan(loan_amount, years, interest_rate)
    assert my_loan.loan_amount == loan_amount
    assert my_loan.years == years
    assert my_loan.interest_rate == interest_rate
    assert my_loan.monthly_payment == pytest.approx(530.33, abs=0.01)
    assert my_loan.remaining_balance == loan_amount
    assert my_loan.months_remaining == years * 12

def test_case_8_valid_loan_payment_below_monthly_payment():
    # Test case 8: Valid loan parameters but payment below monthly payment
    loan_amount = 50000
    years = 10
    interest_rate = 0.05
    my_loan = loan.Loan(loan_amount, years, interest_rate)
    with pytest.raises(ValueError, match="Payment amount must be at least the monthly payment."):
        my_loan.make_payment(my_loan.monthly_payment - 0.01)  # Payment below monthly payment

def test_case_9_valid_loan_payment_above_remaining_balance():
    # Test case 9: Valid loan parameters but payment above remaining balance
    loan_amount = 50000
    years = 10
    interest_rate = 0.05
    my_loan = loan.Loan(loan_amount, years, interest_rate)
    with pytest.raises(ValueError, match="Payment amount cannot exceed the remaining balance."):
        my_loan.make_payment(my_loan.remaining_balance + 0.01)  # Payment above remaining balance

def test_case_10_valid_loan_payment_equal_to_monthly_payment():
    # Test case 10: Valid loan parameters and payment equal to monthly payment
    loan_amount = 50000
    years = 10
    interest_rate = 0.05
    my_loan = loan.Loan(loan_amount, years, interest_rate)
    pmt = my_loan.monthly_payment
    my_loan.make_payment(pmt)  # Payment equal to monthly payment
    assert my_loan.remaining_balance == pytest.approx(loan_amount - pmt, abs=0.01)  # Remaining balance should decrease
    assert my_loan.months_remaining == (years * 12) - 1  # Months remaining should decrease by 1

def test_case_11_valid_loan_payment_equal_to_remaining_balance():
    # Test case 11: Valid loan parameters and payment equal to remaining balance
    loan_amount = 50000
    years = 10
    interest_rate = 0.05
    my_loan = loan.Loan(loan_amount, years, interest_rate)
    my_loan.make_payment(my_loan.remaining_balance)  # Payment equal to remaining balance
    assert my_loan.remaining_balance == 0  # Remaining balance should be zero
    assert my_loan.months_remaining == 0  # Months remaining should be zero