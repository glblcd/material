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

+++
## Let's build it!
```python
import pyowm

owm = pyowm.OWM('{API-KEY}')
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()

w.get_wind()
w.get_humidity()
```
<!--
https://stackoverflow.com/questions/1474489/python-weather-api
-->

---
## Go play!
![Hack](/assets/img/hack-600.png)

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
How do I request data on the web?

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
> GET  /customers
> GET  /customer/3213
> POST /customer {*something*}

+++
## REST
* What does the data look like?
  * What's its *format*

+++
## REST
JSON?
* Javascript Object Notation
```javascript
var sam = {
    givenname: "Sam",
    familyname: "Moorhouse",
    DoB: "1984-02-28"
}
sam.familyname // Moorhouse
```

+++
## REST
XML?
* eXtensible Markup Language
```xml
<Person>
    <GivenName>Sam</GivenName>
    <FamilyName>Moorhouse</FamilyName>
    <DoB>1984-02-28</DoB>
</Person>
```

+++
## REST
Let's build it!
```python
from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID={APIKEY}')
pprint(r.json)
```

+++
## REST
```python
{u'base': u'cmc stations',
 u'clouds': {u'all': 68},
 u'cod': 200,
 u'coord': {u'lat': 51.50853, u'lon': -0.12574},
 u'dt': 1383907026,
 u'id': 2643743,
 u'main': {u'grnd_level': 1007.77,
```
...

---
## API
So the *Python* API is a *Layer* on top of the *REST* API
* Lower level = more power, more work?
* Higher level = more meaning, less work?

---
## What next?
* The Stars!
  * https://www.programmableweb.com/api/star

---
## Go play!
![Hack](/assets/img/hack-600.png)