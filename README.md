# Python tutorial for Structural Bioinformatics Course

In this tutorial we will show how to automatize some repeating process. Here we will use it to make
a movie of a rotating molecule. For this purpose we will use Python scripting language.
This language can be used directly in command line by typing:
```
python
```
This opens a command line of Pythonu. You can type some commands there and they will be immidiatelly
executed. We will not use it this way. Therefore exit Python command line by Ctrl+D.

Instead we will write the program into the file. We will call it `program.py`. Such program can be
executed by typing:
```
python program.py
```
It is possible to use another option which we will describe later.

Let us start with writing the program in Linux shell:
```
cat > program.py 
print 1+1 
Ctrl+D
```
We will get a file `program.py` with a single line:
```{python}
print 1+1
```
This can be executed by:
```
python program.py
```
The program will calculate 1+1 and print the result. 

You can edit the program to:
```{python}
for i in range(10):
  print i
```
It is important to have indent of (preferably two) spaces before print.
This will define what is in the loop. The command `range(10)` returns 10 numbers from 0 to 9.
The line `for i in range(10):` will create a loop that is executed 10x. The value of `i` in the first
execution is equal to 0, in the next execution it is 1 etc. The program will therefore print 0 to 9,
one on each line. Try it.

If you want 1, 2 ... 10, you can simply replace `print i` by `print i+1`

If we replace `print i` for `print i+i` it will print 0, 2, 4 ... 18.

We can add `i` values not as numbers but as strings. To do this we can convert them to a string
by function `str` as `str(i)`. If you replace `print i+i` by `print str(i)+str(i)` the program will
print 00, 11, ... 99.

Now we will show how to make strings 00, 01, ... 09 or even 000, 001, ... 999. There are more elegant
ways how to do that, for example using regular expressions, but we will show this in less elegant
way to learn some Python. For this we will take the value of `i` and we will store it as a string
in the variable `si` using `si = str(i)`. Next, we will add zeros in front of si untill it reaches
the length of the string equal to 3. Here we go:
```{python}
for i in range(10): 
  si = str(i) 
  while len(si)<3: 
    si = "0"+si 
  print si 
```
Note that there are four spaces in front of `si = "0"+si`, which means that there is a loop in the
loop. The command `while` is executed while the condition (`len(si)<3`) is true. The function `len`
(when applied on a string) returns the number of characters in the string, i.e. 1 for "0", 2 for "00"
etc.

Now let's have a look at something different. 

There are many programs for rendering scenes. For some reason the program 
[PoVRay](https://www.povray.org) is very popular for making molecular representations and
is supported by many molecular visualization programs. PoVRay takes an input file as a scene
containing various spheres, tubes and other 3D shapes, together with their colors, textures etc.
Beside that you can specify locations, colors and intensities of light sources, location of
camera, you can add fog and you can do many other things.

For a protein you can open it in some software such as 


and save it as an input file for PoVRay. Next you can render it by a command which may look
something like:
```
povray +H400 +W600 +A0.3 test.pov
```
where +H and +W defines height and width, respectively, +A defines antialliasing and `test.pov`
is the input file. This should generate a file `test.png`.


