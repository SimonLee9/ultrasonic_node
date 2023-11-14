#define TRIG_PIN1 9
#define ECHO_PIN1 8
#define TRIG_PIN2 10
#define ECHO_PIN2 11

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN1, OUTPUT);
  pinMode(ECHO_PIN1, INPUT);
  pinMode(TRIG_PIN2, OUTPUT);
  pinMode(ECHO_PIN2, INPUT);
}

void loop() {
  long duration1, distance1;
  long duration2, distance2;
  
  digitalWrite(TRIG_PIN1, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN1, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN1, LOW);
  duration1 = pulseIn(ECHO_PIN1, HIGH);
  distance1 = duration1 * 0.034 / 2;
  Serial.print(distance1);
  Serial.print(",");  // 구분자 추가

  digitalWrite(TRIG_PIN2, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN2, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN2, LOW);
  duration2 = pulseIn(ECHO_PIN2, HIGH);
  distance2 = duration2 * 0.034 / 2;
  Serial.println(distance2);

  delay(500);  // 적절한 딜레이 설정
}
