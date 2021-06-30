########################################### Librairies #################################################
import streamlit as st
import pickle
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import sqlite3
import hashlib

conn= sqlite3.connect('data_base.db')
c = conn.cursor()
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data_base = c.fetchall()
	return data_base

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()
def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False


########################################### Variables #################################################
# type_org=['Business Entity Type 3', 'School', 'Government', 'Religion', 'Other', 'XNA', 'Electricity',
#                   'Medicine', 'Business Entity Type 2', 'Self-employed', 'Transport: type 2',
#                   'Construction', 'Housing', 'Kindergarten', 'Trade: type 7', 'Industry: type 11', 'Military',
#                   'Services', 'Security Ministries', 'Transport: type 4', 'Industry: type 1',
#                   'Emergency', 'Security', 'Trade: type 2', 'University', 'Transport: type 3', 'Police',
#                   'Business Entity Type 1', 'Postal', 'Industry: type 4', 'Agriculture',
#                   'Restaurant', 'Culture', 'Hotel', 'Industry: tye 7', 'Trade: type 3', 'Industry: type 3', 'Bank',
#                   'Industry: type 9', 'Insurance', 'Trade: type 6', 'Industry: type 2',
#                   'Transport: type 1', 'Industry: type 12', 'Mobile', 'Trade: type 1', 'Industry: type 5',
#                   'Industry: type 10', 'Legal Services', 'Advertising', 'Trade: type 5',
#                   'Cleaning', 'Industry: type 13', 'Trade: type 4', 'Telecom', 'Industry: type 8', 'Realtor',
#                   'Industry: type 6']
# type_emploi = ['Laborers', 'Core staff', 'Accountants', 'Managers', 'Drivers', 'Sales staff', 'Cleaning staff',
#                    'Cooking staff',
#                    'Private service staff', 'Medicine staff', 'Security staff', 'High skill tech staff',
#                    'Waiters/barmen staff', 'Low-skill Laborers', 'Realty agents',
#                    'Secretaries', 'IT staff', 'HR staff']
list_features = []
list_features_real = []
cl_id=False
###Load data
def loadData(file):
    with open(file,'rb') as handle:
        outputData = pickle.load(handle)
    return outputData

data_all = loadData('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/app_scoring/data/data_appli.pickle')
data_string=loadData('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/app_scoring/data/string_values.pickle')
scaler = loadData('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/app_scoring/data/scaler.pickle')
XGB_clf = loadData('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/app_scoring/data/XGB_clf.pickle')

# ORGANIZATION_dict = loadData('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/ORGANIZATION_TYPE_normal.pickle')
# OCCUPATION_TYPE_dict = loadData('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/OCCUPATION_TYPE_normal.pickle')
##chargement des logos
file_logo='/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/app_scoring/images/logo.png'
accorde='/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/app_scoring/images/accordé.png'
refuse='/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/app_scoring/images/refusé.png'
########################################### Functions #################################################


