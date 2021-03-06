#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 10

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);

void setup(void)
{
  // start serial port
Serial.begin(9600);

  // Start up the library
  sensors.begin();
 
}

void loop(void){
  
sensors.requestTemperatures(); // Send the command to get temperatures 
Serial.print("s");
float x=sensors.getTempCByIndex(0);
Serial.print(x);
Serial.print("e");
Serial.println();
    
}
