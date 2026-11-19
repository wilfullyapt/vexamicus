// Shin link (knee → foot)
include <../vitamins.scad>

module shin() {
    L = SHIN_L;
    difference() {
        hull() {
            cylinder(d=LEG_WIDTH+1, h=LEG_THICK, center=true);
            translate([L,0,0]) cylinder(d=LEG_WIDTH+3, h=LEG_THICK, center=true);
        }
        for (s=[-1,1])
            translate([L/2, s*2.0, 0])
                cube([L*0.75, 1.5, LEG_THICK+1], center=true);
        bolt_hole();
        translate([L,0,0]) bolt_hole(d=BEARING_ID);
        // foot mount face flats
        translate([L, 0, 0])
            for (a=[0:90:270]) rotate([0,0,a]) translate([5,0,0])
                cylinder(d=1.8, h=LEG_THICK+1, center=true);
    }
}

shin();
