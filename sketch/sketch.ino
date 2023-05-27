void setup() {
  // put your setup code here, to run once:
  pinMode(4, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    switch (Serial.read()){
      case ')': digitalWrite(4, LOW);
        break;
      case '(': digitalWrite(4, HIGH);
        break;
  }
  }
   
}
