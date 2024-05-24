#include "Keypad.h"
#include "Arduino.h"

const byte ROWS = 4; // number of rows
const byte COLS = 4; // number of columns
const int trigPin = 9;  
const int echoPin = 10;
const int ledPin = 11;

bool distanceReached=false;
float duration, distance; 
int stato = 0;
char c="";

char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

String strToSend="";
String strReceived="";

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
  if(stato == 0){
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
      digitalWrite(ledPin,HIGH);
      Serial.println("A");
      stato = 1;
    }
  }
  else if(stato == 1){
    char customKey = customKeypad.getKey();
    if (customKey){
      if(customKey!='*')
      {
        strToSend.concat(customKey);
      }
      else   
      {
        Serial.println(strToSend);
        stato = 2;
        Serial.println(stato);
      }
    }
  }
  else if(stato == 2){
    if(Serial.available()) {
      do {
        if(Serial.available()) {
          c = Serial.read();
          strReceived+= c;
        }
      }while(c != '\n');
      Serial.println(strReceived);
    }
    if(strReceived == "ciao"){
      Serial.println("ok");
    }
  }
}