import streamlit as st
import yaml

st.set_page_config(page_title="Page 1")
st.title("Page 1")
st.write(f"Hello {st.session_state.get('name')}, welcome to Page 1!")
st.write("""
On the second page, we're going to first check to see if the user is authenticated by looking at session state.  if it's not, then render a button to go back home.  If the user is authenticated, display the page content.
""")

if st.session_state.get("authentication_status"):
    authenticator = st.session_state.get("authenticator")
    authenticator.logout(location="sidebar", key="logout-demo-app-page-1")
    authenticator.login(location="unrendered", key="authenticator-page-1")

    st.success("You are logged in!")
    st.balloons()


elif st.session_state == {} or st.session_state["authentication_status"] is None:
    st.warning("Please use the button below to navigate to Home and log in.")
    st.page_link("Home.py", label="Home", icon="🏠")
    st.stop()


# Check for Admin Access
try:
    user_roles = st.session_state["config"]["credentials"]["usernames"][
        st.session_state.username
    ].get("roles")

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

except KeyError:
    pass
