#include <AccelStepper.h>
#include <Stepper.h>
#include <Servo.h>
#include <Arduino.h>
#include <math.h>
#include <MultiStepper.h>

#define X_ENABLE_PIN 38
#define Y_ENABLE_PIN 56
#define E0_ENABLE_PIN 24
#define E1_ENABLE_PIN 30
#define Z_ENABLE_PIN 62

int currentValue1;
int currentValue2;
int previousValue1;
int previousValue2;
int pos;

String content = "";
float data[100];


// we need to calculate the gear ratio and steps of each stepper to have accurate movement
// for each motore to increase the resolution 3 pins for microstepping were added it means 3200 steps for whole revolution is needed
// Shoulder has a ratio of 18:1>> 18x3200=57600 steps for 360 degree rotation >> 160 steps for one degree
// Arm axis, Stepper motor has gear ratio of 13.73:1 and a pulley belt transmission of 9 which comes to 123.57>>>> 123.57x3200=395424 steps for a 360 degree rotation >> 1098.4 steps for one degree rotation
// Angle to Step
// Last has a ratio of 7:1>> 7x3200=22400 steps for 360 degree rotation >> 62.22 steps for one degree
// Base 10:1>> 10x3200=32000 >>88.88
const float JOG1 = 160;
const float JOG2 = 62.22;
const float JOG3 = 160;
const float JOG4 = 62.22;
const float JOG5 = 88.88;
//Ramp 1.4

AccelStepper LeftShoulder(1, 54, 55);
AccelStepper LeftArm(1, 60, 61);
AccelStepper RightShoulder(1, 26, 28);
AccelStepper RightArm(1, 36, 34);
AccelStepper Base(1, 46, 48);

MultiStepper steppers;

int theta1Array[100];
int theta2Array[100];
int theta3Array[100];
int theta4Array[100];
int positionsCounter = 0;

Servo gripperservoRight1;
Servo gripperservoRight2;
Servo gripperservoLeft1;
Servo gripperservoLeft2;

void setup() {
  // put your setup code here, to run once:
  //for Ramp 1.4. When using in CNC shield disable it
  LeftShoulder.setEnablePin(X_ENABLE_PIN);
  LeftShoulder.setPinsInverted(false, false, true); //invert logic of enable pin
  LeftShoulder.enableOutputs();
  LeftArm.setEnablePin(Y_ENABLE_PIN);
  LeftArm.setPinsInverted(false, false, true); //invert logic of enable pin
  LeftArm.enableOutputs();
  RightShoulder.setEnablePin(E0_ENABLE_PIN);
  RightShoulder.setPinsInverted(false, false, true); //invert logic of enable pin
  RightShoulder.enableOutputs();
  RightArm.setEnablePin(E1_ENABLE_PIN);
  RightArm.setPinsInverted(false, false, true); //invert logic of enable pin
  RightArm.enableOutputs();
  Base.setEnablePin(Z_ENABLE_PIN);
  Base.setPinsInverted(false, false, true); //invert logic of enable pin
  Base.enableOutputs();

  gripperservoRight1.attach(11);
  gripperservoRight2.attach(6);
  gripperservoLeft1.attach(5);
  gripperservoLeft2.attach(4);



  Serial.begin(115200); 
  LeftShoulder.setMaxSpeed(6000);
  LeftShoulder.setSpeed(6000);
  LeftShoulder.setAcceleration(2000);
  LeftArm.setMaxSpeed(3000);
  LeftArm.setSpeed(300);
  LeftArm.setAcceleration(1000);
  RightShoulder.setMaxSpeed(6000);
  RightShoulder.setSpeed(6000);
  RightShoulder.setAcceleration(2000);
  RightArm.setMaxSpeed(3000);
  RightArm.setSpeed(3000);
  RightArm.setAcceleration(2000);
  Base.setMaxSpeed(3000);
  Base.setSpeed(3000);
  Base.setAcceleration(1000);
  

  steppers.addStepper(LeftShoulder); // adding each stepper to the multipstepper array for synchronous motion
  steppers.addStepper(LeftArm);
  steppers.addStepper(RightShoulder);
  steppers.addStepper(RightArm);
  steppers.addStepper(Base);
}

 
void loop() {

 if (Serial.available()) {
    content = Serial.readString(); // Read the incomding data from Python
    // Extract the data from the string and put into separate float variables (data[] array)
    for (int i = 0; i < 100; i++) {
      int index = content.indexOf(","); // locate the first ","
      data[i] = atol(content.substring(0, index).c_str()); //Extract the number from start to the ","
      content = content.substring(index + 1); //Remove the number from the string
    }
  }
  

  if  (data[0]>= 0 && data[0]<= 180 && data[1]>= -90 && data[1]<= 90  && data[2]>= 0 && data[2]<= 180 && data[3]>= -90 && data[3]<= 90 && data[4]>= -30 && data[4]<= 30 && data[5]>= 0 && data[5]<= 90 ) {
    long positions[5];
    positions[0]= data[0]*JOG1;
    positions[1]= data[1]*JOG2;
    positions[2]= -data[2]*JOG3;
    positions[3]= -data[3]*JOG4;
    positions[4]= data[4]*JOG5;
    
  
    
    steppers.moveTo(positions);
    steppers.runSpeedToPosition();
    LeftShoulder.setCurrentPosition(data[0]*JOG1);
    LeftArm.setCurrentPosition(data[1]*JOG2);
    RightShoulder.setCurrentPosition(-data[2]*JOG3);
    RightArm.setCurrentPosition(-data[3]*JOG4); 
    Base.setCurrentPosition(data[4]*JOG5);
    

    gripperservoRight1.write(data[5]);
    gripperservoRight2.write(-data[5]);  
    gripperservoLeft1.write(data[5]);
    gripperservoLeft2.write(-data[5]);
  }

    //Joint to Joint Motion, 
    /*if  (data[3]>= -150 && data[3]<= 150) {
      BaseStepper.moveTo(data[3]*JOG1);
      BaseStepper.runToPosition();
      delay(100);
      }
    if  (data[4]>= -100 && data[4]<= 100){
      MiddleStepper.moveTo(data[4]*JOG2);
      MiddleStepper.runToPosition();
      delay(100);
      }
    if  (data[5]>= -150 && data[5]<= 150){ 
      LastStepper.moveTo(-data[5]*JOG3);
      LastStepper.runToPosition();
      delay(100);
      }
  */
  }



