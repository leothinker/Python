import streamlit as st
import streamlit_authenticator as stauth
import yaml
from streamlit_authenticator.utilities import LoginError
from yaml.loader import SafeLoader

st.set_page_config(page_title="Home")
st.title("Streamlit-Authenticator")
st.write("""
A basic implementation of a Multi-Page App using Streamlit and Streamlit-Authenticator.  You can learn more about it at: [https://github.com/mkhorasani/Streamlit-Authenticator](https://github.com/mkhorasani/Streamlit-Authenticator).
         
Log in with the following credentials:
""")

st.code("Username: brian\nPassword: password")

# Load credentials from the YAML file
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize the authenticator
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

# Store the authenticator object in the session state
st.session_state["authenticator"] = authenticator
# Store the config in the session state so it can be updated later
st.session_state["config"] = config

# Authentication logic
try:
    authenticator.login(location="main", key="login-demo-app-home")
except LoginError as e:
    st.error(e)


if st.session_state["authentication_status"]:
    authenticator.logout(location="sidebar", key="logout-demo-app-home")
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")


# Check for Admin Access
try:
    user_roles = st.session_state.get("roles", []) or []

    if "admin" in user_roles:
        st.subheader("Admin Tools")

        # Download button for updated config.yaml
        def download_config():
            config_data = yaml.dump(st.session_state["config"])
            st.download_button(
                label="Download Updated Config",
                data=config_data,
                file_name="config.yaml",
                mime="text/yaml",
            )

        download_config()

        # Session State for Debugging
        with st.expander("Session State for Debugging", icon="💾"):
            st.session_state

except Exception as e:
    st.error(f"An error occurred: {e}")
