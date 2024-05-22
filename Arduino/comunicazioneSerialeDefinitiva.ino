#include "Keypad.h"
#include "Arduino.h"

const byte ROWS = 4; // number of rows
const byte COLS = 4; // number of columns
const int trigPin = 9;  
const int echoPin = 10;
const int ledPin = 11;

bool distanceReached=false;
float duration, distance; 

char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

String strToSend="";

byte rowPins[ROWS] = {8, 7, 6, 5}; // row pinouts of the keypad R1 = D8, R2 = D7, R3 = D6, R4 = D5
byte colPins[COLS] = {4, 13, 12, 2};    // column pinouts of the keypad C1 = D4, C2 = D3, C3 = D2
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS,COLS);

void setup()
{
  pinMode(trigPin, OUTPUT);  
	pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT); 
  Serial.begin(9600);
}
 
void loop()
{
  digitalWrite(trigPin, LOW);  
	delayMicroseconds(2);  
	digitalWrite(trigPin, HIGH);  
	delayMicroseconds(10);  
	digitalWrite(trigPin, LOW); 
  duration = pulseIn(echoPin, HIGH);  
  distance = (duration*.0343)/2;
  delay(100);  
  if(distance < 10)
  {
    distanceReached = true;
    digitalWrite(ledPin,HIGH);
    Serial.println("camera");
  }
  while(distanceReached)
  {
    char customKey = customKeypad.getKey();
  
    if (customKey){
      if(customKey!='*')
      {
        strToSend.concat(customKey);
      }
      else   
        Serial.println(strToSend);
    }
  }
  
}