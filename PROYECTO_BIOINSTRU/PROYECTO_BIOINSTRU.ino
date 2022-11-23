int i;
void setup() {
  Serial.begin(9600);
  i = 0;
}

void loop() {
  /*
    Esto es para generar valores aleatorios y probar el código de python
  */
  Serial.print(random(1,7));

  /*
    Esto es para probar la lectura del voltaje en el pin analógico
  */
  //double sensorValue = analogRead(A0);
  //sensorValue=sensorValue*5/1023;
  //Serial.println(sensorValue);

  delay(500);
}
