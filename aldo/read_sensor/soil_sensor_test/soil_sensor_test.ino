const int MOISTURE_PIN = 0;    // Pin to read soil sensor
const int TEMP_PIN = 1;    // Pin to read soil sensor
float m_volt;
float t_volt;

void setup() {

  Serial.begin(115200);  // Initialize Serial for debuging purposes.
}

void loop() {      
  m_volt = analogRead (MOISTURE_PIN) * 1000;
  t_volt = analogRead (TEMP_PIN) * 1000;

  Serial.print(m_volt);
  Serial.print(",");
  Serial.println(t_volt);

  delay(1000);

}