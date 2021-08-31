# Fourier-Pygame
Attempt to create an epicycle drawing using the Discrete Fourier Transform


This project is an attempt to replicate the epicycle drawings such as this one :https://www.youtube.com/watch?v=-qgreAUpPwM&t=101s
Doing this relies on using the Discrete Fourier Transform to take in a set of complex numbers and use them to give information about the complex function that describes them.
First, use draw.py to draw a path, which should write to fourierpath.txt , then run fourier_main.py to get the animation. Additionally, the file that fourier_main reads from can be changed to 
square.txt, which is a set of programatically created points that form a square. Currently the problem is that the animation works for the square but rarely for the drawing.

This is a work in progress and any help is greatly appreciated.
