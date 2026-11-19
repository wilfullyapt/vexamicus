// SEA torsion hub — motor shaft → latex pack → crank
include <../vitamins.scad>

module sea_hub() {
    difference() {
        union() {
            cylinder(r=SEA_HUB_R, h=SEA_HUB_H, center=true);
            // crank arm
            hull() {
                cylinder(d=10, h=SEA_HUB_H*0.7, center=true);
                translate([CRANK_L, 0, 0])
                    cylinder(d=8, h=SEA_HUB_H*0.7, center=true);
            }
            translate([CRANK_L, 0, 0])
                cylinder(d=10, h=SEA_HUB_H*0.9, center=true);
        }
        // motor shaft
        cylinder(d=MOTOR_BORE + CLEAR, h=SEA_HUB_H+2, center=true);
        // set screw
        translate([0, 0, 0]) rotate([0,90,0])
            cylinder(d=2.4, h=SEA_HUB_R+5);
        // latex slots (radial)
        for (a=[0:60:300])
            rotate([0,0,a])
                translate([SEA_HUB_R*0.55, 0, 0])
                    cube([SEA_HUB_R*0.7, SPRING_SLOT_W, SEA_HUB_H+1], center=true);
        // crank joint
        translate([CRANK_L, 0, 0]) bolt_hole(h=SEA_HUB_H+2);
        // lightening
        for (a=[30:60:330])
            rotate([0,0,a]) translate([SEA_HUB_R*0.35,0,0])
                cylinder(d=4, h=SEA_HUB_H+1, center=true);
    }
}

sea_hub();
