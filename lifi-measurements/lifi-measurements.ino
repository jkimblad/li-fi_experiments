//Header file with bit-array to be transmitted
#include "lifi-measurements.h"

//Constants
int const HIGH_THRESHOLD = 100;
int const DELAY = 50;
int const SENSOR_PIN = A0;
int const TRANSMITTER_PIN = 2;

//Global variables
short recData [400];
int errors = 0;
int i = 0;

//Setup required for arduino
void setup() {
    Serial.begin(115200);
    pinMode(TRANSMITTER_PIN, OUTPUT);
    pinMode(SENSOR_PIN, INPUT);

    delay(1000);

    //Take measurements by transmitting data
    measurements();

    //Calculate the amount of errors after transmission is finished
    errorCalc();
    
    //Print results
    Serial.print("Errors: ");
    Serial.println(errors);
}

//Endless loop required for arduino
void loop() {

}

//Sends the data and saves the received data
void measurements() {
    for(i = 0; i < sizeof(data); i++) {
	digitalWrite(TRANSMITTER_PIN, data[i]);
	delay(DELAY);
	recData[i] = analogRead(SENSOR_PIN);
    }
}

//Calculates the amount of received errors
void errorCalc(){
    errors = 0;
    for(i = 0; i < sizeof(data); i++) {
	if (data[i] == 1) {
	    if (recData[i] < HIGH_THRESHOLD) {
		errors++;
	    }
	} else if (data[i] == 0) {
	    if (recData[i] >= HIGH_THRESHOLD) {
		errors++;
	    }
	}
    }
}

