// Body core — battery bay, MCU shelf, hip mounts, tail bearing
include <../vitamins.scad>

module body_core() {
    difference() {
        // outer shell
        hull() {
            translate([0,0,0])
                round_rect([BODY_L, BODY_W, BODY_H], r=3, center=true);
            // motor shoulder bulge (+X)
            translate([BODY_L*0.28, 0, 2])
                rotate([0,90,0])
                    cylinder(d=BODY_W*0.85, h=12*SCALE, center=true);
        }

        // hollow
        round_rect([BODY_L-2*WALL, BODY_W-2*WALL, BODY_H-2*WALL], r=2, center=true);

        // battery bay opening (-Z)
        translate([0, 0, -BODY_H/2 + BATTERY_H/2 + 1])
            cube([BATTERY_L + 1, BATTERY_W + 1, BATTERY_H + 2], center=true);

        // MCU tray access (+Z)
        translate([0, 0, BODY_H/2 - 1])
            cube([BODY_L*0.55, BODY_W*0.55, WALL+2], center=true);

        // hip axle through (Y)
        translate([-BODY_L*0.15, 0, HIP_Z])
            rotate([90,0,0])
                cylinder(d=BEARING_ID + 0.2, h=BODY_W+10, center=true);

        // hip bearing seats
        for (s=[-1,1])
            translate([-BODY_L*0.15, s*(BODY_W/2 - 3), HIP_Z])
                rotate([90,0,0])
                    cylinder(d=BEARING_OD + CLEAR, h=6, center=true);

        // tail shaft bore (+Y side exit conceptually along Y through rear)
        translate([BODY_L*0.35, 0, 4])
            rotate([90,0,0])
                cylinder(d=TAIL_SHAFT + 0.3, h=BODY_W+8, center=true);

        // cable pass
        translate([0, BODY_W/2 - WALL/2, 0])
            cube([10, WALL+2, 8], center=true);

        // lightening
        for (x=[-12, 0, 12]*SCALE)
            translate([x, 0, 6])
                rotate([90,0,0])
                    cylinder(d=8*SCALE, h=BODY_W+2, center=true);
    }

    // internal MCU shelf
    translate([0, 0, 4])
        cube([BODY_L*0.5, BODY_W - 2*WALL - 1, 1.6], center=true);

    // battery retention lips
    for (y=[-1,1])
        translate([0, y*(BATTERY_W/2 + 1.2), -BODY_H/2 + 3])
            cube([BATTERY_L*0.7, 2, 3], center=true);

    // printed labels (emboss)
    translate([0, -BODY_W/2 + 0.6, 0])
        rotate([90,0,0])
            linear_extrude(1.2)
                text("VEXAMICUS", size=3.2*SCALE, halign="center", valign="center");
}

body_core();
