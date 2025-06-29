import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from anagrafica import anagrafica_page

with st.sidebar:
    st.title("My app")

with open("./config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

st.session_state.authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

st.session_state.authenticator.login()

if st.session_state["authentication_status"]:
    with st.sidebar:
        # authenticator.logout()
        st.write(f"Welcome *{st.session_state['name']}*")

        # page = option_menu(
        #     menu_title="Menù",
        #     options=["Anagrafica", "Tessere", "Scontrini", "Prodotti"],
        #     icons=["people-fill", "card-text", "receipt", "tag-fill"],
        # )
        #
        # if page == "Anagrafica":
    anagrafica_page()

elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
