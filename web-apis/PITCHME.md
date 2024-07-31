## Web APIs
##### Global Code | 2024
![Web APIs](/assets/img/weather-512.png)

In this topic we begin by investigating the weather together. It's a great place to start: the weather is variable, different across regions, has a dramatic effect on our life.

It's fun to present some slides, then drop into the terminal and write some code, then take it to the board and diagram out what just happened - how does your computer know what the weather's like in Tampa FL? For that matter - how does the web service? You can talk about all kinds of things here - databases, sensor arrays, polling vs push...

---
## What's the weather like?
* It's August!
* Probably quite nice
* Look out the window


How do we know what the weather's like? How do we know what it's like in Accra? Watch TV weather, ask a website, ask your phone. How do those things know? Well, there are sensors in different places. What do those sensors do? Rain, temperature, wind. Every so often they "report back", add a line to a database, whatever.


## What's the weather like?
* Why do we care?
  * How do I dress?
  * How do I get to work?
  * Are my plants healthy?
  * Will my house flood?
* How did mum & dad find out?
  * Radio?

Before the internet, weather reports would be on the radio, in the newspapers etc. Also, you'd know when the rainy season was coming (March-April until November). If the rain didn't come, you're out of luck. 

Technology has allowed us to improve weather prediction through modelling and analysis. In addition, technology protects us from the effects of the environment: [Hydroponics](https://en.wikipedia.org/wiki/Controlled-environment_agriculture) and 3D, computer-controlled farming allows us to grow plants regardless of the weather outside.

## What's the weather like?
* How do we find out about the whether now?
  * weather.com
  * "hey, Siri..."

Services like these aggregate weather data from physical stations located around the world to show the way things are right now. In addition, they use computer modelling, analysis and prediction to attempt to predict the weather in the hours, days and months from now. 
These tasks use some of the most powerful computers in the world: http://www.metoffice.gov.uk/news/in-depth/supercomputers

## Let's build it!
* http://openweathermap.org/
  * Make an account using your email
  * Go to [API keys](https://home.openweathermap.org/api_keys) to get an API key once logged in
* pyOWM
  * `pip install pyowm`

OpenWeatherMap gives us a way to get weather data from a computer program, via an API `"Application Programming Interface"`. 

This is a library that provides weather data in our program, by connecting to OpenWeatherMap over the internet.

## Let's build it!
```python
import pyowm

owm = pyowm.OWM('{API-KEY}')
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()

w.get_wind()
w.get_humidity()
```

## Go play!
![Hack](/assets/img/hack-600.png)

* What's the humidity in Hong Kong?
  * Is that worse than here?
* What's the temperature in Tokyo?
* What's the highest city you can find?
  * What's the air pressure there?
* What's the windspeed in Koforidua?

Note:

Here's some more questions for the students to answer in their pairs. Leave the slide up on the projector while they play around and find the answer.

---
## Real world data
* A bunch of sensor data
* Geographically distributed
* Somehow it gets into apps
* What kinds of data can you think of?

The answer is - anything you can count or measure! Cars waiting at an intersection, people crossing a bridge, air quality, sunset time, biscuit sales, etc etc.

* How would you measure or count each of these? 
* Can it be done automatically? 
* What's the cost of manual vs automatic?

This is a great chance to let the students really ideate about WHAT they can build - now they're starting to understand the pieces of the puzzle. 

* How can we tell how sunny it is?
  * Light sensor & polling
  * What do we do with the numbers?


Here, we play a quick game. We nominate one student as the "data store" and the others have to collect the temperature data from the highest city they found. Eveyone writes the place name and temperature on a piece of paper and hands it to the data store. We can then find out the temperature in any of those cities. We've invented the key-value pair!

---
## Stored data
* Key-value pairs
* "How sunny is it in Accra?"
  * What's the key?

Now, let's add the *humidity* in those cities. What's the problem, and how do we overcome it? Well, you extend the key :)

## Stored data
* Where can we keep it?
* How can we get it back?

We could keep this data in memory - remember Python's `dictionary` type? - or store it in a database for easy look-up.

---
## Break!
![Break](/assets/img/pause-256.png)

Note:
This is a good chance to check out openstreetmap.org!

---
## Web APIs

What we've been doing so far is exploring weather conditions using the weather API.
Before we proceed with exploring even more APIs, let's take some time to discuss important theory and terminology.

* What does API stand for?
* What is an API?
* What are some API examples? What APIs do we use everyday?
  * A good time to interact with the students again in this section using different questions

API is the acronym for `application programming interface` — a software intermediary that allows two applications to talk to each other. APIs are an accessible way to extract and share data within and across organizations.

The application or service that accesses resources is the `client`, and the application or service that contains the resource is the `server`.

APIs are all around us. Every time you use the uber app, send a mobile payment, post something on instagram, send an email, or change the thermostat temperature from your phone, you’re using an API.

When you use one of the above apps, they connect to the Internet and send data to a server. The server then retrieves that data, interprets it, performs the necessary actions, and sends it back to your phone. The application then interprets that data and presents you with the information you wanted in a readable way. 

---
How do I request data on the web?

"Requesting data" could simply mean looking at a webpage.

 What happens when we do that? We type in a web address, which contains both the domain and the path. Our browser queries a DNS server, which translates the domain name to an IP address. We then directly request the rest of the path from the server addressed by the IP address.

Now could be a good time to ask the students to open any webpage and  the Network tab in Chrome's developer screen to check the requests going out and the different characteristics they have. 

Some of those we will explore in this lesson soon.

What are some examples of requesting data over an API?
* requesting weather data
* loading your latest unread emails
* refreshing your feed on instagram to get the latest
* what else?

We have spoken about requesting data, but APIs are much stronger that just that.

How do I *PUSH* data on the web?
* ...like in a form
* POST

## Web APIs
It's called REST, `REpresentational State Transfer`

REST is a set of architectural constraints, commly applied when using HTTP as the transport protocol.

REST APIs communicate through HTTP requests to perform standard functions like creating, reading, updating and deleting records (also known as CRUD) within a resource.

A REST API would use: 
* a GET request to retrieve a record
* a POST request creates a new record
* a PUT request updates a record
* a DELETE request deletes one.

The state of a resource at any particular instant, or timestamp, is known as the resource representation. This information can be delivered to a client in virtually any format including JavaScript Object Notation (JSON), HTML, Python, or plain text. JSON is popular because it’s readable by both humans and machines—and it is programming language-agnostic.

Nowe we can go back to the Network tab and ask students to identify more characteristics of the requests they are seeing? 
Which verb? What about headers?
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
---
## Break!
![Break](/assets/img/pause-256.png)
Note:
Catch up on your labs!


## REST
Let's build it!
```python
from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID={APIKEY}')
pprint(r.json)
```

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

Note:

So now we've shown the two layers that the request works at - at the high level, using a rich, schema-aware API which keeps our code clean and interprets the web response, and at the lower level, using a simple HTTP GET with a specially-formatted URL and interpreting the JSON ourselves.

This is a great chance to talk about layered architecture, data formats, building APIs etc.

# REST API best practices

As a software developer, you are almost guaranteed to work with or build APIs at some point in your career.

Although flexibility is a big advantage of REST APIs, that same flexibility makes it easy to design an API that’s broken or performs poorly. For this reason, developers share best practices in `REST API specifications`.

Having the ability to provide a definition of your API to other people – your colleagues, companies you partner with or organizations who you provide APIs to – is vital to building quality APIs.

API specification languages provide a standardized means to do this.
Your APIs can be described in agnostic terms, decoupling them from any specific programming language. 
Consumers of your API specification do not need to understand the guts of your application or try to learn Lisp or Haskell if that’s what you chose to write it in. They can understand exactly what they need from your API specification, written in a simple and expressive language.

`The OpenAPI Specification (OAS) enables exactly this transfer of knowledge from API provider to API consumer.`

Swagger was the original implementation of the OpenAPI specification but the industry and most tooling has now converged to use OpenAPI.

What is the OpenAPI specification?
* it is an open standard for describing your APIs
* allows us to provide an API specification encoded in a JSON or YAML document
* it provides a comprehensive dictionary of terms that reflects commonly-understood concepts in the world of APIs
  * available endpoints
  * allowed operations
  * parameters
  * authentication methods and much more

Now it's a good time to point students to the OpenAPI initiative, https://www.openapis.org/ .

Let them explore the tools available, ask them to play with the Swagger Editor, https://editor.swagger.io/.
What characteristics of an API do they see documented in a specification?

---
## What next?
* The Stars!
  * https://www.programmableweb.com/api/star

---
## Go play!
![Hack](/assets/img/hack-600.png)