import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open("./config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

# authenticator = st.session_state.authenticator
if not st.session_state.get("authenticator"):
    st.session_state.authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )


st.session_state.authenticator.login(location="unrendered")


login_page = st.Page(
    "pages/login.py", title="Annexx", icon=":material/home:", url_path="login"
)

pages = {
    "Your account": [
        st.Page("pages/create_account.py", title="Create your account", default=True),
        st.Page("pages/manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("pages/learn.py", title="Learn about us"),
        st.Page("pages/trial.py", title="Try it out"),
    ],
}

print("streamlit_app.py:\n", st.session_state)
print("\n----------------------\n")
pg = st.navigation(
    pages
    if (st.session_state.get("authentication_status"))
    else {"login": [login_page]}
)
pg.run()
