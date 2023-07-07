import processing.serial.*;
Serial outSerial;  // Create object from Serial class
String read;     // Data received from the serial port
PrintWriter output; // Output file

void setup() {
  outSerial = new Serial(this, Serial.list()[1], 115200);
  output = createWriter("data_1sec_soil_temp.csv");
}

void draw() {
    if (outSerial.available() > 0 ) {
         read = outSerial.readString();
         if (read != null ) {
              output.print(read);
         }
    }
}

void keyPressed() {
    output.flush();  // Writes the remaining data to the file
    output.close();  // Finishes the file
    exit();  // Stops the program
}
