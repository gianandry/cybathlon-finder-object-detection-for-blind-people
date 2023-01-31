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

![Setup scheme of the task](/readme_images/target_objects.png?raw=true "Target objects")

## Solution implemented
The solution requires a HD webcam and a computer. The camera can be hand-held by the user or attached to a wrist band.

In the first phase, the user recognizes the target. The system informs the user that it is ready, and the user identifies the target using the camera. The system then communicates the target to the user and asks if they want to move on to the next phase.

In the second phase, the user moves their arm to search for the target object. If an obstacle is framed, the system reproduces an obstacle sound. If the target is framed, the system reproduces a target sound. The sound increases in volume as the target gets closer to the center of the camera. After the system locates the target for more than ten frames and it is no longer seen, the system asks the user if they have grasped the target.

## Running the project
The version of python 3.10 was used. The requirements of the project are present in the file `requirements.txt`.
We use the 'ssd_mobilenet_v1_coco' (MobileNet-SSD trained on COCO dataset), trained using TensorFlow Object Detection API.
These files are contained in `frozen_inference_graph.zip`, the latter has to be extracted in the working path.
The following command starts the system:
```
python main.py
```
For the second phase previously defined, the function `beep_phase.py`. Some input parameters can be changed according to the task:
- **nn** corresponds to the dimension of the neural network,
- **s** corresponds to the minimal accuracy with which an object is recognized,
- **Zoom** can be True or False depending on whether you want to use the zoom,
- **z** corresponds to the value of the zoom in case it is activated,
- **show_image** can be True or False depending on whether you want to see the frames of the camera in the screen.

A different function `beep_phase_alternative.py` has been implemented to improve the performance for the toothbrush, the most challenging object.
`beep_phase_tutorial.py` is given to get familiar with the system and the sounds before the use of the complete functioning.


