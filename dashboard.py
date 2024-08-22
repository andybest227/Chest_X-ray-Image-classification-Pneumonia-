import streamlit as st
from PIL import Image
import numpy as np
import keras as keras
import matplotlib.pyplot as plt
import tensorflow_hub as hub
from keras.utils import img_to_array
import os

# from keras.utils import img_to_array
base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, "model.best1.hdf5")


def main():
    if st.button("Logout"):
        st.experimental_set_query_params(page="login", cache_clear=True)
    file_uploaded = st.file_uploader("Choose an image...", type="jpeg")
    if file_uploaded is not None:
        image = Image.open(file_uploaded)
        st.write("Uploaded Image.")
        figure = plt.figure()
        plt.imshow(image)
        plt.axis("off")
        st.pyplot(figure)
        result, confidence = predict_class(image)
        if confidence < 60:
            st.error("Invalide Image")
            st.write("Please upload X-Ray Image")
        else:
            st.write("Prediction : {}".format(result))
            st.write("Confidence : {}%".format(confidence))

    html_temp = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    <div style="background-color:#E9FFBC;padding:10px; font-family:'Times New Roman'; text-align:center; margin-top: 2rem;">
    <h7 style="color:black;text-align:center;">Automated Madical Image Classification Using Deep Learning</h7><br>
    </div> """
    st.markdown(html_temp, unsafe_allow_html=True)


def predict_class(image):
    with st.spinner("Loading Model..."):
        classifier_model = keras.models.load_model(
            model_path,
            compile=False,
        )

    # Resize the image to (200, 200)
    test_image = image.resize((200, 200))
    # Convert to grayscale
    test_image = test_image.convert("L")
    # Convert the image to an array
    test_image = img_to_array(test_image)
    # Normalize the image data
    test_image /= 255.0
    # Flatten the image to a vector of size 40000
    test_image = test_image.flatten()
    # Expand dimensions to match model input
    test_image = np.expand_dims(test_image, axis=0)

    # Class names for prediction
    class_name = ["NORMAL", "PNEUMONIA"]

    # Predict class
    prediction = classifier_model.predict(test_image)
    confidence = round(100 * (np.max(prediction[0])), 2)
    final_pred = class_name[np.argmax(prediction)]

    return final_pred, confidence


footer = """
<style>
a:link , a:visited{
    color: white;
    background-color: transparent;
    text-decoration: None;
}

a:hover,  a:active {
    color: red;
    background-color: transparent;
    text-decoration: None;
}

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: transparent;
    color: black;
    text-align: center;
}s
</style>
"""
st.markdown(footer, unsafe_allow_html=True)
