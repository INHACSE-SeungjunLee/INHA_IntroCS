from cs1graphics import *
import time

def interpolate_colors(t, color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (int((1 - t) * r1 + t * r2),
            int((1 - t) * g1 + t * g2),
            int((1 - t) * b1 + t * b2))

def color_value(color):
    return Color(color).getColorValue()

def change_color(sun, morning_sky, noon_sky, morning_sun, noon_sun):
    sky_color1 = color_value(morning_sky)
    sky_color2 = color_value(noon_sky)
    sun_color1 = color_value(morning_sun)
    sun_color2 = color_value(noon_sun)
    t = 0
    for i in range(100):
        t = t+0.01
        canvas.setBackgroundColor(interpolate_colors(t, sky_color1, sky_color2))
        sun.setFillColor(interpolate_colors(t, sun_color1, sun_color2))
        time.sleep(0.1)

canvas = Canvas(400, 300)
sun = Circle(30, Point(200,100))
sun.setBorderWidth(0)
canvas.add(sun)

change_color(sun, morning_sky="dark blue", noon_sky="deepskyblue", morning_sun="red", noon_sun="yellow")

canvas.wait()
canvas.close()