import streamlit as st
import os


def render():
    placeholder = st.empty()
    with placeholder.form("Register"):
        st.markdown("### Complete the form below to create account")
        full_name = st.text_input("Full name")
        username = st.text_input("Username")
        email = st.text_input("Email address")
        password = st.text_input("Password", type="password")
        comfirm_password = st.text_input("comfirm password", type="password")
        submit = st.form_submit_button("Register", help="Create account")

        if submit:
            register_user(full_name, username, email, password, comfirm_password)

    if st.button("Back to Login"):
        st.experimental_set_query_params(page="login", cache_clear=True)
    html_temp = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    <div style="background-color:#E9FFBC;padding:10px; font-family:'Times New Roman'; text-align:center; margin-top: 2rem;">
    <h7 style="color:black;text-align:center;">Automated Medical Image Classification Using Deep Learning</h7>
    </div> """
    st.markdown(html_temp, unsafe_allow_html=True)


def black_field():
    st.error("All input fields are required")


def password_match():
    st.error("Password does not match")


def user_exist(username):
    st.error(username + " already exist")
    return


def successful_reg():
    st.success("Registration successfully")
    st.experimental_set_query_params(page="login")


def register_user(full_name, username, email, password, comfirm_password):
    if (
        not full_name
        or not username
        or not email
        or not password
        or not comfirm_password
    ):
        black_field()
        return
    if not password == comfirm_password:
        password_match()
        return

    # check if this username already exist
    list_of_files = os.listdir()

    # Defining verification's condition
    if username in list_of_files:
        user_exist(username)
        return

    # Open file in write mode
    file = open("/users_files/username.txt", "w")

    # Write username and password information
    file.write(full_name + "\n")
    file.write(username + "\n")
    file.write(email + "\n")
    file.write(password)
    file.close()

    successful_reg()


footer = """
<style>
a:link , a:visited{
    color: white;
    background-color: transparent;
    text-decoration: None;
}

a:hover,  a:active {
    color: red;
    background-color: transparent;
    text-decoration: None;
}

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: transparent;
    color: black;
    text-align: center;
}
</style>
"""
st.markdown(footer, unsafe_allow_html=True)
