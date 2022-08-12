const int SENSOR_PIN = A3;    // Pin to read soil sensor
float percentFC;
int volt = 0;

const int dryVoltage = 0;           //  output in air, dry     
const int midVoltage = 1650;           // output at midpoint between wet and dry, or 50% water depth
const int wetVoltage = 3330;           // output in well watered soil  or submerged in water
void setup() {
  Serial.begin(115200);  // Initialize Serial for debuging purposes. 
}
 
void loop() {      
 volt = analogRead (SENSOR_PIN);
 // convert % field capacity or full scale range, w/ 3-pt calibration
 if (volt < midVoltage)                 
   { percentFC=map(volt,wetVoltage,midVoltage,50,0); 
   Serial.print ("Dry soil(mV)        ");
   //Serial.print(percentFC);
   Serial.print("        ");
   Serial.println (volt);
   }
 else {
   Serial.print ("Wet soil(mV)        ");
   percentFC=map(volt,midVoltage,dryVoltage,100,50);
   //Serial.print (percentFC);
   Serial.print("        ");
   Serial.println (volt);
      }
   delay(1000);   
 }