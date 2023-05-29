
long AnalogData_1[3];
long AnalogData_2[3];

void setup() {
  // put your setup code here, to run once:
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(A4, INPUT);
  pinMode(A6, INPUT);
  Serial.begin(9600);
  AnalogData_1[0] = 1;
  AnalogData_2[0] = 2;
}

unsigned long last_print1;
unsigned long last_print2;
char in[2];

void loop() {
  checkBoxies();
  if (millis() - last_print1 >= 10) {
    AnalogData_1[1] = millis(); AnalogData_1[2] = analogRead(A4);
    Serial.print(AnalogData_1[0]); Serial.print(';'); Serial.print(AnalogData_1[1]);  Serial.print(';'); Serial.println(AnalogData_1[2]); 
    last_print1 = millis();
  }
  //if (millis() - last_print2 >= 10) {
  //  AnalogData_2[1] = millis(); AnalogData_2[2] = analogRead(A6); 
  //  Serial.print(AnalogData_2[0]); Serial.print(';'); Serial.print(AnalogData_2[1]);  Serial.print(';'); Serial.println(AnalogData_2[2]);
  //  last_print2 = millis();
  //}
}




void checkBoxies() {
    if (Serial.available() > 0) {
    Serial.readBytes(in, 2);
    switch (in[0]) {
      case 4:
        switch (in[1]) {
          case 1: digitalWrite(4, 1); break;
          case 0: digitalWrite(4, 0); break;
        } break;
      case 5:
      switch (in[1]) {
          case 1: digitalWrite(in[0], HIGH); break;
          case 0: digitalWrite(in[0], LOW); break;
        } break;
      case 6:
      switch (in[1]) {
          case 1: digitalWrite(in[0], HIGH); break;
          case 0: digitalWrite(in[0], LOW); break;
        } break;
      case 7:
      switch (in[1]) {
          case 1: digitalWrite(in[0], HIGH); break;
          case 0: digitalWrite(in[0], LOW); break;
        } break;
    }
  }
}