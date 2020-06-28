# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

sun_center = sd.get_point(430, 650)

def sun():
    i = 0
    while True:
        sd.circle(center_position=sun_center, radius=60, color=sd.COLOR_YELLOW, width=0)
        if i % 2 == 0:
            #sd.start_drawing()
            for angle in range(0, 360, 30):
                if angle % 20 == 0:
                    v = sd.get_vector(start_point=sun_center, angle=angle, length=90, width=4)
                    v.draw(sd.COLOR_YELLOW, width=4)
                    v1 = sd.get_vector(start_point=v.end_point, angle=angle, length=30, width=4)
                    v1.draw(sd.COLOR_YELLOW, width=4)
                    #sd.circle(center_position=sun_center, radius=60, color=sd.COLOR_YELLOW, width=0)
                else:
                    v = sd.get_vector(start_point=sun_center, angle=angle, length=90, width=4)
                    v.draw(sd.COLOR_YELLOW)
                    v1 = sd.get_vector(start_point=v.end_point, angle=angle, length=30, width=4)
                    v1.draw(sd.COLOR_DARK_BLUE, width=4)
                    #sd.circle(center_position=sun_center, radius=60, color=sd.COLOR_YELLOW, width=0)
        else:
            for angle in range(0, 360, 30):
                if angle % 20 == 0:
                    v = sd.get_vector(start_point=sun_center, angle=angle, length=90, width=4)
                    v.draw(sd.COLOR_YELLOW)
                    v1 = sd.get_vector(start_point=v.end_point, angle=angle, length=30, width=4)
                    v1.draw(sd.COLOR_DARK_BLUE, width=4)
                    #sd.circle(center_position=sun_center, radius=60, color=sd.COLOR_YELLOW, width=0)
                else:
                    v = sd.get_vector(start_point=sun_center, angle=angle, length=90, width=4)
                    v.draw(sd.COLOR_YELLOW, width=4)
                    v1 = sd.get_vector(start_point=v.end_point, angle=angle, length=30, width=4)
                    v1.draw(sd.COLOR_YELLOW, width=4)
                    #sd.circle(center_position=sun_center, radius=60, color=sd.COLOR_YELLOW, width=0)
        #sd.sleep(1)

        i += 1
        sd.sleep(1)
        if sd.user_want_exit():
            break




#sun()

#sd.pause()
