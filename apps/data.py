
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import sqlite3
# conn== sqlite3.connect(data.db)
# c=conn.cursor()

# def creat_table():
#     c.execute("")

def importPickeles(file):
    with open(file,'rb') as handle:
        outputData = pickle.load(handle)
    return outputData


data_all = importPickeles('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/data_appli.pickle')
data_string=importPickeles('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/string_values.pickle')
scaler = importPickeles('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/scaler.pickle')
XGB_clf = importPickeles('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/XGB_clf.pickle')
ORGANIZATION_dict = importPickeles('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/ORGANIZATION_TYPE_normal.pickle')
OCCUPATION_TYPE_dict = importPickeles('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/OCCUPATION_TYPE_normal.pickle')


# def oneHotEncoding():
type_org=['Business Entity Type 3', 'School', 'Government', 'Religion', 'Other', 'XNA', 'Electricity', 'Medicine', 'Business Entity Type 2', 'Self-employed', 'Transport: type 2',
 'Construction', 'Housing', 'Kindergarten', 'Trade: type 7', 'Industry: type 11', 'Military', 'Services', 'Security Ministries', 'Transport: type 4', 'Industry: type 1',
 'Emergency', 'Security', 'Trade: type 2', 'University', 'Transport: type 3', 'Police', 'Business Entity Type 1', 'Postal', 'Industry: type 4', 'Agriculture',
 'Restaurant', 'Culture', 'Hotel', 'Industry: tye 7', 'Trade: type 3', 'Industry: type 3', 'Bank', 'Industry: type 9', 'Insurance', 'Trade: type 6', 'Industry: type 2',
 'Transport: type 1', 'Industry: type 12', 'Mobile', 'Trade: type 1', 'Industry: type 5', 'Industry: type 10', 'Legal Services', 'Advertising', 'Trade: type 5',
 'Cleaning', 'Industry: type 13', 'Trade: type 4', 'Telecom', 'Industry: type 8', 'Realtor', 'Industry: type 6']
type_emploi=['Laborers', 'Core staff', 'Accountants', 'Managers', 'Drivers', 'Sales staff', 'Cleaning staff', 'Cooking staff',
 'Private service staff', 'Medicine staff', 'Security staff', 'High skill tech staff', 'Waiters/barmen staff', 'Low-skill Laborers', 'Realty agents',
 'Secretaries', 'IT staff', 'HR staff']
