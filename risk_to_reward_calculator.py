import streamlit as st

# Initialize Streamlit dashboard
st.title("Risk to Reward Calculator")

# Step 1: Inputs for investment, RoR, and risk percentage
investment = st.number_input("Enter your investment amount (e.g., 100 USDT):", min_value=0.0, value=100.0)
ror = st.number_input("Enter the Risk to Reward ratio (e.g., 2):", min_value=0.0, value=2.0)
risk_percentage = st.number_input("Enter your risk percentage (e.g., 3%):", min_value=0.0, max_value=100.0, value=3.0)

# Step 2: Days of the month input
st.subheader("Trade Results for Each Day")
days = [f"Day {i+1}" for i in range(30)]
results = {}

for day in days:
    results[day] = st.selectbox(f"{day} (Win or Lose):", ["-", "Win", "Lose"], index=0)

# Step 3: Calculate cumulative profit/loss dynamically
cumulative_balance = investment
win_count, loss_count = 0, 0

# Store daily balances for display
daily_balances = []

for day, result in results.items():
    if result == "Win":
        # Reward based on updated balance
        reward_amount = (ror * (risk_percentage / 100) * cumulative_balance)
        cumulative_balance += reward_amount
        win_count += 1
    elif result == "Lose":
        # Risk based on updated balance
        risk_amount = (risk_percentage / 100) * cumulative_balance
        cumulative_balance -= risk_amount
        loss_count += 1
    
    # Store daily balance
    daily_balances.append(cumulative_balance)

# Display daily balances
st.subheader("Daily Balances")
for i, balance in enumerate(daily_balances, 1):
    st.write(f"Day {i}: {balance:.2f} USDT")

# Step 4: Display final results
st.subheader("Summary")
st.write(f"Total Wins: {win_count}")
st.write(f"Total Losses: {loss_count}")
st.write(f"Final Balance: {cumulative_balance:.2f} USDT")

# Step 5: Insights for win rate
if win_count + loss_count > 0:
    win_rate = (win_count / (win_count + loss_count)) * 100
    st.write(f"Win Rate: {win_rate:.2f}%")

st.markdown("""
### Insights
Try moving your losses or wins to different days to analyze how the sequence impacts your final balance!
""")
