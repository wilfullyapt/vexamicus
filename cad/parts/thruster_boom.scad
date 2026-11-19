// T2 thruster boom (pair mirrored in assembly)
include <../vitamins.scad>

module thruster_boom(side=1) {
    difference() {
        union() {
            // spar
            hull() {
                cylinder(d=8*SCALE, h=6*SCALE, center=true);
                translate([THRUST_BOOM_L, side*12*SCALE, 8*SCALE])
                    cylinder(d=10*SCALE, h=6*SCALE, center=true);
            }
            translate([THRUST_BOOM_L, side*12*SCALE, 8*SCALE])
                cylinder(r=THRUST_MOTOR_R+2, h=8*SCALE, center=true);
        }
        // body bolt
        bolt_hole(d=2.6);
        // motor bore
        translate([THRUST_BOOM_L, side*12*SCALE, 8*SCALE])
            cylinder(r=THRUST_MOTOR_R, h=10*SCALE, center=true);
        // wire channel
        translate([THRUST_BOOM_L/2, side*6, 4])
            cube([THRUST_BOOM_L*0.7, 2, 2], center=true);
    }
}

thruster_boom(1);
