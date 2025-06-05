
import streamlit as st

st.title("KWG Big/Small Prediction Tool")

st.markdown("Enter the last 9 numbers from recent periods (0–9):")

numbers = []
for i in range(9):
    num = st.number_input(f"Period {i}", min_value=0, max_value=9, step=1, key=f"num{i}")
    numbers.append(num)

if st.button("Predict Result"):
    N = len(numbers)
    big_nums = [n for n in numbers if n >= 5]
    small_nums = [n for n in numbers if n < 5]

    big_count = len(big_nums)
    small_count = len(small_nums)

    # Count repeating Big numbers
    repeating_big = len([n for n in set(big_nums) if big_nums.count(n) > 1])

    P_big = (big_count / N) + (repeating_big / N)
    P_small = small_count / N

    st.write(f"**Probability Big**: {P_big:.2f}")
    st.write(f"**Probability Small**: {P_small:.2f}")

    if P_big > P_small:
        st.success("🔮 Prediction: **BIG**")
    elif P_small > P_big:
        st.success("🔮 Prediction: **SMALL**")
    else:
        st.warning("🤷‍♂️ Equal probability for Big and Small.")
