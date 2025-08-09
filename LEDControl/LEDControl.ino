int ledPin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char s = Serial.read();  // read one character

    if (s == '1') {          // compare with single quotes
      digitalWrite(ledPin, HIGH);
      Serial.println("LED ON");
    }
    else if (s == '0') {     // compare with single quotes
      digitalWrite(ledPin, LOW);
      Serial.println("LED OFF");
    }
    else {
      Serial.println("Invalid command. Send '1' or '0'.");
    }
  }
}
