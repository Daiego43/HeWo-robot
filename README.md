# HeWo Bot
## A personal robot project
After two years of working on a social robotics project, I have decided to conduct an opensource project for
the community to gather basic knowledge on how to design human robot interactions.

This is a repository for a series of implementations of open-source packages. In order to develop a 
minicharacter/assistant called HeWo the robot, HeWo-bot or simply hewo. 

The tools are already out there, we have to use them all.

<p align="center">
  <img src="images/hewo.png" alt="Hewo the robot" width="50%">
</p>

And yes `HeWo` comes from `Hello World`.

## Infraestructure and Philosophy
Originally, HeWo was just a face in a pygame window, but if we want to scale it up, the face itself should be a publisher
and suscriber to a series of topics or commands.

This is why we need to separate all of the face features in a separate module, and the same will be for every other
feature of the robot.
If then we follow this module philosophy, development will be clearer.(But keep in mind that as it will grow in complexity, more package segmentation will be needed).

### First modules
- **Face module**: Origin of the project. Face module is a pygame window that runs a ros node that take care of controlling the elements in the display. Controlling elements in the display is also really easy thanks to pygame.
- **Vision module**: Using all of mediapipe features. This module could be divided in two: Camera and vision.
- **Web monitor module**: Used to monitor and control robot behavior from a web interface.




## Devices used
- Raspberry Pi 4 with and Adeept Motor HAT (from rasptank robot). The HAT makes it easier to control stuff.
<p align="center">
  <img src="images/raspi1.png" alt="Raspberry Pi and HAT 1" width="50%">
  <img src="images/raspi2.png" alt="Raspberry Pi and HAT 2" width="50%">
</p>

- Bluetooth usb c microphones
<p align="center">
  <img src="images/microphone.png" alt="Bluetooth USB C microphones" width="50%">
</p>
- Camera for computer vision, Intel Realsense D400 series
<p align="center">
  <img src="images/camera.png" alt="Intel Realsense Camera" width="50%">
</p>

- Display. I am using a mini display resembling an old computer monitor.
<p align="center">
  <img src="images/display.png" alt="Mini display" width="50%">
</p>
It also has ports for everything, such as oudio output, usb, usb-type c, hdmi, etc...


## Goals
### Basic
- [x] Face expression setup 
- [ ] Face expression control engine
- [ ] Voice recognition
- [ ] Voice synthesis
- [ ] Voice control engine
- [ ] Computer vision data processing
- [ ] Dialog engine and conversational data processing
- [ ] Audio interface to record/play audio


### Movement
- [ ] Neck design and type of mechanism choice
- [ ] Design of the body of the robot
- [ ] Choice of claws/hands
- [ ] Choice of wheels/legs
