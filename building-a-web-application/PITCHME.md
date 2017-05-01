## Building a Wep Application
##### IoT in Africa | 2017
![Building a Web Application](/assets/img/flask-600.png)

---
## What's a Web Application
* One where you use a Web Browser :)

---
## Let's build one!
* Flask is a *Container*

```sh
sudo pip install Flask
```

+++
## Let's build one!
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

* http://127.0.0.1:5000/

+++
## Let's build one!
* Add another *route*

```python
@app.route('/whereami')
def whereami():
    return 'Koforidua!'
```

* http://127.0.0.1:5000/whereami

---
## Go play!
![Hack](/assets/img/hack-600.png)