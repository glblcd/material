## MQTT
##### Global Code | 2019
![MQTT](/assets/img/mqtt.png)

---

## How do systems communicate?
* Web: browser -> server
* Email: sender -> receivers
* Chat: senders -> receivers
* ...?

+++

## How do systems communicate?
* How do they know *how* to communicate?
  * Data formats
  * Protocols

---

## Pub/Sub
One common pattern for communication
* One "Publisher"
* Many "Subscribers"

---

## Publisher
* Sends messages
* Just plain text
  * You decide the protocol
  * And the data format!

---

## Subscriber
* Subscribes to topics
  * Like a chat room
  * Can subscribe more than once
* Publisher can also subscribe!

+++

## How do I use it
* Firstly we'll use mosquitto
  * You installed it last week
  * sudo apt-get install mosquitto mosquitto-clients

Note:

Here, you should get the mqtt server details and run the wildcard subscriber on the big screen
Tell the students how to subscribe to topics - for example, their name, and how they can send messages either to the screen or each other. This is usually pretty wild so let them have fun & make sure everyone is working before you move on:

mosquitto_sub -t test/all -h \<hostname\>.com
mosquitto_pub -t test/all -h \<hostname\>.com -m "Hello Class!"

+++
## Go play!
![Hack](/assets/img/hack-600.png)

---

## How do I use it in code?
* A python library called paho
  * pip install paho-mqtt

+++
## Go play!
![Hack](/assets/img/hack-600.png)

Note:

Paho is very well documented and our use right now is very simple:
https://pypi.org/project/paho-mqtt/

A nice thing to do here is just write out the code yourself, and have the class type along with you. Stop regularly to talk about what you're doing:
 * What's the difference between `pip install paho-mqtt` and `import paho.mqtt.client as mqtt`?
 * What's the difference between client.on_connect = on_connect and on_connect()?
 * Why do we set up the callbacks before we connect?
 * Why do we loop_forever?

