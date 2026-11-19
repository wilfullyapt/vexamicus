// Full Vexamicus T1 preview assembly (kinematic pose)
include <params.scad>
use <parts/body_core.scad>
use <parts/sea_hub.scad>
use <parts/femur.scad>
use <parts/shin.scad>
use <parts/coupler.scad>
use <parts/foot_toe.scad>
use <parts/tail_wheel.scad>
use <parts/thruster_boom.scad>

// Pose: hip crank angle (deg). 0 = outstretched-ish, negative crouches.
HIP_ANGLE = -35;
KNEE_BEND = 55; // simple display bend

module leg_assembly() {
    // SEA at hip
    color("orange")
        rotate([90,0,0])
            sea_hub();

    // femur
    color("steelblue")
        rotate([0, HIP_ANGLE, 0]) {
            femur();
            // knee
            translate([FEMUR_L, 0, 0])
                rotate([0, KNEE_BEND, 0]) {
                    color("cadetblue") shin();
                    translate([SHIN_L, 0, 0])
                        rotate([0, -HIP_ANGLE - KNEE_BEND, 0])
                            color("DimGray") foot_toe();
                }
            // coupler (display only — parallel approx)
            translate([8, LEG_THICK+1, 0])
                rotate([0, HIP_ANGLE*0.2, 0])
                    color("gray") coupler();
        }
}

module assembly(show_thrusters=true) {
    // body
    color("SlateGray") body_core();

    // leg on -X hip
    translate([-BODY_L*0.15, LEG_THICK, HIP_Z])
        leg_assembly();

    // tail wheel on +X / +Y
    color("goldenrod")
        translate([BODY_L*0.35, BODY_W/2 + TAIL_WHEEL_H, 4])
            rotate([90,0,0])
                tail_wheel();

    if (show_thrusters) {
        color("IndianRed")
            translate([BODY_L*0.1, BODY_W/2 - 2, BODY_H/2 - 4])
                thruster_boom(1);
        color("IndianRed")
            translate([BODY_L*0.1, -(BODY_W/2 - 2), BODY_H/2 - 4])
                thruster_boom(-1);
    }

    // ground plane hint
    color([0.3,0.5,0.3,0.25])
        translate([0,0, -SHIN_L - FEMUR_L*0.3 - TOE_R])
            cube([200, 200, 1], center=true);
}

assembly(true);
