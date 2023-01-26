class RotateArm:

    def move(self, code):
        # Code 312 is the input from the L2 button
        # This moves the arm anti-clockwise
        if code == 312:
            if value == 1:
                # Positive run is left when looking at the robot with the pybrick in front of you
                rotate_motor.run(200)
            else: 
                rotate_motor.run(0)

        # Code 313 is the input from the R2 button
        # This moves the arm clockwise
        elif code == 313:
            if value == 1:
                # Negative run is to the right
                rotate_motor.run(-200)
            else: 
                rotate_motor.run(0)      