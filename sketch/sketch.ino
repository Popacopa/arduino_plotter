void setup() {
  // put your setup code here, to run once:
  pinMode(4, OUTPUT);
  Serial.begin(9600);
}
char in[2];
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    Serial.readBytes(in, 2);
    Serial.print(in[0]);Serial.println(in[1]);
    //switch (in[1]){
      //case 0: digitalWrite(4, LOW);
        //break;
      //case 1: digitalWrite(4, HIGH);
        //break;
  }
  
   
}
