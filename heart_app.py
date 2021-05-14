# import libraries
import streamlit as st
import pickle
import numpy as np
import sklearn

# load models
survey_model = pickle.load(open('model_heart.p', 'rb'))
diabetes_model = pickle.load(open('model_diabetes.p', 'rb'))

################################################################################
# This section lays out the design of the home page
st.title('Heart Health Screening Tool')
st.write('This app allows you to check your risk for heart disease or diabetes.')
st.markdown('---')

page = st.sidebar.selectbox('', ('Home', 'Heart Disease', 'Diabetes'))

if page == 'Home':
    st.write("Heart disease is the #1 cause of death in the US. It can cause heart \
    attack, stroke and other ailments. Most cases of heart disease are preventable. \
    Dietary and lifestyle changes can lower one's risk of developing the condition \
    and there are medical treatments to help manage symptoms if it is developed.") # this line of code will explain the app and how to use it
    st.write('')
    st.write('Diabetes is another disease that affects much of the population. It \
    is caused by having blood sugar levels that are too high and some people \
    experience insulin resistance. It is also preventable for many \
    people with healthy diet and lifestyle habits. Lifestyle changes are also used \
    for treatment along with medical and prescription interventions.') # info about diabetes
    st.write('')
    st.write('To check to see if you are at risk of developing heart disease or \
    diabetes, choose a questionnaire below and follow the prompts.')

    page = st.selectbox('', ('Choose a Questionnaire', 'Heart Disease', 'Diabetes'))

if page == 'Choose a Questionnaire':
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.markdown('---')
    st.markdown("\
    [Information Source](https://www.cdc.gov/heartdisease/index.htm#:~:text=Heart%20disease%20is%20the%20leading,can%20lead%20to%20heart%20attack.) | \
    [Information Source](https://medlineplus.gov/diabetes.html#:~:text=Diabetes%20is%20a%20disease%20in,body%20does%20not%20make%20insulin.)")

    # disclaimer
    st.write('Disclaimer: This website is for informational purposes only and is not \
    intended to be a substitute for professional medical advice, diagnosis, treatment \
    or legal advice. For questions concerning your health, please contact your physician \
    or other qualified medical professional.')
    st.write('')
    st.write('If you are experiencing a medical emergency, please contact 911 or \
    go to your nearest emergency room.')

################################################################################
# this section lays out the design for the heart disease assessment page

