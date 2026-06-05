// This is the arduino sketch for reading analog noise -  it is not ran in this program (VS Code). This is a copy of the cde that is being send to the Arduino itself. 

void setup() {
  Serial.begin(115200);
  Serial.println("START"); // this part will not be displayed in the data files since it was created simply for my convinience
}

void loop() {
  int v = analogRead(A0);
  Serial.println(v);
  delay(5); // this is the delay between each reading, it can be adjusted to increase or decrease the number of samples per millisecond. Currently it is 5 microseconds, which means we are taking 200 samples per second (1000 ms / 5 ms = 200 samples/s). Hence, for us to have 10000 samples, it will take approximately 50 seconds (10000 samples / 200 samples/s = 50 seconds).
}
