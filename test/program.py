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
