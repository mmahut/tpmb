// Version: 0.3

// Horizontal wall
difference() {
    // Creating the base 
    cube([100,80,7]);
    
    // Cutting a hole for trezor to sit in
    translate([0,25,2])
        cube([65,30,10]);
}

// Vertical wall
difference() {
    // Creating the vertical block
    cube([10, 80, 28]);
    // Cutting an opening for stuck trezor
    translate([0,26,-2])
        cube([10,28,12]);
    
    // Creating opening for right servo
    translate([0,7,12])
     cube([10,23,22]);
    
    // Creating opening for left servo
    translate([0,50,12])
     cube([10,23,22]);
}