if page == 'Heart Disease':
    st.header('Heart Disease Questionnaire')
    hype = st.selectbox('Have you ever been told you have high blood pressure \
     or hypertension?', ['','Yes', 'No'])
    chol = st.selectbox('Have you ever been told you have high cholesterol?',
    ['', 'Yes', 'No'])
    ang = st.selectbox('Have you ever been told you had angina? (Squeezing, pressure, \
    heaviness, pain in the chest due to reduced blood flow)', ['', 'Yes', 'No'])
    atck = st.selectbox('Have you ever been told you had a heart attack?', ['', 'Yes', 'No'])

    miss = st.selectbox('Did you work last week?', ['', 'Yes', 'No'])
    duty = st.selectbox('Are you currently on full-time active duty in the armed forces?',
    ['', 'Yes', 'No'])

    over_65 = st.selectbox('Is anyone living in your home over 65 years of age?',
    ['', 'Yes', 'No'])
    ss_rr = st.selectbox('Is anyone living in your home receiving retirement income \
    from Social Security or Railroad Retirement?', ['', 'Yes', 'No'])
    insure = st.radio('Do you have any of the following insurances?', ['Private Insurance',
    'Medicare', 'Medicaid', 'Tricare', 'CHIP', 'VA Healthcare', 'CHAMPUS',
    'Indian Health Service', 'State-Sponsored Plan','Other Government Plan',
    'None of These'])
    submit = st.button('Submit', key=1)

    # function to process heart disease inputs
    def input_process(hypertension, cholesterol, angina, attack, miss_work, act_duty,
    over65, ssrr, insurance):
        if hypertension == 'No':
            hypertension = 1
        else:
            hypertension = 0
        if cholesterol == 'No':
            cholesterol = 1
        else:
            cholesterol = 0
        if angina == 'No':
            angina = 1
        else:
            angina = 0
        if attack == 'No':
            attack = 1
        else:
            attack = 0
        if miss_work == 'No':
            miss_work = 1
        else:
            miss_work = 0
        if act_duty == 'No':
            act_duty = 1
        else:
            act_duty = 0
        if ssrr == 'No':
            ssrr = 1
        else:
            ssrr = 0
        if over65 == 'Yes':
            over65 = 1
        else:
            over65 = 0
        if insurance == 'None of These':
            insurance = 1
            medicare = 1
        elif insurance == 'Medicare':
            insurance = 0
            medicare = 0
        else:
            insurance = 0
            medicare = 1

        X = [act_duty, miss_work, medicare, over65, ssrr, insurance, attack, angina,
        cholesterol, hypertension]
        result = np.array(X).reshape(1,-1)
        return result

    # run heart disease model with user inputs
    if submit:
        heart_X = input_process(hypertension=hype, cholesterol=chol,
        angina=ang, attack=atck, miss_work=miss, act_duty=duty,
        over65=over_65, ssrr=ss_rr, insurance=insure)

        prediction = survey_model.predict_proba(heart_X)[0]
        # st.write(prediction)

        # output depending on prediction probabilities
        if prediction[1] >= .35 and prediction[1] < .50:
            st.write('You may be at risk of developing heart disease.')
            st.write('Here are some things to consider speaking with your physician about:')
            st.markdown('--Blood Tests')
            st.markdown('--Urinalysis')
            st.markdown('--Biopsy')
            st.markdown('--HRCT scan, CT scan, MRI, Ultrasound, Xray')
            st.write('Below are links to resources to help you learn more about risk factors, \
            symptoms and ways to prevent heart disease.')
            st.write('')
        elif prediction[1] >= .5:
            st.write('You may be at risk of developing heart disease.')
            st.write('Here are some things to consider speaking with your physician about:')
            st.markdown('--Blood Tests')
            st.markdown('--Urinalysis')
            st.markdown('--ECG or EKG (electrocardiogram)')
            st.markdown('--Echocardiogram ultrasound')
            st.markdown('--Exercise stress test')
            st.markdown('--CT scan, Chest Xray')
            st.markdown('--Coronary angiogram')
            st.markdown('--Cardiac catheterization')
            st.write('Below are links to resources to help you learn more about \
            risk factors, symptoms and ways to prevent heart disease.')

        else:
            st.write('Your risk is currently low.')
            st.write('Below are links to resources to help you maintain your low risk:')


    st.markdown('---')
    st.markdown("\
    [ABCS of Heart Health](https://millionhearts.hhs.gov/data-reports/factsheets/ABCS.html) | \
    [Heart Attack & Stroke Symptoms](https://www.heart.org/en/about-us/heart-attack-and-stroke-symptoms)")
    # disclaimer
    st.write('Disclaimer: This website is for informational purposes only and is not \
    intended to be professional medical advice, diagnosis, treatment \
    or legal advice. For questions concerning your health, please contact your physician \
    or other qualified medical professional.')
    st.write('')
    st.write('If you are experiencing a medical emergency, please contact 911 or \
    go to your nearest emergency room.')
    st.markdown("[Data Source](https://www.cdc.gov/nchs/nhis/2019nhis.htm)")