def insertPersonnalInformations(list_features,list_features_real):

    global button_soumettre
    local_css("style.css")
    nom = st.text_input("Name")
    prenom = st.text_input("First name")
    age = st.slider("How old are you ?", 18, 125, 25)

    list_features.append([nom])
    list_features.append([prenom])

    type_contrat = st.selectbox("Type of Contract",data_string.NAME_CONTRACT_TYPE.drop_duplicates().tolist())

    if type_contrat =="Cash loans":
        list_features.append([1,0])
        list_features_real.append("Cash loans")
    elif type_contrat =="Revolving loans":
        list_features.append([0,1])
        list_features_real.append("Revolving loans")

    genre = st.radio("Genre:",('Women', 'Man', 'Bi'))
    if genre =="Women":
        list_features.append([1,0,0])
        list_features_real.append("Women")

    elif genre == "Man":
        list_features.append([0,1,0])
        list_features_real.append("Man")

    else:
        list_features.append([0,0,1])
        list_features_real.append("Bi")

    voiture = st.radio("Do you have a car:",('Yes', 'No'))
    if voiture =="Yes":
        list_features.append([1,0])
        list_features_real.append("Yes")

    elif voiture =="No":
        list_features.append([0,1])
        list_features_real.append("No")


    nombre_enfant = st.slider("How many children ?", 0, 50, 0)
    list_features.append([nombre_enfant])
    list_features_real.append(nombre_enfant)

    proprietaire = st.radio("Are you owner?",('Yes', 'No'))
    if proprietaire =="Yes":
        list_features.append([1,0])
        list_features_real.append("Yes")

    elif proprietaire =="No":
        list_features.append([0,1])
        list_features_real.append("No")


    rente_annuelle=st.text_input("Annual salary",0)
    list_features.append([float(rente_annuelle)])
    list_features_real.append(float(rente_annuelle))

    montant_pret=st.text_input("The loan amount",0)
    list_features.append([float(montant_pret)])
    list_features_real.append(float(montant_pret))


    rente_pret=st.text_input("Rental income",0)
    list_features.append([float(rente_pret)])
    list_features_real.append(float(rente_pret))

    prix_bien_pret_accorde=st.text_input("Amount granted",0)
    list_features.append([float(prix_bien_pret_accorde)])
    list_features_real.append(float(prix_bien_pret_accorde))

    list_features.append([float(age)])
    list_features_real.append(float(age))

    statut_marital = st.selectbox("Marital Status",data_string.NAME_FAMILY_STATUS.drop_duplicates().tolist())
    if statut_marital =="Single / not married":
        list_features.append([1,0,0,0,0,0])
        list_features_real.append("Single / not married")

    elif statut_marital =="Married":
        list_features.append([0,1,0,0,0,0])
        list_features_real.append("Married")


    elif statut_marital =="Widow":
        list_features.append([0,0,1,0,0,0])
        list_features_real.append("Widow")


    elif statut_marital =="Civil marriage":
        list_features.append([0,0,0,1,0,0])
        list_features_real.append("Civil marriage")


    elif statut_marital =="Separated":
        list_features.append([0,0,0,0,1,0])
        list_features_real.append("Separated")

    elif statut_marital =="Unknown":
        list_features.append([0,0,0,0,0,1])
        list_features_real.append("Unknown")



    type_bien = st.selectbox("Housing type",data_string.NAME_HOUSING_TYPE.drop_duplicates().tolist())
    if type_bien =="House / apartment":
        list_features.append([1,0,0,0,0,0])
        list_features_real.append("House / apartment")

    elif type_bien =="Rented apartment":
        list_features.append([0,1,0,0,0,0])
        list_features_real.append("Rented apartment")

    elif type_bien =="With parents":
        list_features.append([0,0,1,0,0,0])
        list_features_real.append("With parents")

    elif type_bien =="Municipal apartment":
        list_features.append([0,0,0,1,0,0])
        list_features_real.append("Municipal apartment")

    elif type_bien =="Office apartment":
        list_features.append([0,0,0,0,1,0])
        list_features_real.append("Office apartment")

    elif type_bien == "Co-op apartment":
        list_features.append([0,0,0,0,0,1])
        list_features_real.append("Co-op apartment")



    # type_immobilier=st.text_input("Nom")
    niveau_etude = st.selectbox("Type education",['Secondary / secondary special', 'Higher education', 'Incomplete higher',
                                                  'Lower secondary', 'Academic degree'])
    if niveau_etude =='Secondary / secondary special':
        list_features.append([1,0,0,0,0])
        list_features_real.append("Secondary / secondary special")

    elif niveau_etude =='Higher education':
        list_features.append([0,1,0,0,0])
        list_features_real.append("Higher education")

    elif niveau_etude =='Incomplete higher':
        list_features.append([0,0,1,0,0])
        list_features_real.append("Incomplete higher")

    elif niveau_etude =='Lower secondary':
        list_features.append([0,0,0,1,0])
        list_features_real.append("Lower secondary")

    elif niveau_etude =='Academic degree':
        list_features.append([0,0,0,0,1])
        list_features_real.append("Academic degree")



    duree_emploi=st.slider("Days employed", 0, 400000, 0)
    list_features.append([duree_emploi])
    list_features_real.append(float(duree_emploi))


    type_societe = st.selectbox("Organization Type",['Business Entity', 'Education', 'Government', 'Religion', 'Other', 'Health', 'Self-employed', 'Services', 'Bank and Insurance', 'Industry'])

    if type_societe =='Business Entity':
        list_features.append([1,0,0,0,0,0,0,0,0,0])
        list_features_real.append('Business Entity')
    elif type_societe =='Education':
        list_features.append([0,1,0,0,0,0,0,0,0,0])
        list_features_real.append("Education")
    elif type_societe =='Government':
        list_features.append([0,0,1,0,0,0,0,0,0,0])
        list_features_real.append("Government")
    elif type_societe =='Religion':
        list_features.append([0,0,0,1,0,0,0,0,0,0])
        list_features_real.append("Religion")
    elif type_societe =='Other':
        list_features.append([0,0,0,0,1,0,0,0,0,0])
        list_features_real.append("Other")
    elif type_societe =='Health':
        list_features.append([0,0,0,0,0,1,0,0,0,0])
        list_features_real.append("Health")
    elif type_societe =='Self-employed':
        list_features.append([0,0,0,0,0,0,1,0,0,0])
        list_features_real.append("Self-employed")
    elif type_societe =='Services':
        list_features.append([0,0,0,0,0,0,0,1,0,0])
        list_features_real.append("Services")
    elif type_societe =='Bank and Insurance':
        list_features.append([0,0,0,0,0,0,0,0,1,0])
        list_features_real.append("Bank and Insurance")
    elif type_societe =='Industry':
        list_features.append([0,0,0,0,0,0,0,0,0,1])
        list_features_real.append("Industry")


    type_post = st.selectbox("Occupation Type ",['Laborers', 'Service staff', 'Accountants', 'Managers', 'Medicine staff', 'Realty agents', 'Secretaries', 'IT staff', 'HR staff'])
    if type_post =='Laborers':
        list_features.append([1,0,0,0,0,0,0,0,0])
        list_features_real.append('Laborers')
    elif type_post =='Service staff':
        list_features.append([0,1,0,0,0,0,0,0,0])
        list_features_real.append('Service staff')
    elif type_post =='Accountants':
        list_features.append([0,0,1,0,0,0,0,0,0])
        list_features_real.append("Accountants")
    elif type_post =='Managers':
        list_features.append([0,0,0,1,0,0,0,0,0])
        list_features_real.append("Managers")
    elif type_post =='Medicine staff':
        list_features.append([0,0,0,0,1,0,0,0,0])
        list_features_real.append("Medicine staff")
    elif type_post =='Realty agents':
        list_features.append([0,0,0,0,0,1,0,0,0])
        list_features_real.append("Realty agents")
    elif type_post =='Secretaries':
        list_features.append([0,0,0,0,0,0,1,0,0])
        list_features_real.append("Secretaries")
    elif type_post =='IT staff':
        list_features.append([0,0,0,0,0,0,0,1,0])
        list_features_real.append("IT staff")
    elif type_post =='HR staff':
        list_features.append([0,0,0,0,0,0,0,0,1])
        list_features_real.append("HR staff")


