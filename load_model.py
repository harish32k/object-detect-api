import torch
import os
torch.hub.set_dir(os.path.join('static'))
model = torch.hub.load("ultralytics/yolov5", "yolov5x", force_reload=False)