import pickle
import streamlit as st
import datetime
import pandas as pd
import base64
import streamlit as st

# loading the saved models
date_time = datetime.datetime.now()
usedcar_model = pickle.load(open('C:/Users/Reshma/Downloads/FpCarPrice/random_forest_model_test.sav', 'rb'))


def main():
	#setting page configuration
    st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🧊",
    # layout="wide",
    menu_items={
        'About': "This is a web application to predict the price of a pre-owned car in the current market.",
        'Report a bug': "mailto:reshmarajan318@gmail.com"
    }
)
    html_temp="""
     <div style = "background-color:rgb(76, 127, 237);padding:16px;">
     <h2 style="color:black;text-align:center;">Used Car Price Prediction Using ML</h2>
     </div>
    """
    # heading for the web app.
    st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown("Are you planning to sell your car !?")
    st.markdown("This the place where you can know the correct value on your car.")
    st.markdown("Please answer some simple question to know your cars worth.")
    st.write('')
    st.write('')

    #collecting inputs from user 
    car_company = st.selectbox('What is the brand of the car?',('Audi','BMW','Ford','Hyundai','Mercedes','Skoda'))

    car_model = st.text_input('What is the model of the car?')

    F1 = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic', 'Semi-Auto', 'Other'))
    if F1=="Manual":
        p1=0
    elif F1=="Automatic":
        p1=1
    elif F1=="Automatic":
        p1=3
    elif F1=="Other":
        p1=4
          
    p2 = st.number_input('What is distance completed by the car in Miles ?',100,50000000,step=100)

    F3 = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'Hybrid', 'Other', 'Electric'))
    if F3=="Petrol":
        p3=0
    elif F3=="Diesel":
        p3=1
    elif F3=="Hybrid":
        p3=2
    elif F3=="Electric":
        p3=3
    elif F3=="Other":
        p3=4
        
    p4 = st.number_input('Miles per gallon ?  (mgp)',1.0,100.0,step=1.0) 
        
    p5 = st.number_input('What is the engine size of the car ? ',1.0,10.0,step=10.0) 
    
    
    years = st.number_input('In which year car was purchased ?',1990,date_time.year,step=1)

    p6 = date_time.year-years
    
    #loading the input to the model
    data_new = pd.DataFrame({
     'transmission':p1,
    'mileage':p2,
    'fuelType':p3,
    'mpg':p4,
    'engineSize':p5,
    'Age':p6
},index=[0])
    try: 
        if st.button('Predict'):
        	#making prediction with applied model
            prediction = usedcar_model.predict(data_new)
            if prediction>0:
                st.success('You can sell your {company} {model} for {price:.2f} pounds'.format(price = prediction[0], company=car_company,model = car_model))
            else:
                st.warning("Sorry.. You will be not able to sell your {company} {model} !!".format(price = prediction[0], company=car_company,model = car_model))
    except:
        st.warning("Opps!! Something went wrongn Please Try again")

    
    
    
if __name__ == '__main__':
    main()

    
