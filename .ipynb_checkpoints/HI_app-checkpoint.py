import streamlit as st
import pickle

model = pickle.load(open('HI_model.pkl','rb'))

st.title("Health Insurance Price Prediction")

age=st.text_input('Age:')

gender=st.radio(
    'select your gender',
    ["male","female"]
)
# gender=st.text_input('Gender:')

bmi=st.slider(
    "select a BMI:",
    min_value=15.0,
    max_value=60.0,
    value=15.0,
    step=0.1
)

# bmi=st.text_input('BMI:')

children=st.selectbox(
    'No. of children:',
    ['0','1','2','3','4','5']
)


# children = st.text_input('No. of children:')
# smoker = st.text_input('Do you Smoker:')

smoker=st.radio(
    'Do you Smoker:',
    ["yes","false"]
)

if st.button('Summit'):
    age = int(age)
    bmi = float(bmi)
    children = int(children)
    gender_enc = 1 if gender =='female' else 0
    smoker_enc = 1 if smoker =='yes' else 0
    q = [[age,gender_enc,bmi,children,smoker_enc]]
    yp = round(model.predict(q)[0],2)
    st.write('your premium:'+ str(yp))




st.markdown(
    f"""
    <div style="
        background: linear-gradient(135deg, #14532d, #166534);
        border: 2px solid #22c55e;
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(34,197,94,0.2);
    ">
        <p style="
            color: #bbf7d0;
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 10px;
        ">
            🛡️ YOUR ESTIMATED PREMIUM
        </p>
        <h1 style="
            color: white;
            font-size: 38px;
            margin: 0;
        ">
            ₹{float(yp):,.2f}
        </h1>
        <p style="
            color: #bbf7d0;
            font-size: 14px;
            margin-top: 10px;
            margin-bottom: 0;
        ">
            Estimated Health Insurance Cost
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