# @st.cache()
def load_logo(file_logo):
    # Chargement du logo
    logo = Image.open(file_logo)

    return logo
logo=load_logo(file_logo)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

import time
def identification():
    global cl_id, cl,username,password
    local_css("style.css")
    html_template = """
    <div style="background-color:{};padding:10px">
    <h1 style="color:{};text-align:center"> Connection to the application  </h1>
    </div>
    """
    st.markdown(html_template.format("#2C3539","#FFFFFF"), unsafe_allow_html=True)


    st.subheader("Login Section")


    username = st.text_input("User Name")
    password = st.text_input("Password", type="password")
    # col1, col2 = form.beta_columns(2)
    action = st.radio("", ('Login', 'Creat an Account'))
    if action=="Login":

        create_usertable()
        hashed_pswd = make_hashes(password)
        result = login_user(username,check_hashes(password,hashed_pswd))

        if result:
            cl_id=True
            cl=username
            st.success("Logged In as {}".format(username))
        elif password=="" or username=="":
            pass
        else:
            st.warning('Incorrect Username or Password')
    elif action=="Creat an Account":
        new_user = st.text_input("Username")
        new_password = st.text_input("Creat a password", type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")





# @st.cache (suppress_st_warning=True)



def runInsertPersonnalInformations():

    global scaler, XGB_clf, list_features, list_features_real,reponse
    local_css("style.css")
    html_template = """
    <div style="background-color:{};padding:10px">
    <h1 style="color:{};text-align:center"> General information  </h1>
    </div>
    """
    st.markdown(html_template.format("#2C3539","#FFFFFF"), unsafe_allow_html=True)




    insertPersonnalInformations(list_features, list_features_real)

    arr = np.array([item for sublist in list_features for item in sublist][2:])
    with open('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/app_scoring/data/arr_output.pickle','wb') as handle:
        pickle.dump(arr, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/app_scoring/data/arr_output_str.pickle','wb') as handle:
        pickle.dump(list_features_real, handle, protocol=pickle.HIGHEST_PROTOCOL)
    if st.button("Submit"):
        X_scaled = scaler.fit_transform(arr[:, np.newaxis])
        y_pred = XGB_clf.predict(X_scaled.T)
        if int(y_pred[0]) == 0:
            st.image(accorde, width=100)
            st.write("Score is:"+str(0.62), width=100)
        elif int(y_pred[0]) == 1:
            st.image(refuse, width=100)
            st.write("Score is:"+str(0.62), width=100)

    else:
        pass



list_input_data=[data_all,data_string]

def plotFigure(list_input_data):
    html_template = """
    <div style="background-color:{};padding:10px">
    <h1 style="color:{};text-align:center"> Loan Simulation  </h1>
    </div>
    """
    st.markdown(html_template.format("#2C3539","#FFFFFF"), unsafe_allow_html=True)

    # st.write(data.list_features)
    arr_output = loadData('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/arr_output.pickle')
    arr_output_str = loadData('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/arr_output_str.pickle')

    col1 = st.beta_columns(3)
    col2 = st.beta_columns(3)
    col3 = st.beta_columns(3)


    sns.set()

    ## salaire annuel
    fig, ax = plt.subplots(figsize=(16, 15.2))
    fig = sns.FacetGrid(list_input_data[0], hue='TARGET', height=4,size=4, aspect=1)
    fig=fig.map(sns.kdeplot, 'AMT_INCOME_TOTAL', shade=True)
    plt.axvline(arr_output_str[5], color='red')
    fig.axes[0,0].set_xlabel('AMT_INCOME_TOTAL')
    legend_labels = ['Client','Credit granted', 'Credit refused']
    fig.axes[0,0].legend(legend_labels)
    col1[0].pyplot(fig)

    ## Valeur Credit
    fig, ax = plt.subplots(figsize=(16, 15.2))
    fig = sns.FacetGrid(list_input_data[0], hue='TARGET', height=4, aspect=1)
    fig.map(sns.kdeplot, 'AMT_CREDIT', shade=True)
    plt.axvline(arr_output_str[6], color='red')
    fig.axes[0,0].set_xlabel('AMT_CREDIT')
    legend_labels = ['Client','Credit granted', 'Credit refused']
    fig.axes[0,0].legend(legend_labels)
    col1[1].pyplot(fig)

    ## Ancienté emploi
    fig = sns.FacetGrid(list_input_data[0], hue='TARGET', height=4, aspect=1)
    fig.map(sns.kdeplot, 'DAYS_EMPLOYED', shade=True)
    plt.axvline(arr_output_str[8], color='red')
    fig.axes[0,0].set_xlabel('DAYS_EMPLOYED')
    legend_labels = ['Client','Credit granted', 'Credit refused']
    fig.axes[0,0].legend(legend_labels)
    col1[2].pyplot(fig)

    ## Sexe du client
    fig, ax = plt.subplots(figsize=(16, 15.2))
    ax.hist(list_input_data[1][['CODE_GENDER','TARGET']])
    keys=['Man','Woman','Bi']
    val=[0.05,1.05,2]
    dictInfo=dict(zip(keys, val))
    for key,val in dictInfo.items():
        if arr_output_str[1] == key:
            plt.axvline(val, color='red', linewidth=3)
    ax.set_xlabel('CODE_GENDER', size=40)
    legend_labels = ['Client','Credit granted', 'Credit refused']
    ax.tick_params(axis='both', which='major', labelsize=36)
    ax.legend(legend_labels)
    plt.setp(ax.get_legend().get_texts(), fontsize=36)
    col2[0].pyplot(fig)

    ## Statut marital
    fig, ax = plt.subplots(figsize=(16, 15.2))
    ax.hist(list_input_data[1][['NAME_FAMILY_STATUS','TARGET']])
    keys = ['Single\n not married', 'Married', 'Widow', 'Civil marriage', 'Separated', 'Unknown']
    val = [0.1,1.15,2.15,3.15,4.15,5.15]
    dictInfo=dict(zip(keys, val))
    for key,val in dictInfo.items():
        if arr_output_str[10] == key:
            plt.axvline(val, color='red', linewidth=3)

    ax.set_xlabel('NAME_FAMILY_STATUS', size=40)
    legend_labels = ['Client','Credit granted', 'Credit refused']
    ax.tick_params(axis='both', which='major', labelsize=36)
    ax.set_xticklabels(keys)

    ax.legend(legend_labels)
    plt.setp(ax.get_legend().get_texts(), fontsize=36)
    col2[1].pyplot(fig)

    ## Proprietaire de voiture
    fig, ax = plt.subplots(figsize=(16, 15.2))
    ax.hist(list_input_data[1][['FLAG_OWN_CAR','TARGET']])
    keys=["Yes","No"]
    val=[0.025,1.025]
    dictInfo=dict(zip(keys, val))
    for key,val in dictInfo.items():
        if arr_output_str[2] == key:
            plt.axvline(val, color='red', linewidth=3)
    ax.set_xlabel('FLAG_OWN_CAR', size=40)
    legend_labels = ['Client','Credit granted', 'Credit refused']
    ax.tick_params(axis='both', which='major', labelsize=36)
    ax.set_xticklabels(keys)
    ax.legend(legend_labels)
    plt.setp(ax.get_legend().get_texts(), fontsize=36)
    col2[2].pyplot(fig)

    ## Proprietaire de bien
    fig, ax = plt.subplots(figsize=(16, 15.4))
    ax.hist(list_input_data[1][['FLAG_OWN_REALTY','TARGET']])
    keys=["Yes","No"]
    val=[0.025,1.025]
    dictInfo=dict(zip(keys, val))
    for key,val in dictInfo.items():
        if arr_output_str[2] == key:
            plt.axvline(val, color='red', linewidth=3)
    ax.set_xlabel('FLAG_OWN_REALTY', size=40)
    legend_labels = ['Client','Credit granted', 'Credit refused']
    ax.tick_params(axis='both', which='major', labelsize=36)
    ax.set_xticklabels(keys)
    ax.legend(legend_labels)
    plt.setp(ax.get_legend().get_texts(), fontsize=36)
    col3[0].pyplot(fig)

    ## Age Client

    fig = sns.FacetGrid(list_input_data[0], hue='TARGET', height=4, aspect=1)
    fig.map(sns.kdeplot, 'AGE', shade=True)
    plt.axvline(arr_output_str[9], color='red')
    fig.axes[0,0].set_xlabel("Age")
    legend_labels = ['Client','Credit granted', 'Credit refused']
    fig.axes[0,0].legend(legend_labels)
    col3[1].pyplot(fig)

    ## Nombre d'enfants

    fig = sns.FacetGrid(list_input_data[0], hue='TARGET', height=4, aspect=1)
    fig.map(sns.kdeplot, 'CNT_CHILDREN', shade=True)
    fig.axes[0,0].set_xlabel("CNT_CHILDREN")
    plt.axvline(arr_output_str[3], color='red')

    legend_labels = ['Client','Credit granted', 'Credit refused']
    fig.axes[0,0].legend(legend_labels)
    col3[2].pyplot(fig)

def visu():
    html_template = """
    <div style="background-color:{};padding:10px">
    <h1 style="color:{};text-align:center"> Welcome to the intercative visualisation </h1>
    </div>
    """
    st.markdown(html_template.format("#2C3539","#FFFFFF"), unsafe_allow_html=True)

    axe_X = st.sidebar.selectbox("Axe X", data_all.columns.tolist())
    axe_Y = st.sidebar.selectbox("Axe Y", data_all.columns.tolist())
    plot_type = st.sidebar.radio("", ('kdeplot','Histogram', 'Scatter',))
    if plot_type=="kdeplot":
        fig = sns.FacetGrid(list_input_data[0], hue=axe_X, height=4, aspect=1)
        fig.map(sns.kdeplot, axe_Y, shade=True)
        fig.axes[0, 0].set_xlabel(axe_X)
        fig.axes[0, 0].set_ylabel(axe_Y)
        st.pyplot(fig)

    elif plot_type=="Scatter":
        fig, ax = plt.subplots(figsize=(16, 15.2))

        ax.scatter(list_input_data[0][axe_X], list_input_data[0][axe_Y])
        ax.set_xlabel(axe_X, size=40)
        ax.set_ylabel(axe_Y, size=40)

        st.pyplot(fig)
    elif plot_type == "Histogram":

        fig, ax = plt.subplots(figsize=(16, 15.2))
        ax.hist(list_input_data[0][[axe_X, axe_Y]])
        ax.set_xlabel(axe_X, size=40)
        ax.set_ylabel(axe_Y, size=40)
        st.pyplot(fig)





########################################### Excecution part ###########################################
if __name__ == '__main__':

    # st.beta_set_page_config(layout="wide")
    row1 = st.sidebar.beta_columns(1)
    row2 = st.sidebar.beta_columns(1)
    row3 = st.sidebar.beta_columns(1)
    row2[0].image(logo, width=300)
    task = row2[0].selectbox("Menu", ["Identification", "Information", "Simulation", "Visualisation"])
    if task == "Identification":
        identification()
        if cl_id:
            row1[0].write("Bienvenu "+cl)

    elif task == "Information":
        runInsertPersonnalInformations()

        # row1[0].write("Bienvenu " + cl)
        # row3[0].write(reponse)


    elif task == "Simulation":
        plotFigure(list_input_data)
        # row1[0].write("Bienvenu " + cl)

        # if reponse==0:
        #     row3[0].image(accorde, width=100)
        # elif reponse==1:
        #     row3[0].image(refuse, width=100)
    elif task == "Visualisation":
        visu()





