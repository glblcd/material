## Web APIs
##### Global Code | 2018
![Web APIs](/assets/img/weather-512.png)
Note:
In this topic we begin by investigating the weather together. It's a great place to start: the weather is variable, different across regions, has a dramatic effect on our life.

---
## What's the weather like?
* It's July!
* Probably quite nice
* Look out the window
Note:
How do we know what the weather's like? How do we know what it's like in Accra? Watch TV weather, ask a website, ask your phone. How do those things know? Well, there are sensors in different places. What do those sensors do? Rain, temperature, wind. Every so often they "report back", add a line to a database, whatever.

+++
## What's the weather like?
* Why do we care?
  * How do I dress?
  * How do I get to work?
  * Are my plants healthy?
  * Will my house flood?

+++
## What's the weather like?
* How did mum & dad find out?
  * Radio?
Note:
Before the internet, weather reports would be on the radio, in the newspapers etc. Also, you'd know when the rainy season was coming (March-April until November). If the rain didn't come, you're out of luck. Technology has allowed us to improve weather prediction through modelling and analysis. In addition, technology protects us from the effects of the environment: [Hydroponics](https://en.wikipedia.org/wiki/Controlled-environment_agriculture) and 3D, computer-controlled farming allows us to grow plants regardless of the weather outside.

+++
## What's the weather like?
* What about now?!
  * weather.com
  * "hey, Siri..."
Note:
Try these out! Services like these aggregate weather data from physical stations located around the world to show the way things are right now. In addition, they use computer modelling, analysis and prediction to attempt to predict the weather in the hours, days and months from now. These tasks use some of the most powerful computers in the world: http://www.metoffice.gov.uk/news/in-depth/supercomputers

---
## Let's build it!
* http://openweathermap.org/
  * get an API key
* pyOWM
  * `pip install pyowm`
Note:
OpenWeatherMap gives us a way to get weather data from a computer program, via an API ("Application Programming Interface"). This is a library that provides weather data in our program, by connecting to OpenWeatherMap over the internet.

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

---
## Go play!
![Hack](/assets/img/hack-600.png)

+++
##Go play!
* What's the humidity in Hong Kong?
  * Is that worse than here?
* What's the temperature in Tokyo?
* What's the highest city you can find?
  * What's the air pressure there?
* What's the windspeed in Koforidua?

---
## Real world data
* A bunch of sensor data
* Geographically distributed
* Somehow it gets into apps
* What kinds of data can you think of?
Note:
The answer is - anything you can count or measure! Cars waiting at an intersection, people crossing a bridge, air quality, sunset time, biscuit sales, etc etc. How would you measure or count each of these? Can it be done automatically? What's the cost of manual vs automatic?

+++
## Real world data
* How can we tell how sunny it is?
  * Light sensor & polling
  * What do we do with the numbers?
Note:
Here, we play a quick game. We nominate one student as the "data store" and the others have to collect the temperature data from the highest city they found. Eveyone writes the place name and temperature on a piece of paper and hands it to the data store. We can then find out the temperature in any of those cities. We've invented the key-value pair!

---
## Stored data
* Key-value pairs
* "How sunny is it in Accra?"
  * What's the key?
Note:
Now, let's add the *humidity* in those cities. What's the problem, and how do we overcome it?

+++
## Stored data
* Where can we keep it?
* How can we get it back?
Note:
We could keep this data in memory - remember Python's `dictionary` type? - or store it in a database for easy look-up.

---
## Break!
![Break](/assets/img/pause-256.png)
Note:
This is a good chance to check out openstreetmap.org!

---
## Web APIs
How do I request data on the web?
Note:
"Requesting data" could simply mean looking at a webpage. What happens when we do that? We type in a web address, which contains both the domain and the path. Our browser queries a DNS server, which translates the domain name to an IP address. We then directly request the rest of the path from the server addressed by the IP address.

+++ 
## Web APIs
How do I *PUSH* data on the web?
* ...like in a form
* POST
Note:
Here we can use the Network tab in Chrome's developer screen to investigate the various GET requests that the browser sends when we browse to a webpage. Try to submit a form over HTTP and see the POST data being sent, too.

+++
## Web APIs
It's called REST
* *RE*presentational *S*tate *T*ransfer
* We can use HTTP
  * To *request* with *GET*
  * To *update* with *POST*

---
## Break!
![Break](/assets/img/pause-256.png)
Note:
Catch up on your labs!

---
## REST
~~~~
GET  /customers
GET  /customer/3213
POST /customer {*something*}
~~~~

+++
## REST
* What does the data look like?
  * What's its *format*

+++
## REST
JSON?
* *Javascript* Object Notation
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
...
```

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