import streamlit as st

# import streamlit_authenticator as stauth
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

print("login.py 1:\n", st.session_state)
print("\n----------------------\n")

try:
    authenticator.login()
except Exception as e:
    print("login.py error:\n", st.session_state.get("authentication_status"))
    st.error(e)

print("login.py 2:\n", st.session_state)
print("\n----------------------\n")


if st.session_state.get("authentication_status"):
    authenticator.logout()
    st.write(f"Welcome *{st.session_state.get('name')}*")
    st.title("Some content")
elif st.session_state.get("authentication_status") is False:
    st.error("Username/password is incorrect")
elif st.session_state.get("authentication_status") is None:
    st.warning("Please enter your username and password")
