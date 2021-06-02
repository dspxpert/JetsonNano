
#include <Servo.h>

Servo myservo;

const char SET_MIN_TAG = 'n';
const char SET_MAX_TAG = 'x';
const char SET_DEGREE_TAG = 'd';
const char SET_PULSE_TAG = 'p';

const int outPin = 7;     // the physical pin
unsigned int min_pulse = 771;
unsigned int max_pulse = 2740;
unsigned int pulse = 1500;
unsigned int degree = 90;
unsigned int mode = 0;

void setup(){
  Serial.begin(115200);
  myservo.attach(outPin, min_pulse, max_pulse);
  myservo.write(degree);
  delay(1000);
  instructions();
}

void loop(){
  processSerial();
}

void processSerial(){
  static long val = 0;
  if ( Serial.available()){
    char ch = Serial.read();
    if(ch == 'k' || ch == 'K') val = val * 1000;
    if(ch >= '0' && ch <= '9') // is ch a number?
    {
      val = val * 10 + ch - '0'; // yes, accumulate the value
    }
    else if(ch == SET_MIN_TAG)
    {
      if(val > 0)
      { 
        min_pulse = val;
        Serial.print("Setting Min pulse to ");
        Serial.println(min_pulse);
        myservo.detach();
        myservo.attach(outPin, min_pulse, max_pulse);
        if(mode == 0) myservo.write(degree);
        else myservo.writeMicroseconds(pulse);
        show();
        delay(500);
      }
      val = 0;
    }
    else if(ch == SET_MAX_TAG)
    {
      if(val > 0)
      { 
        max_pulse = val;
        Serial.print("Setting Max pulse to ");
        Serial.println(max_pulse);
        myservo.detach();
        myservo.attach(outPin, min_pulse, max_pulse);
        if(mode == 0) myservo.write(degree);
        else myservo.writeMicroseconds(pulse);
        show();
        delay(500);
      }
      val = 0;
    }
    else if(ch == SET_PULSE_TAG)
    {
      if(val >= min_pulse && val <= max_pulse)
      { 
        pulse = val;
        Serial.print("Setting Pulse to ");
        Serial.println(pulse);
        myservo.writeMicroseconds(pulse);
        mode = 1;
        show();
        delay(500);
      }
      val = 0;
    }
    else if(ch == SET_DEGREE_TAG)
    {
      if(val >= 0 && val <= 180)
      { 
        degree = val;
        Serial.print("Setting Degree to ");
        Serial.println(degree);
        myservo.write(degree);
        mode = 0;
        show();
        delay(500);
      }
      val = 0;
    }
  }
}

void show(){
  Serial.print("["+String(min_pulse)+", "+String(max_pulse)+"] - ");
  if (mode ==0){
    Serial.println(String(degree)+" degree\n");
  }
  else {
    Serial.println(String(pulse)+" microseconds\n");
  }
}

void instructions(){
  Serial.println("Send values followed by one of the following tags:");
  Serial.println(" n - sets miNimum pulse period in microseconds");
  Serial.println(" x - sets maXimum pulse period in microseconds");
  Serial.println(" d - sets servo position in Degree");
  Serial.println(" p - sets servo position in Pulse period(microseconds)\n");
  show();
}
