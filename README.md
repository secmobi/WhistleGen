# What's this?

A 3D whistle model generator forked from Josef Prusa's version.

# How to use?

1. edit the "data.txt" with initials you want to be on whistles
2. ./generator.py
3. compile the whistleN.scad with OpenSCAD and export as STL files
4. use Slic3r to slice the STL files with the config file and print them by a 3D printer

# What're differences with the origin branch?

- fixed errors in generated SCAD files
- rewrited generator with more clear code
- deleted unnecessary files
- added a Slic3r config file which especially optimized for printing whistles in a RepRap printer without cooling fan

# Author
Claud Xiao
http://github.com/secmobi/WhistleGen

# Original README

Whistle generator is written by Josef Prusa - http://josefprusa.cz
licensed under Attribution - Non-Commercial - Creative Commons license


Whistle model is derivative of Whistle by Zaggo, licensed under the Attribution - Non-Commercial - Creative Commons license.

Font used, Candal, is from More Fontz! by polymaker, licensed under the Attribution - Share Alike - Creative Commons license.


//// USING THE GENERATOR
1) Fill the data.txt with initial which will appear on whistles
For example:

HA
CK
AD
AY

2) From your command line run the script

"python generator.py"

3) Compile the resulting plates of whistles in OpenSCAD. They are named whistles1.scad up-to whistlesN.scad depending on the number of initials provided.

4) Slice the resulting .stls in Slic3r and print!

///////// 28.4.2012
