from manim import *
import numpy as np
import random

class diff(Scene):
    def construct(self):
        L = []
        L2 =[]
        title = Text("Bubble Sort", color=WHITE).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        for x in range(0, 11):
            x = random.randint(1, 20)
            number = MathTex(str(x))
            L2.append(x)
            box = Square(side_length=1, stroke_width=10, color="BLUE")
            final = VGroup(box, number)
            L.append(final)
        i=0
        for x in range(-5,6):
                position = np.array([x, 0, 0])
                self.play(L[i].animate.move_to(position), run_time=1)
                i+=1
               
        self.wait(2)
        self.play(Unwrite(title))

    
    
        n = len(L2)

        for i in range(n):
                for j in range(0, n - i - 1):
                    if L2[j] >= L2[j + 1]:
                        self.swap(L[j], L[j + 1])
                        L2[j], L2[j + 1] = L2[j + 1], L2[j]
                        L[j], L[j + 1] = L[j + 1], L[j]
        self.wait(0.5)
        for box in L:
             self.play(box[0].animate.set_color(GREEN),run_time=0.1)
        
        self.wait(5)

    def swap(self,mob1, mob2):
        x1, y1, z1 = mob1.get_center()
        x2, y2, z2 = mob2.get_center()
        mob1[0].set_color(RED)
        mob2[0].set_color(YELLOW)
        self.play(mob1.animate.shift(DOWN*2))
        self.play(mob1.animate.shift(RIGHT*(x2 - x1)))
        self.play(mob2.animate.shift(UP*2))
        self.play(mob2.animate.shift(LEFT* (x2 - x1)))
        self.play(mob1.animate.shift(UP*2))
        self.play(mob2.animate.shift(DOWN*2)) 
        mob1[0].set_color(BLUE)
        mob2[0].set_color(BLUE)

 

