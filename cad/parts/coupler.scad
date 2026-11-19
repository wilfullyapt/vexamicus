// Coupler (parallelogram assist)
include <../vitamins.scad>

module coupler() {
    L = COUPLER_L;
    difference() {
        hull() {
            cylinder(d=LEG_WIDTH, h=LEG_THICK*0.85, center=true);
            translate([L,0,0]) cylinder(d=LEG_WIDTH, h=LEG_THICK*0.85, center=true);
        }
        bolt_hole();
        translate([L,0,0]) bolt_hole();
    }
}

coupler();
