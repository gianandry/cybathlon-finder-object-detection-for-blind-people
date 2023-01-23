# first phase: understand which is the object to find
# you need to add the following line to the main:
# target = start.define_target(cvNet, classes)
# cv.destroyAllWindows()


import numpy as np
import cv2 as cv
import time
import pyttsx3
from vocal_command import vocal_command


        
def define_target(cvNet, classes, colors, cam):
    
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    tic=time.perf_counter()
    #cam = cv.VideoCapture()
    flag = 0
    exit = 0
    while True:
        ret_val, imgi = cam.read() #USARE PER VIDEO
        #imgi = cv.imread('images/prova3.jpg') #USARE PER IMMAGINE

        rows = imgi.shape[0]
        cols = imgi.shape[1]
        c = int(cols/2)  
        r = int(rows/2)
        imgs = [imgi]
        image = []
        for img in imgs:
            cvNet.setInput(cv.dnn.blobFromImage(img, size=(400, 400), swapRB=True, crop=False))
            cvOut = cvNet.forward()
        
            # Go through each object detected and label it
            for detection in cvOut[0,0,:,:]:
                score = float(detection[2])
                if score > 0.7:
        
                    idx = int(detection[1])   # prediction class index. 

                    rowsa = img.shape[0]
                    colsa = img.shape[1]
                    
                    if classes[idx] == 'banana' or classes[idx] == 'bottle' or classes[idx] == 'cell phone' or classes[idx] == 'toothbrush' or classes[idx] == 'apple' or classes[idx] == 'cup':         
                        target = classes[idx]
                        left = detection[3] * colsa
                        top = detection[4] * rowsa
                        right = detection[5] * colsa
                        bottom = detection[6] * rowsa
                        cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)
                    
                        # draw the prediction on the frame
                        label = "{}: {:.2f}%".format(classes[idx],score * 100)
                        y = top - 15 if top - 15 > 15 else top + 15
                        cv.putText(img, label, (int(left), int(y)),cv.FONT_HERSHEY_SIMPLEX, 0.5, colors[idx], 2)
                        flag = 1
                        toc=time.perf_counter()
                        interval=toc-tic
                    
                        
                        # The text that you want to convert to audio
                        
                        mytext = "The object is a "+target+". Do you want to pass to the next phase?"
                        # speaking initialization
                        engine = pyttsx3.init()
                        voices = engine.getProperty('voices')
                        engine.setProperty('voice', voices[1].id)
                        # texting of the speaking 
                        engine.say(mytext)
                        engine.runAndWait()
                        
                        while(flag):
                            try:
                                command = vocal_command()
                                print(command)
                            except Exception as e:
                                print(e)
                            if "yes" in command:
                                exit = 1
                                flag = 0
                                mytext = "Passing to the next phase"
                                # speaking initialization
                                engine = pyttsx3.init()
                                voices = engine.getProperty('voices')
                                engine.setProperty('voice', voices[1].id)
                                # texting of the speaking 
                                engine.say(mytext)
                                engine.runAndWait()
                            elif "no" in command:
                                flag = 0
                                mytext = "I try to look again"
                                # speaking initialization
                                engine = pyttsx3.init()
                                voices = engine.getProperty('voices')
                                engine.setProperty('voice', voices[1].id)
                                # texting of the speaking 
                                engine.say(mytext)
                                engine.runAndWait()
                            else:
                                mytext = "I did not understand, repeat!"
                                # speaking initialization
                                engine = pyttsx3.init()
                                voices = engine.getProperty('voices')
                                engine.setProperty('voice', voices[1].id)
                                # texting of the speaking 
                                engine.say(mytext)
                                engine.runAndWait()
                        tic=time.perf_counter()
                        if exit == 1:
                            return target

        imgi=cv.resize(imgi,(1280,720))
        cv.imshow('immagine', imgi)
        # Press ESC to quit
        if cv.waitKey(1) == 27: 
            break
        
        
    return target