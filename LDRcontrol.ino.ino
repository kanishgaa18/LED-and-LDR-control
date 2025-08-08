int ldrPin = A0;  
int ldrValue = 0; 

void setup() {
  Serial.begin(9600); 
}

void loop() {
  ldrValue = analogRead(ldrPin); 
  Serial.print("LDR Value: ");
  Serial.println(ldrValue); 

  delay(500); 
}
