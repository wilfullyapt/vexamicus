// Reaction wheel for pitch tail
include <../vitamins.scad>

module tail_wheel() {
    difference() {
        union() {
            cylinder(r=TAIL_WHEEL_R, h=TAIL_WHEEL_H, center=true);
            // hub boss
            cylinder(d=14, h=TAIL_WHEEL_H+4, center=true);
        }
        cylinder(d=TAIL_SHAFT + CLEAR, h=TAIL_WHEEL_H+10, center=true);
        // set screw
        rotate([0,90,0]) cylinder(d=2.4, h=TAIL_WHEEL_R);
        // mass pockets for brass inserts (M4 heat set / press)
        for (a=[0:45:315])
            rotate([0,0,a]) translate([TAIL_WHEEL_R*0.62, 0, 0])
                cylinder(d=6.2, h=TAIL_WHEEL_H+1, center=true);
        // spokes lighten
        for (a=[22.5:45:360])
            rotate([0,0,a]) translate([TAIL_WHEEL_R*0.38, 0, 0])
                cube([TAIL_WHEEL_R*0.35, 3, TAIL_WHEEL_H+1], center=true);
    }
}

tail_wheel();
