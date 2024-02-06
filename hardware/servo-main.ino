// Library to control Servo using ESP32S3 board
#include <ESP32Servo.h>
 
// create 2 servo object to control 2 servos independently
Servo myservo;  
Servo myservo1;


// int pos = 0; DEL
// var for pin no. that controls geared motor and servo

// geared motor
int motorpin = 13;
int motorpin1 = 14;
// servo
int servoPin = 17;
int servoPin1 = 18;

void setup() {
  // set pins for output
  pinMode(motorpin, OUTPUT);
  pinMode(motorpin1, OUTPUT);
  pinMode(servoPin, OUTPUT);
  pinMode(servoPin1, OUTPUT);

  // attach servo object to respective pins and set to starting position
  myservo.attach(servoPin, 500, 2400);
  myservo1.attach(servoPin1, 500, 2400);
  myservo.write(90); //pin 17 on board
  myservo1.write(90); //pin 18 on board

  // ROLLER CODE
  // set gear motors to run
  digitalWrite(motorpin, HIGH);
  digitalWrite(motorpin1, HIGH);

  // for debugging
  Serial.begin(115200);
}

// create function for each servo to open and drop waste into respective bins

void servoDrop() {
  // // for debugging
  // neopixelWrite(RGB_BUILTIN,0,RGB_BRIGHTNESS,0);
  myservo.write(30);
  delay(1000);
  myservo.write(90);
}

void servo1Drop() {
  // // for debugging
  // neopixelWrite(RGB_BUILTIN,RGB_BRIGHTNESS,0,0);
  myservo1.write(150);
  delay(1000);
  myservo1.write(90);
}

void loop() {
  // FINAL SERVO CODE for proof of concept of hopper
  Serial.println("servo drop");
  servoDrop();
  delay(5000);
  Serial.println("servo1 drop");
  servo1Drop();
  delay(5000);
}
