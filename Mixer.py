class Mixer:

    def mix(self, code):
        # Code 308 is the input from the square button
        # This mixes 
        if code == 308:  
            if value == 1:
                # Positive is anti-clockwise
                mix_motor.run(3000)
            else:
                mix_motor.run(0) 
