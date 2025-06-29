import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


def anagrafica_page():
    with open("./config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    # st.session_state.authenticator = stauth.Authenticate(
    #     config["credentials"],
    #     config["cookie"]["name"],
    #     config["cookie"]["key"],
    #     config["cookie"]["expiry_days"],
    #     # config["pre-authorized"],
    #     # key="anagrafica-auth"
    # )
    st.write("everthing is working")

    st.session_state.authenticator.login()

    st.title("Anagrafica")
