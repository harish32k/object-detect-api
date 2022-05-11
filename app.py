import os
import torch
from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    #img_names = ['img', 'img1', 'img2', 'img3', 'img4']
    print("received image(s)")
    instances = request.json.get('instances')
    
    names = []
    images = []
    for instance in instances:
        names.append(instance['name'])
        enc_img = instance['image']
        img_bytes = BytesIO(base64.b64decode(enc_img))
        image = Image.open(img_bytes)
        images.append(image)
    
    results = model(images, size=640)
    results_xyxy = results.pandas().xyxy
    outputs = []
    for i in range(len(results_xyxy)):
        result = results_xyxy[i]
        output = { "detections" : eval(result.to_json(orient="records")),
            "name" : names[i]
        }
        outputs.append(output)
    
    to_return = {'predictions' : outputs}
    return jsonify(to_return)

@app.route('/health', methods=['GET'])
def health_check():
   return jsonify({"status": 'healthy'})


if __name__ == "__main__":
    
    torch.hub.set_dir(os.path.join('static'))
    model = torch.hub.load("ultralytics/yolov5", "yolov5x", force_reload=False)  # force_reload to recache
    app.run(host="0.0.0.0", port=5000)  # debug=True causes Restarting with stat
