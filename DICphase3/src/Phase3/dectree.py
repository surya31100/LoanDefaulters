import pickle
import streamlit as st
import webbrowser
from sklearn.tree import DecisionTreeClassifier 
with open('loandefaulters.pickle','rb') as f:
    clf = pickle.load(f)

def main():
    st.title('Loan Defaulter Predictor')
    age = st.number_input('Age',min_value=20, max_value=60, step=1)
    ed = st.radio('Education', ['Not graduated', 'Graduated'])
    if ed == 'Not graduated':
        ed_value = 1
    else:
        ed_value = 2
    la = st.number_input('Loan Amount',min_value=0,max_value=2100000, step=100000)
    av = st.number_input('Asset Value',min_value=0,max_value=2100000, step=100000)
    nl = st.number_input('Number of Loans', min_value=0, max_value=20, step=1)
    ncl = st.number_input('Number of current loans', min_value=0, max_value=20, step=1)
    ld = st.radio('Loan defaulted in the past', ['Yes','No'])
    if ld == 'Yes':
        ld_value = 1
    else:
        ld_value = 0

    if st.button('Predict'):
        prediction = clf.predict([[age,ed_value,la,av,nl,ncl,ld_value]])
        
        if prediction==0:
            st.success('Loan Sanctioned')
            st.subheader("Congratulations!!! You can know more about why this is a great profile here")
        
        else:
            st.success('Loan Denied')
            st.subheader("Sorry, know more about which factors we have considered to deny the application")

    if st.button('Visualize'):
        webbrowser.open_new_tab('https://public.tableau.com/app/profile/surya.teja.vangala/viz/visualization_16835697066980/Dashboard1')

if __name__=='__main__':
    main()