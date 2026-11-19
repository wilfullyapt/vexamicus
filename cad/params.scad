// Vexamicus T0/T1 parametric dimensions (mm)
// Inspired by published Salto-class proportions — original geometry, not a CAD clone.

/* [Scale] */
// Overall linear scale vs nominal T1 (1.0 ≈ 240 mm body height class)
SCALE = 1.0;

/* [Body] */
BODY_W = 42 * SCALE;      // Y width
BODY_H = 38 * SCALE;      // Z height of core block
BODY_L = 55 * SCALE;      // X length
WALL = 2.4 * SCALE;
BATTERY_L = 48 * SCALE;
BATTERY_W = 18 * SCALE;
BATTERY_H = 14 * SCALE;

/* [Leg 4-bar] */
HIP_Z = -8 * SCALE;                 // hip joint below body center
FEMUR_L = 55 * SCALE;               // hip → knee
SHIN_L = 70 * SCALE;                // knee → foot
COUPLER_L = 48 * SCALE;             // parallel coupler
CRANK_L = 18 * SCALE;               // SEA output crank
LEG_THICK = 5 * SCALE;
LEG_WIDTH = 8 * SCALE;
BEARING_ID = 3.2;                   // M3 clearance
BEARING_OD = 10.0;                  // 623-ish pocket (simplified)

/* [Foot] */
TOE_R = 12 * SCALE;
ANKLE_PAD_H = 6 * SCALE;

/* [SEA hub] */
SEA_HUB_R = 16 * SCALE;
SEA_HUB_H = 12 * SCALE;
MOTOR_BORE = 5.2;                   // typical BLDC shaft
SPRING_SLOT_W = 4.5 * SCALE;

/* [Tail / reaction wheel] */
TAIL_BOOM_L = 35 * SCALE;
TAIL_WHEEL_R = 28 * SCALE;
TAIL_WHEEL_H = 8 * SCALE;
TAIL_SHAFT = 3.2;

/* [Thruster booms T2] */
THRUST_BOOM_L = 45 * SCALE;
THRUST_ARM_ROLL = 40 * SCALE;       // ~ half of Salto 80mm moment arm at SCALE~1
THRUST_MOTOR_R = 6 * SCALE;

/* [Clearance / print] */
CLEAR = 0.25;
$fn = 48;

function mm(x) = x;
