import streamlit as st
import os

base_dir = os.path.dirname(__file__)

st.set_page_config(page_title="Medical Image Classification System", layout="centered")


# from dashboard import dashboard
def render():
    placeholder = st.empty()
    with placeholder.form("Login"):
        st.markdown("### Enter your login Credentials")
        email = st.text_input("Enter Username")
        password = st.text_input("Enter Password", type="password")
        submit = st.form_submit_button("Login")
        if submit:
            login_user(email, password)
    if st.button("Create account"):
        navigate()

    html_temp = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    <div style="background-color:#E9FFBC;padding:10px; font-family:'Times New Roman'; text-align:center; margin-top: 2rem;">
    <h7 style="color:black;text-align:center;">Automated Medical Image Classification Using Deep Learning</h7><br>
    </div> """
    st.markdown(html_temp, unsafe_allow_html=True)


def black_field():
    st.error("All input fields are required")


def navigate():
    st.experimental_set_query_params(page="register")


def invalid_details():
    st.error("Invalid login details")


def login_user(username, password):
    if not username or not password:
        black_field()
        return
    else:
        # The method listdir() returns a list containing the names of the entries in the directory given by path
        # check if this username already exist
        folder = os.path.join(base_dir, "users_files")
        list_of_files = os.listdir(folder)

    # Defining verification's condition
    if username + ".txt" in list_of_files:
        with open(folder + "/" + username + ".txt", "r") as file:
            file_contains_password = any(password in line for line in file)

        if file_contains_password:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()


def login_success():
    st.experimental_set_query_params(page="dashboard", cache_clear=True)


def password_not_recognised():
    st.error("Invalid password")


def user_not_found():
    st.error("User not found")


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
# st.image("C:/Users/user/PycharmProjects/RiceLeafDisease/images/img_logo.jpg")
