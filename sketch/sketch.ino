


void setup() {
  // put your setup code here, to run once:
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  Serial.begin(9600);
}


char in[2];

void loop() {
  checkBoxies();
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