/*
Wireless switch that allows users to control the smart bulbs in the system with MQTT, 
see the light levels on thingspeak, to collect and analyze data from the smart bulbs.  
Will also measure the light intensity, to show a relation between when the bulbs were used and 
the amount of light in the day that was present
*/

import dotenv from 'dotenv'
dotenv.config()

ESP8266_IoT.MqttEvent("turn_on_first_bulb", ESP8266_IoT.QosList.Qos0, function (message) {
    if ("turn_on_first_bulb" == message) {
        basic.showLeds(`
            # # # # .
            # # # # .
            # # # # .
            # # # # .
            # # # # .
            `)
    }
 })

 let lightLevel = 0
 pins.digitalWritePin(DigitalPin.P1, 0)
 basic.showIcon(IconNames.Heart)
 ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
 ESP8266_IoT.connectWifi(process.env.WIFI_USERNAME, process.env.WIFI_PASSWORD)

 if (ESP8266_IoT.wifiState(true)) {
    basic.showIcon(IconNames.Happy)
 } else {
    basic.showIcon(IconNames.Sad)
 }

 ESP8266_IoT.setMQTT(
    ESP8266_IoT.SchemeList.TLS,
    process.env.MQTT_CLIENT_ID,
    process.env.MQTT_USERNAME,
    process.env.MQTT_PASSWORD,
    ""
 )

 ESP8266_IoT.connectMQTT(process.env.MQTT_CLUSTER_ID, 8883, false)
 basic.forever(function () {
    lightLevel = Environment.ReadLightIntensity(AnalogPin.P1)
    ESP8266_IoT.connectThingSpeak()
    ESP8266_IoT.setData(
    process.env.THINGSPEAK_API_KEY,
    lightLevel
    )
    ESP8266_IoT.uploadData()
 })
 