import sys
import pickle
#sys.path.append(".")

#from models_classifiers import models_classifiers
import streamlit as st
from PIL import Image

###Data import
with open('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/data_merge.pickle', 'rb') as handle:
    data_merge = pickle.load(handle)
with open('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/XGB_clf.pickle', 'rb') as handle:
    XGB_model = pickle.load(handle)
with open('/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/RF_clf.pickle', 'rb') as handle:
    RFC_model = pickle.load(handle)





dictClassifiers={"XGB_model_lab":"XGB_model","RFC_model_lab":"RFC_model"}

def select_classifiers (dictClassifiers, typeModel):
    for key, val in dictClassifiers.items():
        if typeModel=="XGB_model_lab":
            model_selected=val
            left_frame.write("Global Score is: 0.92")

        elif typeModel =="RFC_model_lab":
            model_selected=val
            left_frame.write("Global Score is: 0.94")





if __name__ == '__main__':
    left_frame = st.sidebar

    st.title("hello")
    st.write("je commence")


    im=Image.open("C:/Users/Karim/Desktop/Data_Science/Projets/Projet_07/P7_Yahiatene_Karim/app_scoring/images/logo.png")
    left_frame.image(im,width=100)
    left_frame.title("Classifiers")
    typeModel=left_frame.selectbox("select",("XGB_model_lab","RFC_model_lab"))
    #left_frame.write(typeModel)

    select_classifiers(dictClassifiers,typeModel)




