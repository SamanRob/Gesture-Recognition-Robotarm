# Smilebot
Computer Vision based, 3d Printed Dualarm Robot, with ability to replicate body gesture.

![Robot Body Dual Arm](https://user-images.githubusercontent.com/83728692/177961737-1f2cd31a-a09a-4be4-b696-6c0d1ab6ccd3.png)

The robot arm is fully constructed by me and 3D printed with my printer. It contains mainly 5 nema 17 Stepper Motors which are controlled by an Arduino Mega using a Ramp 1.4 board. For controlling the robotic arm, the mediapipe library in Python was used and the idea was to detect different landmarks on human body and calculating different joint angles and sending them as an array to the Arduino so that the robotic arm can replicate the gesture of the human. However since the motor are not that powerful and fast, the movement is not realtime and a 5 second video framing is used to not to overload the Arduino. Besids the robotic arm can also easily be controlled using graphical user interface and sending commands to individual motors.
