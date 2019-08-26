
#include <Servo.h>

#define pressed 90
#define unpressed 0

String command;
Servo servo_right;
Servo servo_left;

void setup() {
    // Starting the serial console
    Serial.begin(9600); 
    
    // Attaching both servos
    servo_right.attach(7);
    servo_left.attach(8);
    
    // Setting them in position zero
    servo_right.write(0);
    servo_left.write(0);
    Serial.println("Ready for commands, press my buttons!");
}
 
void loop() {
    if(Serial.available()){
        command = Serial.readStringUntil('\n');
        
        // Press trezor's right button
        if(command.equals("right press")){
          Serial.println("Pressing right button.");
          servo_right.write(pressed);
        }
        
        // Unpress trezor's right button
        else if(command.equals("right unpress")){
          Serial.println("Unpressing right button.");
          servo_right.write(unpressed);
        }
        
        // Press trezor's left button
        else if(command.equals("left press")){
        Serial.println("Pressing the left button.");
        servo_left.write(pressed);
        }
        
        // Unpress trezor's left button
        else if(command.equals("left unpress")){
          Serial.println("Unpressing the left button.");
          servo_right.write(unpressed);
        }
    }
}
