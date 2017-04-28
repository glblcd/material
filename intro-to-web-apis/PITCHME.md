## Web APIs: Intro
##### IoT in Africa | 2017
![Introduction to Web APIs](/assets/img/weather-512.png)

---
## What's the weather like?
* It's July!
* Probably quite nice
* Look out the window

+++
## What's the weather like?
* weather.com
* "hey, Siri..."

---
## Let's build it!
* http://openweathermap.org/
  * get an API key
* pyOWM
  * `pip install pyowm`

+++?gist=f70758637687408b77c27e7f61acf850

---
## Go play!
![Hack](/assets/image/hack-600.png)

---
## Real world
* A bunch of sensor data
* Geographically distributed
* Somehow it gets into apps

+++
## Real world
* How can we tell how sunny it is?
* Light sensor & polling
* What do we do with the numbers?

---
## Stored data
* Key-value pairs
* "How sunny is it in Accra?"
* What's the key?

+++
## Stored data
* How can I get at it?
  * Connect to the database
  * Problems?

+++
## Stored data
* How else?
  * Build an API!
  * Request / Response

---
## Web APIs
How do I usually request data on the web?

+++
## Web APIs
```sh
$ telnet telnet koforiduapoly.edu.gh 80↵
Trying 96.127.180.162...
Connected to koforiduapoly.edu.gh.
Escape character is '^]'.
GET / HTTP/1.1↵
↵
```

+++ 
## Web APIs
How do I *PUSH* data on the web?
* ...like in a form
* POST

+++
## Web APIs
It's called REST
* *RE*presentational *S*tate *T*ransfer
* We can use HTTP
  * To *request* with *GET*
  * To *update* with *POST*

---
## REST
```
GET  /customers
GET  /customer/3213
POST /customer
```
+++
## A vertical slide has the same title as its initial HSLIDE
And contains additional information
```python
def maybeSomeCode():
    okay()
```