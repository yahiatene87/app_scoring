import streamlit as st



# def identification(val=None):
#     "Loging app"
#     html_template = """
#     <div style="background-color:{};padding:10px">
#     <h1 style="color:{};text-align:center"> "Connection a l'application AccordPret" </h1>
#     </div>
#     """
#     st.markdown(html_template.format("#777799","#8D9089"), unsafe_allow_html=True)
#
#     col1, col2 = st.beta_columns(2)
#     menu = ["Home", "Login", "SingUp"]
#
#
#     if col1.button("Login"):
#         st.subheader("Login Section")
#         username = st.text_input("User Name")
#         password = st.text_input("Password", type="password")
#         # if st.sidebar.button("Login"):
#         if password == "0000":
#             st.success("Logged In ass {}".format(username))
#
#
#             # task=st.selectbox("Task",["Add Post","Analytics", "Profiles"])
#             # if task=="Add Post":
#             #     st.subheader("Add Your Post")
#             #     insertPersonnalInformations()
#             # elif task == "Analytics":
#             #     st.subheader("Analytics")
#         else:
#             st.warning('Incorrect Username or Password')
#
#
#     elif col2.button("SingUp"):
#         st.subheader("Creae New Account")
#         new_user = st.text_input("Username")
#         new_passsword = st.text_input("Password", type='password')
#         # if st.button("Singup"):
#         st.success("You have successfully created an valid Acount")
#         st.info("Go to Login Menu to login")

def identification(val=None):
    "Loging app"
    html_template = """
    <div style="background-color:{};padding:10px">
    <h1 style="color:{};text-align:center"> "Connection a l'application AccordPret" </h1>
    </div>
    """
    st.markdown(html_template.format("#777799","#8D9089"), unsafe_allow_html=True)


    menu = ["Home", "Login", "SingUp"]
    st.subheader("Login Section")
    username = st.text_input("User Name")
    password = st.text_input("Password", type="password")
    col1, col2 = st.beta_columns(2)
    if col1.button("Login"):
        # if st.sidebar.button("Login"):
        if password == "0000":
            st.success("Logged In as {}".format(username))


            # task=st.selectbox("Task",["Add Post","Analytics", "Profiles"])
            # if task=="Add Post":
            #     st.subheader("Add Your Post")
            #     insertPersonnalInformations()
            # elif task == "Analytics":
            #     st.subheader("Analytics")
        else:
            st.warning('Incorrect Username or Password')


    elif col2.button("Creat an Account"):
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_passsword = st.text_input("Password", type='password')
        # if st.button("Singup"):
        st.success("You have successfully created an valid Acount")
        st.info("Go to Login Menu to login")
