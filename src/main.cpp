#include <DHT.h>

#define DHTPIN1 15     // Primeiro Sensor
#define DHTPIN2 4      // Segundo Sensor
#define DHTTYPE DHT22  

DHT dht1(DHTPIN1, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht1.begin();
  dht2.begin();
}

void loop() {
  float temp1 = dht1.readTemperature();
  float hum1 = dht1.readHumidity();

  float temp2 = dht2.readTemperature();
  float hum2 = dht2.readHumidity();

  Serial.println("Sensor 1:");
  Serial.print("Temperatura: ");
  Serial.print(temp1);
  Serial.print(" C  |  Umidade: ");
  Serial.print(hum1);
  Serial.println(" %");

  Serial.println("Sensor 2:");
  Serial.print("Temperatura: ");
  Serial.print(temp2);
  Serial.print(" C  |  Umidade: ");
  Serial.print(hum2);
  Serial.println(" %");

  Serial.println("-------------------------");

  delay(3000);  // Aguarda 3 Segundos
}
