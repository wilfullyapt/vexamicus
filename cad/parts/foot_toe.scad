// Foot + ankle rest (static crouch stand, Salto-inspired)
include <../vitamins.scad>

module foot_toe() {
    difference() {
        union() {
            // toe sphere-ish
            translate([0,0,0]) sphere(r=TOE_R);
            // ankle plate
            translate([0,0,TOE_R*0.35])
                cylinder(r=TOE_R*0.9, h=6*SCALE, center=false);
            // shin fork
            translate([0,0,TOE_R*0.35 + 5*SCALE])
                cube([LEG_WIDTH+6, LEG_THICK+4, 14*SCALE], center=true);
            // ankle rest pads (two feet for crouch) — lateral
            for (y=[-1,1])
                translate([-TOE_R*0.9, y*(TOE_R*0.85), -TOE_R*0.2])
                    cube([10*SCALE, 8*SCALE, ANKLE_PAD_H], center=true);
        }
        // hollow rubber seat
        sphere(r=TOE_R - 2.5);
        // axle
        translate([0,0,TOE_R*0.5])
            rotate([90,0,0]) cylinder(d=BEARING_ID+0.2, h=40, center=true);
        // bottom open for rubber plug
        translate([0,0,-TOE_R])
            cylinder(r=TOE_R*0.55, h=TOE_R, center=false);
    }
}

foot_toe();
