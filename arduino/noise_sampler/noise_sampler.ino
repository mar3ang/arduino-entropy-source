const int noisePin = A0;

void setup() {
    Serial.begin(115200);
}

void loop() {
    int sample = analogRead(noisePin);

    Serial.println(sample);

    delayMicroseconds(100);
}