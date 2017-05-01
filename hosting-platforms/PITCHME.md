## Building a Wep Application
##### IoT in Africa | 2017
![Building a Web Application](/assets/img/flask-600.png)

---
## What's a Web Application
* One where you use a Web Browser :)
* Your code exists on a web server

Note:
At this point, it's a good idea to draw out the box diagrams:
  * One server, many clients making requests against it
  * Students should already know a little HTTP
  * Keep the diagram on a whiteboard & refer back to it through the session
---
## Let's build one!
* Flask is a web server
  * ...and other things
  * for Python
  * there are others (e.g. Django)

```sh
sudo pip install Flask
```

Note:
By now, students should be familiar with pip, but worth going over again

+++
## Let's build one!
`myapp.py`:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

`python myapp.py`:
*  http://127.0.0.1:5000/

Note:
Get the students to do this, right now. Then, when most are on their way,
you can bring up the next slide, then the hack! slide.

+++
## Let's build one!
* Add another *route*

`myapp.py`:
```python
@app.route('/whereami')
def whereami():
    return 'Koforidua!'
```
`python myapp.py`:
* http://127.0.0.1:5000/whereami

---
## Go play!
![Hack](/assets/img/hack-600.png)

---
## Build a homepage
* Make it interactive
* Make it look awesome!

+++
## Build a homepage
`myapp.py`:
```python
from flask import Flask, render_template
@app.route('/')
def index():
    return render_template('index.html')
```
`templates/index.html`:
```html
<html>
    <body>
        <h1>Hello from a template!</h1>
    </body>
</html>
```
Note:
* We've added a new import
* the *templates* directory is convention

+++
## Build a homepage
* Add your own css!
  * create a css file in ```static```
  * add a ```link``` in your html

---
## Go play!
![Hack](/assets/img/hack-600.png)

---
## Make it *dynamic*
`myapp.py`:
```python
from flask import Flask, render_template
@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)
```
`templates/index.html`:
```html
<html>
    <body>
        <h1>Hello, {{to}}!</h1>
    </body>
</html>
```

---
## Go play!
![Hack](/assets/img/hack-600.png)

---
## Make it *look awesome*
* Bootstrap!
https://getbootstrap.com/getting-started/
* google ```bootstrap themes``` && go!