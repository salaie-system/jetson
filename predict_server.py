# load modules
import flask
import pandas as pd
import tensorflow as tf
import cv2
import numpy as np

# init flask
app = flask.Flask(__name__)

# init tensorflow
sess = tf.Session()
graph = tf.get_default_graph()
tf.keras.backend.set_session(sess)
model = tf.keras.models.load_model("/home/nvidia/workspace/models/ResNet50_model_weights.h5")

def predict_image(image_filename):
    """
    撮影された画像を学習済みモデルで推論し、結果を返す
    """
    image_size = 150
    image_directory = "/home/nvidia/Pictures/" 
    np_image = cv2.imread(image_directory + image_filename, cv2.IMREAD_COLOR)
    np_resize_image = cv2.resize(np_image, (image_size, image_size))
    np_resize_reshape_image = np_resize_image.reshape(-1, image_size, image_size, 3)
    global graph, graph
    with graph.as_default():
        tf.keras.backend.set_session(sess)
        result = str(np.ndarray.argmax(model.predict(np_resize_reshape_image)))
    print("Predict " + image_filename + " : " + result)
    return result

@app.route("/predict", methods=["GET"])
def predict():
    """
    getリクエストから受け取るファンクション
    """
    data = {"success": False}
    params = flask.request.args
    data["success"] = True
    data["image"] = params.get("path")
    data["predict"] = predict_image(params.get("path"))
    return flask.jsonify(data)

# start the flask app
app.run(host='0.0.0.0')
