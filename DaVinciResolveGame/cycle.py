#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This modules frame cycles 50 layers in Resolve timeline for our game.

from getresolve import getresolve
import time

# Init Resolve
resolve = getresolve()
projectManager = resolve.GetProjectManager()
currentProject = projectManager.GetCurrentProject()
currentTimeline = currentProject.GetCurrentTimeline()

def frame_cycle():

    t = .030

    while True:
        for i in range(1,51):
            currentTimeline.SetTrackEnable('video', i, True)
            time.sleep(t)
            currentTimeline.SetTrackEnable('video', i+1, True)
            currentTimeline.SetTrackEnable('video', i, False)

if __name__ == '__main__':
    frame_cycle()
