import streamlit as st

st.title("GIẢI PHUƯƠNG TRÌNH BẬC NHẤT")
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')

if st.button('Giải'):
    if (a == 0 and b != 0):
        st.error("Phương trình vô nghiệm")
    else:
        res = -b/a
        st.success(f'Phương trình có nghiệm {res}')