#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
# from getresolve import getresolve
from smpte import SMPTE


# Init Resolve
# resolve = getresolve()
projectManager = resolve.GetProjectManager()
currentProject = projectManager.GetCurrentProject()
currentTimeline = currentProject.GetCurrentTimeline()
itemList = currentTimeline.GetItemListInTrack('video', 1)

s = SMPTE()
s.fps = currentTimeline.GetSetting('timelineFrameRate')
if currentTimeline.GetSetting('timelineDropFrameTimecode') == '1':
    s.df = True

# Init joystick
clock = pygame.time.Clock()
pygame.joystick.init()
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()


def goto_item(cvi, direction):

    cviStart = cvi.GetStart()
    i = 0

    while i < len(itemList):

        # Get the item after the current timeline item.
        if itemList[i].GetStart() == cviStart:

            if direction == 'left':
                try:
                    cueItem = itemList[i-1]
                except IndexError:
                    break

            if direction == 'right':
                try:
                    cueItem = itemList[i+1]
                except IndexError:
                    break

            # Go to the next video item.
            frames = cueItem.GetStart()
            timecodeString = s.gettc(frames)
            currentTimeline.SetCurrentTimecode(timecodeString)

        i += 1


#
def main_loop():

    while True:
        for event in pygame.event.get():
            pass

        currentVideoItem = currentTimeline.GetCurrentVideoItem()

        # Reset pan position to default.
        if joystick.get_button(1) == 1:
            currentVideoItem.SetProperty({'Pan': 0})

        # Go to the clip to the left of the playhead
        if joystick.get_button(3) == 1:
            clock.tick(6)
            goto_item(currentVideoItem, 'left')

        # Go to the clip to the right of the playhead
        if joystick.get_button(0) == 1:
            clock.tick(6)
            goto_item(currentVideoItem, 'right')

        # Change timeline resolution, square, vertical.
        if joystick.get_button(9) == 1:
            clock.tick(6)
            currentProject.SetSetting('timelineResolutionWidth',  '1080')
            currentProject.SetSetting('timelineResolutionHeight', '1080')

        if joystick.get_button(10) == 1:
            clock.tick(6)
            currentProject.SetSetting('timelineResolutionWidth',  '1080')
            currentProject.SetSetting('timelineResolutionHeight', '1920')


        # Get joystick value for position.
        axisPosition = joystick.get_axis(0)

        # Set pan value.
        currentPan = currentVideoItem.GetProperty('Pan')
        pan  = currentPan  + (axisPosition  *  4.5) ** 3
        currentVideoItem.SetProperty({'Pan': pan})

        clock.tick(60)

        # Quit when button 6 is pressed.
        if joystick.get_button(6) == 1:
            print('Exit')
            exit()

    pygame.quit()



if __name__ == '__main__':
    main_loop()
