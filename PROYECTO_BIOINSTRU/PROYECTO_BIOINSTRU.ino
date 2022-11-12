int i;
void setup() {
  Serial.begin(9600);
  i = 0;
}

void loop() {
  Serial.print(random(1, 3));
  delay(500);
}
