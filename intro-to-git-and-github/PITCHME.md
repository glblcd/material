## Git and GutHub
##### IoT in Africa | 2017
![Git and Github](/assets/img/git-512.png)
Note:
This is a great piece to do early on because it means you don't have to cargo-cult git into the early teaching sessions, and you can introduce some professional guidance ("use github!") very early in the programme.

There's a mixture of discussion, technical explanation (which can maybe be a bit dry?), and walkthrough which you must do with the class - creating a github account, create a "hello world" project, clone the repo, write some code locally, commit it locally, then push to the github remote. Then browse to github and - hey presto! - your code is right there.

Make sure everyone in the class is keeping up with all the steps. If possible, write them down and keep them at the front of the class as a cheat-sheet for the rest of the programme. Impress upon the class how important it is to use github for *each* project they work on, even small stuff. Show them your own github repo - you're a pro, after all - show them microsoft's, maybe ask them to go find the code for a project they know.

Show how you can use a github project's wiki, issues pages etc.

That's where we leave this topic - branching and merge conflicts will maybe come up later in the programme and you can have an ad-hoc discussion about merges, fast-forwards etc.


---
## How do we share code?
![think](/assets/img/thinking-800.png)
Note:
Let's try and lead a progressive discussion about the problem that a distributed VCS solves:
* What if I make a change and it breaks my code?
  * Ctrl-z
* What if I want to go wayyy back to how things were yesterday?
  * erm...
* How can I share a codebase between two people?
  * a network drive allows sharing, but no resource locking
* So maybe the filesystem isn't the right place for code
  * but it's intuitive, and a good way to lay out code.

---
## We use "git"
* Distributed Version Control
* Built for the linux kernel project
* ...by the linux kernel owner!
   * 19.5 MILLION lines of code
   * ~14000 contributors

+++
## We use "git"
* it's local
  * works with no internet connection!
* *everyone* uses it
  * microsoft, google, US government

---
## Let's install it
![install](/assets/img/debian-500.png)
note:
see who remembers!
$ sudo apt-get install git
run `git` to show some of the commands
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
$ git config --list

---
## Git basics
* Working directory
* Staging area
* .git directory
note:
Draw from https://git-scm.com/book/en/v2/Getting-Started-Git-Basics when you're drawing this out on the board
identify the 'clone', 'add', and 'commit' operations

---
## Let's do it!
![Hack](/assets/img/hack-600.png)
note:
write a simple 'hello world' in Python, have the class work along with you
print "Hello, World!"
git init; git add .; git commit -m "init"
then build it into a function by adding the main sentinel:
def main():
    print "Hello, World!"

if __name__ == "__main__":
    main()
git add .; git commit -m "refactor executed code into a function"

---
## History
* `git log -p`
* `git log --since=2.weeks`

---
## Single-user workflow
```sh
$ git init
[...]
$ git add .
$ git commit -m "added hello world function"
```

Note:
Great, I've got a local repo. Now I can get change history, remember what I was doing & when, even move back to an earlier version (ask the class to find out how!)
But... what if my computer breaks?

---
## Git remotes
* How we collaborate
* slightly different
`git remotes`
`git remote add <shortname> <url>`

Note:
Again, here it's a good time to draw out what a git remote is and how we can use them to collaborate
their local <--> their github remote <--> my github clone <--> my local
            push                 pull request             pull

---
## Using github
* It's a remote!
```sh
$ git add remote origin https://github.com/iotinafrica/material.git
[git add, commit...]
$ git push
```
Note:
Works even without collaboration. Or you can grant someone perms to push to your repo. Or use the pull-request model

+++
## Using github
![go!](/assets/img/github-256.png)
Note:
Run-through with the class
create a github account
create a new project "hello world"
add 'origin' remote to everyone's hello-world project
git push -u origin master

explore fun repos:
https://github.com/chrislgarry/Apollo-11/tree/master/Comanche055
https://github.com/google
