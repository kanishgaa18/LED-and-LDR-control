int ledPin = 13; 

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT); 
}

void loop() {
  if(Serial.available())
  {
    String s = Serial.readString();
    if(s == "1")
    {
      digitalWrite(ledPin,HIGH);
    }
    else if (s == "0") {
        digitalWrite(ledPin, LOW);  
    }
    else {
      Serial.println("Invalid command. Send '1' or '0'.");
    }
  } 
}
