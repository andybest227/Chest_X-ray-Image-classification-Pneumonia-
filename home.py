import streamlit as st
from PIL import Image
from login import render as render_login
from register import render as render_register

from dashboard import main as render_dashboard


def main():
    st.title("Medical Image Classification System")
    # image = Image.open(
    #     "C:/Users/user/PycharmProjects/RiceLeafDisease/images/banner.jpg"
    # )
    # st.image(image)
    # Get the current page from the URL query parameter
    page = st.experimental_get_query_params().get("page", ["login"])[0]

    # Render the appropriate page based on the current query parameter
    if page == "login":
        render_login()
    elif page == "register":
        render_register()
    elif page == "dashboard":
        render_dashboard()


if __name__ == "__main__":
    main()
