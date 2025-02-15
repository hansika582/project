import streamlit as st

# Function to calculate the remaining budget
def calculate_budget(income, expenses):
    total_expenses = sum(expenses)
    remaining_budget = income - total_expenses
    return total_expenses, remaining_budget

# Streamlit application
st.title("Simple Budget Calculator")

st.write("Enter your monthly income and expenses below:")

# User input for monthly income
income = st.number_input("Monthly Income", min_value=0.0, step=100.0)

# User input for expenses
rent = st.number_input("Rent/Mortgage", min_value=0.0, step=50.0)
utilities = st.number_input("Utilities (Electricity, Water, etc.)", min_value=0.0, step=10.0)
groceries = st.number_input("Groceries", min_value=0.0, step=10.0)
transportation = st.number_input("Transportation", min_value=0.0, step=10.0)
other_expenses = st.number_input("Other Expenses", min_value=0.0, step=10.0)

# List of all expenses
expenses = [rent, utilities, groceries, transportation, other_expenses]

# Calculate total expenses and remaining budget when the user inputs data
if income > 0:
    total_expenses, remaining_budget = calculate_budget(income, expenses)

    # Display results
    st.write(f"**Total Expenses**: ${total_expenses:.2f}")
    st.write(f"**Remaining Budget**: ${remaining_budget:.2f}")

    if remaining_budget < 0:
        st.error(f"Warning: You have overspent by ${abs(remaining_budget):.2f}")
    else:
        st.success(f"You are within budget! Remaining budget: ${remaining_budget:.2f}")
else:
    st.warning("Please enter your income to calculate your budget.")
