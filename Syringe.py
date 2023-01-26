class Syringe:

    def move(self, code):
        # Code 304 reacts to the X button
        # The value variables corresponds to whether the button is pressed or released
        # A value of 1 means the button is was pressed. A value of 0 means the button was released.
        # This if moves the syringe down
        if code == 304:
            if value == 1:
                # Positive run on the syringe is down
                syringe_motor.run(3000)
            else: 
                syringe_motor.run(0)

        # Code 305 reacts to the O botton
        #  This elif moves the syringe up     
        elif code == 305:
            if value == 1:
                # Negative run on the syringe is up
                syringe_motor.run(-3000)
            else: 
                syringe_motor.run(0)