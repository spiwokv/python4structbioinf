# How to install PoVRay

* Type:
```
git clone https://github.com/POV-Ray/povray.git
```

* Follow [https://github.com/POV-Ray/povray/blob/3.7-stable/unix/README.md](https://github.com/POV-Ray/povray/blob/3.7-stable/unix/README.md)

# How to install Mplayer (incl. mencoder)

* Type:
```
wget ftp://ftp.mplayerhq.hu/MPlayer/releases/MPlayer-1.3.0.tar.xz
```

* Untar the file

* Compile and install by:
```
./configure 
make 
sudo make install
```

* If fails install missing libraries, e.g. yasm
```
sudo apt-get install yasm
```
