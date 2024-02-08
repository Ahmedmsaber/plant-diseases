from PIL import Image 
import numpy as np 
import tensorflow as tf
from tensorflow.keras.preprocessing import image 
from tensorflow.keras.models import load_model 
import os
#from cate import load_classes 
 
 
classes_name = [ 
  "Apple___Apple_scab", 
  "Apple___Black_rot", 
  "Apple___Cedar_apple_rust", 
  "Apple___healthy", 
  "Blueberry___healthy", 
  "Cherry_(including_sour)___Powdery_mildew", 
  "Cherry_(including_sour)___healthy", 
  "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", 
  "Corn_(maize)___Common_rust_", 
  "Corn_(maize)___Northern_Leaf_Blight", 
  "Corn_(maize)___healthy", 
  "Grape___Black_rot", 
  "Grape___Esca_(Black_Measles)", 
  "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", 
  "Grape___healthy", 
  "Orange___Haunglongbing_(Citrus_greening)", 
  "Peach___Bacterial_spot", 
  "Peach___healthy", 
  "Pepper,_bell___Bacterial_spot", 
  "Pepper,_bell___healthy", 
  "Potato___Early_blight", 
  "Potato___Late_blight", 
  "Potato___healthy", 
  "Raspberry___healthy", 
  "Soybean___healthy", 
  "Squash___Powdery_mildew", 
  "Strawberry___Leaf_scorch", 
  "Strawberry___healthy", 
  "Tomato___Bacterial_spot", 
  "Tomato___Early_blight", 
  "Tomato___Late_blight", 
  "Tomato___Leaf_Mold", 
  "Tomato___Septoria_leaf_spot", 
  "Tomato___Spider_mites Two-spotted_spider_mite", 
  "Tomato___Target_Spot", 
  "Tomato___Tomato_Yellow_Leaf_Curl_Virus", 
  "Tomato___Tomato_mosaic_virus", 
  "Tomato___healthy" 
] 
current_path = os.getcwd()
# Load your trained Keras model 
model = load_model('model.h5') 
 
def getModel():
    return load_model(f"{current_path}/model.h5") 

def prediction(model,img_path):

    img = Image.open(img_path) 
    target_size = (128, 128)   
    img = img.resize(target_size) 
    img_array = image.img_to_array(img) 
    img_array = np.expand_dims(img_array, axis=0) 
    predictions = model.predict(img_array) 
    predictions = np.array(predictions) 
    predicted_class_index = np.argmax(predictions) 
    predict = classes_name[predicted_class_index] 
    return predict


