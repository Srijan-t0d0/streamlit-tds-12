import streamlit as st

st.header("Find the largest number")

n1 = st.number_input("Input your 1st number", placeholder="First number", value=None)
n2 = st.number_input("Input your 2nd number", placeholder="Second number", value=None)
n3 = st.number_input("Input your 3rd number", placeholder="Third number", value=None)


try:
    n_max = max([n1, n2, n3])
    st.divider()
    st.write(
        f"Largest number is {n_max:.2f}",
    )
except:
    st.divider()
    st.write(
        f"Please input the numbers",
    )
