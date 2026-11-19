// Femur link (hip → knee)
include <../vitamins.scad>

module femur() {
    L = FEMUR_L;
    difference() {
        hull() {
            cylinder(d=LEG_WIDTH+2, h=LEG_THICK, center=true);
            translate([L,0,0]) cylinder(d=LEG_WIDTH+2, h=LEG_THICK, center=true);
        }
        // I-beam cutouts
        for (s=[-1,1])
            translate([L/2, s*2.2, 0])
                cube([L*0.72, 1.6, LEG_THICK+1], center=true);
        bolt_hole();
        translate([L,0,0]) bolt_hole();
        // cable groove
        translate([L/2, 0, LEG_THICK/2])
            cube([L*0.6, 1.5, 1.2], center=true);
    }
}

femur();
