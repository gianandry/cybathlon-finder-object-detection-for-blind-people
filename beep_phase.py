import numpy as np
import math
import cv2 as cv # OpenCV computer vision library
from detected_object import DetectedObject
import pygame
import time
import os
from vocal_command import vocal_command
import pyttsx3

def beep_phase(cam, cvNet, classes, target, nn=500, s=0.3, Crop=False, Zoom = True, z = 1.5, show_image = False):
  #INITIALIZATION OF VARIABLES
  sounds_path = os.getcwd() + "/sounds/"  #initializations for sounds played
  pygame.mixer.init()
  sounds = ("sound_1", "sound_2", "sound_3", "sound_4")
  playing_sound = None
  toplay_sound = None
  colors = np.random.uniform(0, 150, size=(len(classes), 3)) #initialization of colors print of image
  flag = []  #flag used to exit the beep phase
  z1 = (z-1)/(2*z) #constants used for the zoom
  z2 = (z+1)/(2*z)
  rg= [25, 40, 60] # IMPORTANT!! these are the limits of the ranges used to the define the sound ranges
  norm_ranges = ([0, rg[0]-1], [rg[0], rg[1]-1], [rg[1], rg[2]-1], [rg[2], 100])
  time_object_not_located = 4
  
  #WHILE CICLE OF FRAMES ACQUIRED BY THE CAMERA
  while True:
    ret_val, imgi = cam.read() #read image from camera
    cols = imgi.shape[1] #dir x
    rows = imgi.shape[0] #dir y
    #pre-treatment of image
    if Zoom:
      imgi = imgi[int(rows*z1):int(rows*z2), int(cols*z1):int(cols*z2)]
      cols = imgi.shape[1] #dir x
      rows = imgi.shape[0] #dir y
    c = int(cols/2)  
    r = int(rows/2)
    if Crop:
      img1 = imgi[:r, :c]
      img2 = imgi[:r, c:]
      img3 = imgi[r:, :c]
      img4 = imgi[r:, c:]
      img5 = imgi[int(rows/4):int(rows*3/4), int(cols/4):int(cols*3/4)] 
      imgs = [img1, img2, img3, img4, img5]
    else:
      imgs = [imgi]
    #initialization of variables
    diag = int(math.sqrt(c*c+r*r))
    object_found = False
    target_found = False
    obstacle_found = False
    obstacle_right = False
    obstacle_left = False
    image = []
    objs = []
    norms = []
    # FOR USED DURING THE CROP - GOES THROUGH EACH DIVISION OF THE IMAGE
    for idx_img, img in enumerate(imgs):
      cvNet.setInput(cv.dnn.blobFromImage(img, size=(nn, nn), swapRB=True, crop=False)) #start of neural network
      cvOut = cvNet.forward() #passes the image to the neural network and stores results in cvOut
      rowsa = img.shape[0]
      colsa = img.shape[1]
      #GO THROUGH EACH DETECTED OBJECT AND LABELS IT
      for detection in cvOut[0,0,:,:]:
        score = float(detection[2])
        if score > s:
          idx = int(detection[1])   # prediction class index. 
          if classes[idx] == 'banana' or classes[idx] == 'bottle' or classes[idx] == 'cell phone' or classes[idx] == 'toothbrush' or classes[idx] == 'apple' or classes[idx] == 'cup':
            object_found = True
            if classes[idx] == target: #if detection is the target start flag and tic to end the run
              target_found = True
              flag.append(1)
              tic = time.perf_counter()
            else:
              obstacle_found = True
            left = detection[3] * colsa
            top = detection[4] * rowsa
            right = detection[5] * colsa
            bottom = detection[6] * rowsa
            #EXTRACT NORM
            x_rel = int((right+left)/2)
            y_rel = int((bottom+top)/2)
            deti = DetectedObject(idx_img, x_rel, y_rel, classes[idx], target, c, r) #creation of object representing the detection
            objs.append(deti)
            norm = deti.norm()
            norms.append(norm)
            if obstacle_found:  #if one or more obstacle are found we need to know if they cover right and/or left area
              if deti.x > 0:
                obstacle_right = True
              if deti.y < 0:
                obstacle_left = True
            if target_found:  #exit from loop in detections
              break 
      if target_found:  #exit from loop of images (needed with crop)
        break

    #SOUNDS PART
    #if the object found is an OBSTACLE and NO target is found
    if obstacle_found: 
      obstacle_range = 75 
      if z == 2: #with this level of zoom it is better to play the obstacle sound even with the highest level of distance
        obstacle_range = 100
      if min(norms) <= obstacle_range:
        if obstacle_right and not obstacle_left:
          toplay_sound = sounds_path + "sound_wrongR" + ".mp3"
        elif obstacle_left and not obstacle_right:
          toplay_sound = sounds_path + "sound_wrongL" + ".mp3"
        else:
          toplay_sound = sounds_path + "sound_wrong" + ".mp3"  
      else:
        toplay_sound = None
        playing_sound = None
        
    #if the TARGET is detected
    beep = ""
    direction = ""
    up_down = ""
    if target_found:
      for idx_sound, n in enumerate(norm_ranges):
        if (norm >= n[0] and norm <= n[1]):
          beep = sounds[idx_sound]
      if beep != "sound_1":
        if deti.x > 0:
          direction = "R"
        else:
          direction = "L"
        if deti.y > int(rg[0]*diag/100): #pixels corresponding to 24 distance
          up_down = "U"
        if deti.y < -int(rg[0]*diag/100):
          up_down = "D"
      toplay_sound = sounds_path + beep + direction + up_down + ".mp3"
            
    #if NO OBJECT is detected
    if not object_found:
      toplay_sound = None
      playing_sound = None

    #use pygame to load/stop/change sound played
    if toplay_sound == None:
      pygame.mixer.music.unload()
    elif toplay_sound != playing_sound:
      pygame.mixer.music.unload()
      pygame.mixer.music.load(toplay_sound)
      pygame.mixer.music.play()
      playing_sound = toplay_sound
    
    #DRAWINGS ON IMAGE
    if show_image:
      cv.circle(imgi,(c,r), 10, (251,206,177), -1)  
      for obj in objs:
        x,y = obj.pos_pix()
        cv.line(imgi, (c, r), (x, y), (251,206,177))
        cv.circle(imgi,(x, y), 5, (0,0,255), -1)
      imgi=cv.resize(imgi,(1280,720)) #resize of image to pc format
      cv.imshow('immagine', imgi)
      if cv.waitKey(1) == 27: # Press ESC to quit
          break
  
    #EXIT FROM MODE
    toc = time.perf_counter()
    if len(flag) > 10 and not target_found:
      interval = toc-tic
      if interval >= time_object_not_located:
        pygame.mixer.music.unload()
        mytext = "Have you grasped the "+target+"?"
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        # texting of the speaking 
        engine.say(mytext)
        engine.runAndWait()
        while(True):
          try:
              command = vocal_command()
              print(command)
          except Exception as e:
              print(e)
          if "yes" in command:
              mytext = "Good job!"
              engine = pyttsx3.init()
              voices = engine.getProperty('voices')
              engine.setProperty('voice', voices[1].id)
              # texting of the speaking 
              engine.say(mytext)
              engine.runAndWait()
              return
          if "no" in command:
              flag = []
              mytext = "I try to look again"
              engine = pyttsx3.init()
              voices = engine.getProperty('voices')
              engine.setProperty('voice', voices[1].id)
              # texting of the speaking 
              engine.say(mytext)
              engine.runAndWait()
              break
  return