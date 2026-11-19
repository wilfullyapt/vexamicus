// Shared primitives
include <params.scad>

module round_rect(size, r=1.5, center=false) {
    // size = [x,y,z]
    x=size[0]; y=size[1]; z=size[2];
    translate(center ? [-x/2,-y/2,-z/2] : [0,0,0])
    minkowski() {
        cube([max(0.01,x-2*r), max(0.01,y-2*r), max(0.01,z)], center=false);
        cylinder(r=r, h=0.01, center=false);
    }
}

module bearing_pocket(h=LEG_THICK+0.2) {
    cylinder(d=BEARING_OD + CLEAR, h=h, center=true);
}

module bolt_hole(d=BEARING_ID, h=40) {
    cylinder(d=d + CLEAR, h=h, center=true);
}

module carbon_tube(L=50, od=4, id=3) {
    difference() {
        cylinder(d=od, h=L, center=true);
        cylinder(d=id, h=L+1, center=true);
    }
}

module motor_standoff_pattern(spacing=16, h=6, d=2.2) {
    for (a=[0:90:270])
        rotate([0,0,a]) translate([spacing/2,0,0])
            cylinder(d=d, h=h, center=true);
}
