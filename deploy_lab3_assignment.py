
import streamlit as st 
import joblib 

# st.title("Hello World")

st.title("nepali news Classifier")

model = joblib.load("news_classification_nepali.joblib")
text = st.text_area(label = "", max_chars=1000, height = 300)





if st.button("Predict Category"):
    prediction = model.predict([text])[0]
    print(prediction)
    st.success(f"Predicted news category is {prediction}")