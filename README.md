# Cybathlon finder - object detection for blind people
This repository contains a possible solution fo the cybathlon race called finder.
## Team
Campanelli Andrea - a.campanelli@studenti.unibs.it <br> 
Coccoli Gianmarco - g.coccoli002@studenti.unibs.it <br>
Scassola federico - f.scassola@studenti.unibs.it<br>

## Definition of the task
The task is to find a specific object from a group of objects for blind people. The pilots have to locate and grasp the target object, which is randomly placed inside one of the six boxes near the start line of the task.

![Setup scheme of the task](/readme_images/setup_task.png?raw=true "Setup scheme of the task")

The pilot shall verbally communicate the name of the object to the referee. The target object must then be placed on a small table near the finish line. The six objects used are:

- cup <br>
- toothbrush <br>
- cell phone <br>
- banana <br>
- apple <br>
- bottle <br>
<br>

![List target objects](/readme_images/target_objects.png?raw=true "Target objects")

## Solution implemented
The solution requires a HD webcam and a computer. The camera can be hand-held by the user or attached to a wrist band.

![Our solution device](/readme_images/mounted_device.png?raw=true "The solution implemented")

In the first phase, the user recognizes the target. The system informs the user that it is ready, and the user identifies the target using the camera. The system then communicates the target to the user and asks if they want to move on to the next phase.

In the second phase, the user moves their arm to search for the target object. If an obstacle is framed, the system reproduces an obstacle sound. If the target is framed, the system reproduces a target sound. The sound increases in volume as the target gets closer to the center of the camera. After the system locates the target and it is no longer seen for more than four seconds, the system asks the user if they have grasped the target.

## Running the project
The project requires Python 3.10 and the requirements listed in `requirements.txt`.
Key packages used include Pygame, OpenCV, SpeechRegonition & pyaudio and pyttsx3.
The system employes the 'ssd_mobilenet_v1_coco' (MobileNet-SSD trained on COCO dataset), trained using TensorFlow Object Detection API.
These files are contained in `frozen_inference_graph.zip`, which must be extracted to the working directory.

To start the system, run the following command:
```
python main.py
```
The first phase is implemented in the `start.py` file in the function `define_target` and it returns the target.

The second phase is implemented in `beep_phase.py`. Some input parameters can be changed:
- **nn**: Neural network size
- **s**: Minimum accuracy of object recognition
- **Crop**: (True/False) Wheter to divide images in four parts to improve the recognition, at the cost of increased computational time
- **Zoom**: (True/False) whether to use the zoom
- **z**: Zoom value, if activated
- **show_image**: (True/False) Whether to display the camera frames.

A different function `beep_phase_alternative.py` has been implemented to improve performance for the toothbrush, which is the most challenging object.
`beep_phase_tutorial.py` is also available to familiarize with the system and the sounds before using the full functionality.

The `vocal_command.py` contains the function for speech recognition and `detected_object.py` is used to find the distance and the position of the detected objects in the current frame.

The `sounds` folder contains all the audio files used during the program's operation. The target sound is labeled as `sound` followed by a letter indicating the direction:

- D down
- U up
- L left
- R right

Additionally, the target sound names contain a number from 1 to 4, representing the area of the frame and the frequency of the sound, where a lower number indicates a higher frequency.

Similarly, obstacle sounds are labeled as `sound_wrong with` a direction letter.
