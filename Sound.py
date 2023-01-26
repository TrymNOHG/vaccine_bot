class Sound:

    def f1():
        ev3.speaker.play_file("Farsken.wav")

    def f2():
        ev3.speaker.play_file("vaccine.wav")    

    def f3():
        ev3.speaker.play_file("Nein.wav")   

    f_list = [f1, f2, f3] 

    def play(code):
        # Code 307 is the input from the triangle button
        if code == 307:
            if value == 1:
                rtall = random.randint(0,2)
                f_list[rtall]()