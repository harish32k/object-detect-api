
# Object Detection API

API to get a objects detected and labeled from images, using the YoloV5 object detection model. This API is specifically developed for a Blind Assistive device.

## About
This is a Flask based web-application that is developed for deployment on Google Cloud Platform. This repository was successfully deployed to Google Cloud's Vertex AI service.
### Purpose
This application helps get a objects detected, labeled and annotated. The gets an input for the images to be labeled and the output will be the images that have objects labeled along with the data on the names of the objects detected, and the respective coordinates of the bounding boxes for those objects.

## How to build and deploy
- Build the docker image using the `Dockerfile` in the repository, preferably using a service like Google Cloud Build to make the process easy. 
- Deploy the model on Google Cloud Vertex AI platform using the docker image that is built.

YoloV5 model link:
https://github.com/ultralytics/yolov5

More about the YoloV5 model

Jocher, G., Chaurasia, A., Stoken, A., Borovec, J., NanoCode, Kwon, Y., TaoXie, Fang, J., imyhxy, Michael, K., Lorna, Abhiram, V., Montes, D., Nadar, J., Laughing, tkianai, yxNONG, Skalski, P., Wang, Z., … Minh, M. T. (2022). ultralytics/yolov5: v6.1 - TensorRT, TensorFlow Edge TPU and OpenVINO Export and Inference. Zenodo.
