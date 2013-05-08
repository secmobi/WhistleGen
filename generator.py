#!/usr/bin/env python

ROW_MAX = 4
COL_MAX = 3

SCAD_BEGIN = """include <Candal.scad>

w = 44;
h = 28;
"""

SCAD_TEMPLATE = """
translate([%d*w, %d*h, 0]) {
     import_stl("blank-whistle.stl");
     translate([-9, -5.5, 20])scale([0.25, 0.25, 0.2]) {
         translate([0, 0, 0]) color("red") Candal("%s", steps = 3, center = true);
     }
}
"""

fn = 1
output = open('whistle%d.scad' % fn, 'w')
output.write(SCAD_BEGIN)

line = 0
for name in open('data.txt', 'r').readlines():
    name = name.strip()
    if len(name) > 2 or len(name) == 0:
        continue

    row, col = line/COL_MAX, line%COL_MAX

    if line != ROW_MAX * COL_MAX:
        line = line + 1
    else:
        line = 0
        fn = fn + 1

        output.close()
        output = open('whistle%d.scad' % fn, 'w')
        output.write(SCAD_BEGIN)

    output.write(SCAD_TEMPLATE % (col, row, name))

output.close()
