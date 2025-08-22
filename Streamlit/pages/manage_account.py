import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open("./config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

authenticator = st.session_state.authenticator
# authenticator = stauth.Authenticate(
#     config["credentials"],
#     config["cookie"]["name"],
#     config["cookie"]["key"],
#     config["cookie"]["expiry_days"],
# )

try:
    authenticator.login(location="unrendered")
except Exception as e:
    st.error(e)


st.title("Manage your account")
