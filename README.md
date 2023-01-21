# Cybathlon finder - object detection for blind people
## Team
Campanelli Andrea <br>
Coccoli Gianmarco <br>
Scassola federico <br>

## Definition of the task
This repository contains a possible solution fo the cybathlon race called finder.
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
The solution implemented requires a webcam HD and a computer. The camera can be hand held by the user or it can be attached to a band and tied to the wrist. 
In a first phase the user has to recognize the target. After the start, the system informs that it is ready, so the user has to recognize with the camera the target of the trial. Then the system communicates the user the object detected and asks if he wants to pass to the next phase. This check is performed because sometimes happens that the system recognizes an object while it is not pointing to the target in the box. This phase is specific for the cybathon race, anyway it is possible to modify easily modify it and make the user direcly communicate the target by vocal command.
## Running the project
