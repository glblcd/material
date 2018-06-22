## Hosting Platforms
##### Global Code | 2018
![Hosting Platforms](/assets/img/heroku-733x258.png)

Note:
This is a great course for teaching in the platonic method - 
each stage results in a series of questions which are answered
in the next stage. Feel free to dip in & out of the slides, or
not use them at all. The ultimate answer, of course, is heroku ;)

The lab for this section is to get the students webapp running on
Heroku - so you could even do that *first* to introduce the motivation.

---
## Where does our code run?
```python mything.py```

locally?

---
## My machine
* Where everything starts!
* Who can access that?
* What happens if hardware breaks?

Note:
The points to introduce here are that
* local dev is fine
* probably good for dev and not hosting
* our local machine probably has a bunch of cruft on it
* We're responsible for fixing hardware etc.

+++
## My machine
* How can people use the stuff I build?
* What if I write something for a client?
  * Where should I *put it*?

---
## Web Hosting
```http://www.foobar.com/mything```
* some web hosting provider?
* My stuff is on the *internet*
  * ...has a public IP address
  * DNS maps to a *name*

+++
## Web Hosting
What happens if
* a disk fails?
* it works on my machine...

+++
## Web Hosting
Who's responsible for
* Upgrading python?
* Applying server patches?

+++
## Web Hosting
Library version upgrades?
* `sudo pip install foo`
* Who has the admin password?

+++
## Web Hosting
* Who owns the machine?
  * Mine: $$$
  * Shared: $
* I'm probably not maximising resource use

---
## Virtual servers
Shared machine
* It *looks* like mine
* Saves some $$$
* Can grow/shrink GHz,RAM,HDD with use

+++
## Virtual servers
I can install what I want
* Same problems!

+++
## Virtual servers
Wouldn't it be cool if I could just *say* what I wanted?
* "64-bit RHEL with 72GB Ram, 2TB HDD please"
```34.123.72.159```

---
## Containers
"I need python running on linux, with flask, requests and SQLAlchemy installed,
plus a postgreSQL database."