list_features=[]
list_features_real=[]
def insertPersonnalInformations(list_features,list_features_real):

    global button_soumettre
    st.subheader("Informations Personnelles")

    nom = st.text_input("Nom")
    prenom = st.text_input("Prenom")
    age = st.slider("Quelle age avez-vous ?", 20, 125, 25)

    list_features.append([nom])
    list_features.append([prenom])

    type_contrat = st.selectbox("Type de contrat",["prêts d'argents","prêts renouvlable"])

    if type_contrat =="prêts d'argents":
        list_features.append([1,0])
        list_features_real.append("prêts d'argents")
    elif type_contrat =="prêts renouvlable":
        list_features.append([0,1])
        list_features_real.append("prêts renouvlable")

    genre = st.radio("Genre:",('Femme', 'Homme', 'Bi'))
    if genre =="Femme":
        list_features.append([1,0,0])
        list_features_real.append("Femme")

    elif genre == "Homme":
        list_features.append([0,1,0])
        list_features_real.append("Homme")

    else:
        list_features.append([0,0,1])
        list_features_real.append("Bi")

    voiture = st.radio("Avez vous une voiture:",('Oui', 'Non'))
    if voiture =="Oui":
        list_features.append([1,0])
        list_features_real.append("Oui")

    elif voiture =="Non":
        list_features.append([0,1])
        list_features_real.append("Non")


    nombre_enfant = st.slider("Nombre d'enfants ?", 0, 50, 0)
    list_features.append([nombre_enfant])
    list_features_real.append(nombre_enfant)

    propriétaire = st.radio("Etes-vous deja propriétaire?",('Oui', 'Non'))
    if propriétaire =="Oui":
        list_features.append([1,0])
        list_features_real.append("Oui")

    elif propriétaire =="Non":
        list_features.append([0,1])
        list_features_real.append("Non")

    rente_annuelle=st.text_input("Salaire annuel",0)
    list_features.append([float(rente_annuelle)])
    list_features_real.append(float(rente_annuelle))

    montant_pret=st.text_input("Le montant du pret",0)
    list_features.append([float(montant_pret)])
    list_features_real.append(float(montant_pret))


    rente_pret=st.text_input("Rente des locations",0)
    list_features.append([float(rente_pret)])
    list_features_real.append(float(rente_pret))

    prix_bien_pret_accordé=st.text_input("Somme accordé",0)
    list_features.append([float(prix_bien_pret_accordé)])
    list_features_real.append(float(prix_bien_pret_accordé))

    list_features.append([float(age)])
    list_features_real.append(float(age))

    statut_marital = st.selectbox("Statut Marital",["Célibataire/Divorcé","Marié","Pacé","veuve/veuf",
                                            "Séparé","Inconnu"])
    if statut_marital =="Célibataire/Divorcé":
        list_features.append([1,0,0,0,0,0])
        list_features_real.append("Célibataire/Divorcé")

    elif statut_marital =="Marié":
        list_features.append([0,1,0,0,0,0])
        list_features_real.append("Marié")


    elif statut_marital =="Pacé":
        list_features.append([0,0,1,0,0,0])
        list_features_real.append("Pacé")


    elif statut_marital =="veuve/veuf":
        list_features.append([0,0,0,1,0,0])
        list_features_real.append("veuve/veuf")


    elif statut_marital =="Séparé":
        list_features.append([0,0,0,0,1,0])
        list_features_real.append("Séparé")

    elif statut_marital =="Inconnu":
        list_features.append([0,0,0,0,0,1])
        list_features_real.append("Inconnu")

    type_bien = st.selectbox("Type de proprieté",["Maison/Appartement","Appartement de location",
                                                     "Vie chez des parents","Logement social","Appartement bureau", "Colocation"])
    if type_bien =="Maison/Appartement":
        list_features.append([1,0,0,0,0,0])
        list_features_real.append("Maison/Appartement")

    elif type_bien =="Appartement de location":
        list_features.append([0,1,0,0,0,0])
        list_features_real.append("Appartement de location")

    elif type_bien =="Vie chez des parents":
        list_features.append([0,0,1,0,0,0])
        list_features_real.append("Vie chez des parents")

    elif type_bien =="Logement social":
        list_features.append([0,0,0,1,0,0])
        list_features_real.append("Logement social")

    elif type_bien =="Appartement bureau":
        list_features.append([0,0,0,0,1,0])
        list_features_real.append("Appartement bureau")

    elif type_bien == "Colocation":
        list_features.append([0,0,0,0,0,1])
        list_features_real.append("Colocation")



    # type_immobilier=st.text_input("Nom")
    niveau_etude = st.selectbox("Niveau d'etude",['Secondary / secondary special', 'Higher education', 'Incomplete higher',
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



    durée_emploi=st.slider("Durée de l'emploi ?", 0, 50, 0)
    list_features.append([durée_emploi])
    list_features_real.append(float(durée_emploi))

    type_societé = st.selectbox("Type de scieté",type_org)

    for key1, value1 in ORGANIZATION_dict.items():
        if key1 == type_societé:
            list_features.append([value1])
            list_features_real.append(key1)

        else:
            pass

    type_post = st.selectbox("Type d'emploi",type_emploi)
    for key2, value2 in OCCUPATION_TYPE_dict.items():
        if key2 == type_post:
            list_features.append([value2])
            list_features_real.append(key2)

        else:
            pass

    button_soumettre=st.button("Soumettre")
    arr = np.array([item for sublist in list_features for item in sublist][2:])
    return  button_soumettre,arr

def PersonnalInformationsToArray(var=None):
    global  list_features
    list_features=[]
    list_features_real=[]
    button_soumettre, arr = insertPersonnalInformations(list_features,list_features_real)
    if button_soumettre:
        X_scaled = scaler.fit_transform(arr[:,np.newaxis])
        y_pred=XGB_clf.predict(X_scaled.T)
        # GB_clf.score(X_scaled, y_train)
        if int(y_pred[0])==0:
            # st.write("Pret accordé")
            st.write(arr)
            # plotFigure()
        elif int(y_pred[0])==1:
            st.write("Pret refusé")

    else:
        pass

