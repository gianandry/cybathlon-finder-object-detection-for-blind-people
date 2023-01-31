import cv2 as cv # OpenCV computer vision library
import numpy as np # Scientific computing library
from start import define_target
from beep_phase import beep_phase 
from beep_phase_alternative import beep_phase_alternative
import pyttsx3
import time
 
# Just use a subset of the classes
classes = ["background", "person", "bicycle", "car", "motorcycle",
  "airplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant",
  "unknown", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse",
  "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "unknown", "backpack",
  "umbrella", "unknown", "unknown", "handbag", "tie", "suitcase", "frisbee", "skis",
  "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard",
  "surfboard", "tennis racket", "bottle", "unknown", "wine glass", "cup", "fork", "knife",
  "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog",
  "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "unknown", "dining table",
  "unknown", "unknown", "toilet", "unknown", "tv", "laptop", "mouse", "remote", "keyboard",
  "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "unknown",
  "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush" ]
 
# Colors we will use for the object labels
colors = np.random.uniform(0, 150, size=(len(classes), 3))

pb  = 'frozen_inference_graph.pb'
pbt = 'ssd_inception_v2_coco_2017_11_17.pbtxt'
 
# Read the neural network
cvNet = cv.dnn.readNetFromTensorflow(pb,pbt)   
 
<<<<<<< HEAD
cam = cv.VideoCapture(0, cv.CAP_DSHOW)
=======
cam = cv.VideoCapture(1,  cv.CAP_DSHOW)
>>>>>>> 3310b84f544425304db150a0843ee25d0a5b33dc

mytext = "I am ready to start!"
# speaking initialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# texting of the speaking 
engine.say(mytext)
engine.runAndWait()

target = define_target(cvNet, classes, colors, cam)

if target == "toothbrush":
  beep_phase_alternative(cam, cvNet, classes, target, nn=700, s=0.2, Zoom = True, z = 1.5, show_image = False)
else:
  beep_phase(cam, cvNet, classes, target, nn = 500, s = 0.3, Crop=False, Zoom=True, z = 1.5, show_image=False)

cv.destroyAllWindows()
