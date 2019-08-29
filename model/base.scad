// Version: 0.1

// Horizontal wall
difference() {
    // Creating the base 
    cube([100,80,7]);
    
    // Cutting a hole for trezor to sit in
    translate([0,25,5]) 
        cube([50,30,2]);
}

// Vertical wall
difference() {
    // Creating the vertical block
    cube([10, 80, 24]);
    // Cutting an opening for stuck trezor
    translate([0,30,0]) 
        cube([10,20,10]);
    
    // Creating opening for right servo
    translate([0,7,12])
     cube([10,23,12]);
    
    // Creating opening for left servo
    translate([0,50,12])
     cube([10,23,12]);
}