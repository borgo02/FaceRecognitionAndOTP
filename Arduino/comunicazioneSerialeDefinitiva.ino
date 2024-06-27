#include "Keypad.h"
#include "Arduino.h"

const byte ROWS = 4; // number of rows
const byte COLS = 4; // number of columns
const int trigPin = 9;  
const int echoPin = 10;
const int ledPin = 11;
const int ledPin_1 = 1;

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
String OstrToSend="";
String strReceived="";

byte rowPins[ROWS] = {8, 7, 6, 5}; // row pinouts of the keypad R1 = D8, R2 = D7, R3 = D6, R4 = D5
byte colPins[COLS] = {4, 13, 12, 2};    // column pinouts of the keypad C1 = D4, C2 = D3, C3 = D2
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS,COLS);

void setup()
{
  pinMode(ledPin_1, OUTPUT);
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
      Serial.println("s:1");
      stato = 1;
    }
  }
  else if(stato == 1){
    strReceived=readSerial();
    if(strReceived == "stato_1"){
      stato=2;
    }
    else if(strReceived == "stato_3"){
      stato=3;
    }
    else if(strReceived == "stato_4"){
      stato=2;
    }
  }
  else if(stato == 2){
    char customKey = customKeypad.getKey();
    if (customKey){
      if(customKey!='*')
      {
        strToSend.concat(customKey);
      }
      else   
      {
        OstrToSend.concat(strToSend);
        Serial.println(OstrToSend);
        stato = 1;
      }
    }
  }
  else if(stato == 3){
    digitalWrite(ledPin_1, HIGH);
  }
  else if(stato == 4){
    digitalWrite(ledPin_1, HIGH);
    delay(1500);
    digitalWrite(ledPin_1, LOW);
    stato=2;
  }
}

String readSerial(){
  String serialStr="";
  if(Serial.available()){
    do {
      if(Serial.available()) {
        c = Serial.read();
        serialStr+= c;
      }
    }while(c != '\n');
  }
  return serialStr;
}


