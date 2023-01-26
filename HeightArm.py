class HeightArm:

    def move(self, code):
        # Code 310 reacts to the L1 button
        # This moves the arm up
        if code == 310:
            if value == 1:
                # Positive run is up
                height_motor.run(50)
            else: 
                height_motor.run(0)   
          
        # Code 311 is the input from the R1 button.
        # This moves the arm down.
        elif code == 311:
            if value == 1:
                # Negative run is down
                height_motor.run(-50)
            else: 
                height_motor.run(0)