
import tensorflow as tf
from tensorflow.keras.models import load_model
import tensorflow_hub as hub
import os
cwd=os.getcwd()

model=load_model(cwd+"/my_tomato_model_mobilenet.h5", custom_objects={'KerasLayer':hub.KerasLayer})
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE] #FOR OPTIMIZING THER SIZE EVEN MORE
tflite_model = converter.convert()
open("my_trained_mobilenet.tflite", "wb").write(tflite_model)
