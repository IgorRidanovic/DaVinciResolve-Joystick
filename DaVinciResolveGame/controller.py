#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
from getresolve import getresolve

# Car clip is on this track.
carTrack = 51

# Init Resolve
resolve = getresolve()
projectManager = resolve.GetProjectManager()
currentProject = projectManager.GetCurrentProject()
currentTimeline = currentProject.GetCurrentTimeline()
currentTimeline.SetTrackEnable('video', carTrack, True)
currentVideoItem = currentTimeline.GetCurrentVideoItem()

# Init joystick
clock = pygame.time.Clock()
pygame.joystick.init()
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()


def main_loop():

    defaultPan  = pan  = 0
    defaultTilt = tilt = -180
    defaultZoom = zoom =.2

    while True:
        for event in pygame.event.get():
            pass

        # Reset car position to default.
        if joystick.get_button(1) == 1:
            pan  = defaultPan
            tilt = defaultTilt
            zoom = defaultZoom

        # Get joystick values.
        axisPan  = joystick.get_axis(0)
        axisTilt = joystick.get_axis(1)

        # Calibrate the joystick if necessary.
        # axisPan = axisPan - 0.00390625
        # if axisPan < 0:
        #     axisPan = axisPan / 1.00390625
        # if axisPan > 0:
        #     axisPan = axisPan /0.996063232421875

        # Set pan, tilt, and zoom values.
        pan  = pan  + (axisPan  *  4.5) ** 3
        tilt = tilt + (axisTilt * -4.5) ** 3
        zoom = tilt / -1000 + 1 * .01

        # Position limits
        if tilt <= -200:
            tilt = -200

        if tilt >= -130:
            tilt = -130

        if zoom <= .14:
            zoom = .14

        if zoom >= .21:
            zoom = .21

        if pan >= 165:
            pan = 165

        if pan <= -165:
            pan = -165

        currentVideoItem.SetProperty({'Pan': pan, 'Tilt': tilt, 'ZoomGang': True, 'ZoomX': zoom})

        clock.tick(60)

        # Quit when button 6 is pressed.
        if joystick.get_button(6) == 1:
            print('Game Over')
            exit()



if __name__ == '__main__':
    main_loop()
