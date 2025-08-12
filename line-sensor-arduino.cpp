int mr1 = 8;  // motor right 1
int mr2 = 9;  // motor right 2
int ml1 = 10;  // motor left 1
int ml2 = 11; // motor left 2
int sr = 6;   // sensor right
int sl = 7;   // sensor left
int svr = 0; // sensor value of right sensor
int svl = 0; // sensor value of left sensor
int led = 13; // LED
int enr = 3; // pmw pin for right motors
int enl = 5; //pmw pin for left motors

int vspeed = 100; //
int tspeed = 255;
int tdelay = 5;

void setup() {
  pinMode(mr1,OUTPUT);
  pinMode(mr2,OUTPUT);
  pinMode(ml1,OUTPUT);
  pinMode(ml2,OUTPUT);
  pinMode(led,OUTPUT);
  pinMode(sr,INPUT);
  pinMode(sl,INPUT);
  
 delay(5000);
}

void loop() {
 svr = digitalRead(sr);
 svl = digitalRead(sl);
  
  if (svl==LOW && svr==LOW) {
  forward(); // moves motor forward
  }

  if (svl==HIGH  && svr==LOW) {
  left(); //  moves motor to the left
  }
 
  if (svl==LOW && svr==HIGH) { 
  right(); // moves motor to the right
  }
  
  if (svl==HIGH && svr==HIGH) {
  stop(); // stops motor if no line detected
  }
}

void forward() {
  // Adjust right motors
  digitalWrite(mr1,HIGH);
  digitalWrite(mr2,LOW);

  // Adjust left motors
  digitalWrite(ml1,HIGH);
  digitalWrite(ml2,LOW);

  // Adjust speed
  analogWrite(enr,vspeed);
  analogWrite(enl,vspeed);
} 

void backward() {
  // Adjust right motors
  digitalWrite(mr1,LOW);
  digitalWrite(mr2,HIGH);

  // Adjust left motors
  digitalWrite(ml1,LOW);
  digitalWrite(ml2,HIGH);

  // Adjust speed
  analogWrite(enr,vspeed);
  analogWrite(enl,vspeed);
}

void right() {
  // Adjust right motors
  digitalWrite(mr1,LOW);
  digitalWrite(mr2,HIGH);

  // Adjust left motors
  digitalWrite(ml1,HIGH);
  digitalWrite(ml2,LOW);

  // Adjust speed
  analogWrite(enr,tspeed);
  analogWrite(enl,tspeed);
  
  delay(tdelay); // waits for some time for motor
} 

void left() {
  // Adjust right motors
  digitalWrite(mr1,HIGH);
  digitalWrite(mr2,LOW);

  // Adjust left motors
  digitalWrite(ml1,LOW);
  digitalWrite(ml2,HIGH);

  // Adjust speed
  analogWrite(enr,tspeed);
  analogWrite(enl,tspeed);
  
  delay(tdelay); // waits for some time for motor
}  

void stop() {
  // makes speed 0 on both motor
  analogWrite(enr,0);
  analogWrite(enl,0);
}
