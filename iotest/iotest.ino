int const HIGH_THRESHOLD = 600;
int sensorPin = A0;
int transmitterPin = 2;
short recData [400];
int errors = 0;
int i = 0;

void setup() {
    Serial.begin(115200);
    pinMode(transmitterPin, OUTPUT);
    pinMode(sensorPin, INPUT);
    digitalWrite(transmitterPin, 1);
    delay(500);
}

void loop() {
    Serial.println(analogRead(sensorPin));
}
