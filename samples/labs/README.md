# ![Intro to Python: Labs](/assets/img/logo-small.png) Intro to Python: Labs

Welcome to the Python lab! Work through this sheet in pairs, making sure that you understand
each bit of code before you move on.

If you get something wrong, let us know! Other people may have done the same thing; maybe you
can help them.

## Fork the repo
In github, take a fork of iotinafrica/intro-to-python. We'll be working in the `labs` directory.

## <a name="1"></a>1: Counting
In the file `counting.py`, write a function called `count` that returns the numbers from 1 to 5
in a `list`. Call your function from `__main__()` and print the results to make sure it's doing the
right thing

Remember to write a `docstring` for your module!

## <a name="2"></a>2: More counting!
In the file `counting_arrays.py`, write another function called `count` that takes a numerical
argument `n` and returns the numbers from 1 to `n` in a `list`.
The list should *include* the `n`. Again, write code in `__main()__`
to test your new `count`.

## <a name="3"></a>3: Evens
In the file `evens.py`, write a function called `evens` that takes a list of numbers and returns the sum
of all the even numbers.

## <a name="4"></a>4: Tuples
In the file `tuples.py`, write two functions:
* `partition` should take a number and return a 2-tuple, with the number on the *left* if it's even, and
on the *right* if it's odd. The other slot should be filled with the constant `None`
* `partition_list`, which takes a list of numbers and returns a 2-tuple of *lists*. It should use your
`partition` function to split the input list into the odd numbers and the even numbers.

# Stretch
Well done if you've come so far. Below are some harder labs that will take more time. Everyone should
hopefully get at least this far

## <a name="complex"></a>Stretch: Complex numbers
Investigate the `complex` numeric type. In a file called `mandelbrot.py`, write a function called `mandelbrot`
that takes a number `n` and prints out the <a href="en.wikipedia.org/mandelbrot_set">Mandelbrot Set</a>
using ascii characters in an `n` x `n` matrix.

## <a name="tic-tac-toe"></a>Stretch: tic-tac-toe
Write a tic-tac-toe game. Firstly, it should print out an empty grid, then wait for input. Players take
turns entering coordinates in the form (x, y). The game adds a O or an X in the right square, then prints
out the grid again.

Make good use of functions to split up your code. For example, you could write a function `print_grid`
which takes the grid state as an argument and prints it to the console.

Stretch: Write a single-player game where the computer plays against you. Are you better at Python than
you are at tic-tac-toe? :)

## Testing
In the shell, in the `labs` directory, execute `python tests.py`. If you've followed all the instructions
and done well in the labs, all the tests should pass. If you get test failures, the output will show you
where you've gone wrong.

Testing is an important part of any software development process. "Testing" code using `__main__()` methods
is brittle, because you need to execute them manually - meaning you might forget and check in buggy code.

In the next labs, we'll ask you to write your own tests *before* you even start writing code. This helps
you think about the problem, and is a really great professional practice.

## Finally
If you've been working in pairs, you'll both want a copy of the code. The other person should also
take a fork of the codeabase and should accept a `pull request` for the changes, so that everyone
has working labs.