################################################################################
# this section lays out the design for the diabetes assessment page
if page == 'Diabetes':
    st.header('Diabetes Questionnaire')
    hype = st.selectbox('Have you ever been told you have high blood pressure \
     or hypertension?', ['','Yes', 'No'])
    chol = st.selectbox('Have you ever been told you have high cholesterol?',
    ['', 'Yes', 'No'])
    sugar = st.selectbox('Have you had a blood sugar test within the last 12 months?',
    ['', 'Yes', 'No'])
    pre_diab = st.selectbox('Have you ever been told you have prediabetes?',
    ['', 'Yes', 'No'])
    ht_disease = st.selectbox('Have you ever been told you have heart disease?',
    ['', 'Yes', 'No'])
    script = st.selectbox('Have you taken prescription medications in the last 12 \
    months?', ['', 'Yes', 'No'])
    pneu = st.selectbox('Have you ever had a pneumonia shot?', ['', 'Yes', 'No'])
    miss = st.selectbox('Did you work last week?', ['', 'Yes', 'No'])
    insure = st.radio('Do you have any of the following insurances?', ['Private Insurance',
    'Medicare', 'Medicaid', 'Tricare', 'CHIP', 'VA Healthcare', 'CHAMPUS',
    'Indian Health Service', 'State-Sponsored Plan','Other Government Plan',
    'None of These'])
    submit_diab = st.button('Submit', key=1)

    # function to process diabetes inputs
    def diabetes_input(hypertension, cholesterol, sugar_test, pre_diabetes,
    heart_dis, rx_script, pneumonia, miss_work, insurance):
        if hypertension == 'No':
            hypertension = 1
        else:
            hypertension = 0
        if cholesterol == 'No':
            cholesterol = 1
        else:
            cholesterol = 0
        if sugar_test == 'Yes':
            sugar_test = 1
        else:
            sugar_test = 0
        if pre_diabetes == 'No':
            pre_diabetes = 1
        else:
            pre_diabetes = 0
        if heart_dis == 'No':
            heart_dis = 1
        else:
            heart_dis = 0
        if rx_script == 'No':
            rx_script = 1
        else:
            rx_script = 0
        if pneumonia == 'No':
            pneumonia = 1
        else:
            pneumonia = 0
        if miss_work == 'No':
            miss_work = 1
        else:
            miss_work = 0
        if insurance == 'None of These':
            insurance = 1
            medicare = 1
        elif insurance == 'Medicare':
            insurance = 0
            medicare = 0
        else:
            insurance = 0
            medicare = 1

        X = [miss_work, medicare, pneumonia, sugar_test, rx_script, insurance,
        pre_diabetes, heart_dis, cholesterol, hypertension]
        result = np.array(X).reshape(1,-1)
        return result

    # run diabetes model with user inputs
    if submit_diab:
        diab_X = diabetes_input(hypertension=hype, cholesterol=chol, sugar_test=sugar,
        pre_diabetes=pre_diab, heart_dis=ht_disease, rx_script=script,
        pneumonia=pneu, miss_work=miss, insurance=insure)

        prediction = diabetes_model.predict_proba(diab_X)[0]

        # output from model depending on prediction probabilities
        if prediction[1] >= .35 and prediction[1] < .50:
            st.write('You may be at risk for developing diabetes.')
            st.markdown('Here are some things to consider speaking to your \
            physician about:')
            st.markdown('--Blood Tests: Fasting blood sugar levels & A1C')
            st.markdown('--Ask your eye doctor about dilation at your next vision screening.')
            st.write('Below are links to informational resources to help you learn \
            more about risk factors, symptoms, and prevention tips.')
        elif prediction[1] >= .5:
            st.write('You may be at risk for developing diabetes. You should talk \
            to your doctor about how to combat this preventable disease.')
            st.write('Here are some things to consider speaking to your \
            physician about:')
            st.markdown('--Blood Tests: Fasting blood sugar levels & A1C')
            st.markdown('--Ask your eye doctor about dilation at your next vision screening.')
            st.write('Below are links to informational resources to help you learn \
            more about risk factors, symptoms, and prevention tips.')
        else:
            st.write('Your risk is currently low.')
            st.write('Check out the links below for resources on how to maintain a low risk status.')

    st.markdown('---')
    st.markdown("\
    [Diabetes Risk Factors](https://www.heart.org/en/health-topics/diabetes/understand-your-risk-for-diabetes) | \
    [Diabetes Symptoms](https://www.heart.org/en/health-topics/diabetes/symptoms-diagnosis--monitoring-of-diabetes) | \
    [Diabetes Prevention](https://www.heart.org/en/health-topics/diabetes/prevention--treatment-of-diabetes)")
    # disclaimer
    st.write('Disclaimer: This website is for informational purposes only and is not \
    intended to be a substitute for professional medical advice, diagnosis, treatment \
    or legal advice. For questions concerning your health, please contact your physician \
    or other qualified medical professional.')
    st.write('')
    st.write('If you are experiencing a medical emergency, please contact 911 or \
    go to your nearest emergency room.')
    st.markdown("[Data Source](https://www.cdc.gov/nchs/nhis/2019nhis.htm)")
