# Cybathlon finder - object detection for blind people
This repository contains a possible solution fo the cybathlon race called finder.
## Team
Campanelli Andrea a.campanelli@studenti.unibs.it <br> 
Coccoli Gianmarco g.coccoli002@studenti.unibs.it <br>
Scassola federico f.scassola@studenti.unibs.it<br>

## Definition of the task
Finding misplaced objects is a big challenge for blind people. Therefore, they usually keep their own apartment very tidy. 
In this task pilots have to locate and grasp a specific object from a group of other objects.
One of the six boxes on the table near the start line of the task must be opened by the pilot to determine the target object. Thereafter, the identical object must be 
located on the task space, picked up, and placed on the small table near the finish line of the task.
Initially, the six objects are randomly placed inside the six boxes on the table;  the six objects are randomly allocated to six predefined locations on the ground.

![Setup scheme of the task](/readme_images/setup_task.png?raw=true "Setup scheme of the task")

The pilot must open only one of the six boxes on the table located near the start line of the task to determine and identify the target object.
After identifying the target object, the pilot shall verbally communicate the name of the object to the referee to make sure that there is a mutual understanding 
between the pilot and the referee about the target object. The target object must be located and placed on the table near the finish line.
If the pilot or any assistive device touches any of the non-target objects, the task is failed.
<br>
the six objects that are used during the task are:
- cup
- toothbrush
- cell phone
- banana
- apple
- bottle

![Setup scheme of the task](/readme_images/target_objects.png?raw=true "Setup scheme of the task")

## Solution implemented
The solution implemented requires a HD webcam and a computer. The camera can be hand-held by the user or it can be attached to a band and tied to the wrist. In the first phase, the user has to recognize the target. After the start, the system informs the user that it is ready, so the user has to recognize the target of the trial with the camera. Then the system communicates to the user the object detected and asks if they want to move on to the next phase. This check is performed because sometimes the system recognizes an object while it is not pointing to the target in the box. This phase is specific for the cybathon race, but it is possible to easily modify it and have the user directly communicate the target through vocal command.

The second phase starts when the target is defined. The user must move their arm to check the zone where they want to find the desired object. If an obstacle is framed, the system reproduces the obstacle sound. In case of the target, it reproduces the target sound. For both sounds are directional. The sound increases in velocity as the target gets closer to the center of the camera. After the system locates the target for more than ten frames and it is no longer seen, the system asks the user if they have grasped the target.
## Running the project
The version of python 3.10 was used. The requirements of the project are present in the file "requiremets.txt".
The following command starts the system:
```
python main.py
```

