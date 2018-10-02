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

Now let's have a look at something different. We will show how to make a movie with a rotating protein
molecule. It is possible to open the molecule in a PDB format in [VMD](https://www.ks.uiuc.edu/Research/vmd/)
and save the scene in some format suitable for rendering.

There are many programs for rendering scenes. For some reason the program 
[PoVRay](https://www.povray.org) is very popular for making molecular representations and
is supported by many molecular visualization programs. PoVRay takes an input file as a scene
containing various spheres, tubes and other 3D shapes, together with their colors, textures etc.
Beside that you can specify locations, colors and intensities of light sources, location of
camera, you can add fog and you can do many other things.

For a protein you can open it in VMD and save it as a `pov` file. You can find these files in
directory `vmdscenes` of this repository. Chose some. If you like you can render it by typing:
```
povray +H600 +W600 +A0.3 vmdscene1.pov -D
```
where `+H` and `+W` defines height and width in pixels, respectively and `+A` defines antialliasing.
This should generate a file `vmdscene1.png`. The option `-D` suppresses PoVRay to show the output image.
This is usefull for rendering via ssh.

Now edit the file you have chosen. It is a text file with understandable keywords such as sphere,
cylinder, camera, fog etc. Now we will make a copy of the file and we will call it `vmdscene1b.pov`
(b for begining):
```
cp vmdscene1.pov vmdscene1b.pov
```
Now edit `vmdscene1b.pov`. The code is different for different scenes, but there are common
definitions of camera, light sources, fog and textures followed by a line:
```
#declare VMD_line_width=0.0020;
```
Make a new line right after this line and insert there a text:
```
#declare protein=union {
```
Now go to the end of the file and add new lines at the bottom:
```
}
object {
  protein
```
Save the file and exit. To recapitulate, we created a file with a structure:
```
SOME SETTINGS HERE
#declare protein=union {
  SOME OBJECT HERE
}
object {
  protein
```
When we add lines:
```
  rotate <0,90,0>
}
```
it will take the object defined between `#declare protein=union {` and `}` (called protein)
and it will rotate it by 90 degrees around axis y. VMD makes the PoVRay files with the protein
centered in the coordinate system so we do not have to translate it to the center of the coordinate
system before rotation and translate back after rotation.

We will not rotate it by 90 degrees, but instead by 1, 2, 3 ... 360 degrees. To do so, write a Python
script:
```{python}
zacatek = open("vmdscene1b.pov", "r").readlines()
for i in range(360):
  si = str(i)
  while len(si) < 3:
    si = "0"+si
  novy = open("final.pov", "w")
  for line in zacatek:
    novy.write(line)
  novy.write("rotate <0,"+str(i)+",0> \n")
  novy.write("}\n")
  novy.close()
```
The command `open` opens the file. The option `"r"` opens the file for reading and `.readlines()`
separates the file into infdividual lines. The option `"w"` opens the file for writing.
The code:
```{python}
  for line in zacatek:
    novy.write(line)
```
rewrites the content of `vmdscene1b.pov` into a newly created file `final.pov`. After that the code:
```{python}
  novy.write("rotate <0,"+str(i)+",0> \n")
  novy.write("}\n")
```
adds lines:
```
rotate <0,0,0>
}
```
or `rotate <0,1,0>` etc. Finally, `novy.close()` closes the file `final.pov`.

To render `final.pov` in each step add a lines:
```{python}
import os
```
at the begining and
```{python}
  os.system("povray +H600 +W600 +A0.3 -Of"+si+".png -D final.pov")
```
into the loop, so that the final code looks like:
```{python}
import os
zacatek = open("vmdscene1b.pov", "r").readlines()
for i in range(360):
  si = str(i)
  while len(si) < 3:
    si = "0"+si
  novy = open("final.pov", "w")
  for line in zacatek:
    novy.write(line)
  novy.write("rotate <0,"+str(i)+",0> \n")
  novy.write("}\n")
  novy.close()
  os.system("povray +H600 +W600 +A0.3 -Of"+si+".png -D final.pov")
```

Now run it (it may take a while). This will generate 360 files `f000.png` to `f359.png`.

Finally, you can make movie from images in mencoder by typing:
```
mencoder -ovc lavc -lavcopts vcodec=mpeg4:vpass=1:vbitrate=1620000:mbd=2:keyint=132:v4mv:vqmin=3:vlelim=-4:vcelim=7:lumi_mask=0.07:dark_mask=0.10: naq:vqcomp=0.7:vqblur=0.2:mpeg_quant -mf type=png:fps=25 -nosound -o test.avi mf://f*.png 
```




