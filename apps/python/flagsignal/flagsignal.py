#############################################################
# Flag Signal App v0.1
# 
# Created by Justinas Saldukas, jsaldukas@gmail.com
#############################################################
# Configuration:

# https://commons.wikimedia.org/wiki/File:White_flag_waving.svg
cfg_flag1Image = "apps/python/flagsignal/images/flags/white_249x268.png"
cfg_flag2Image = "apps/python/flagsignal/images/flags/red_249x268.png"
cfg_flag3Image = "apps/python/flagsignal/images/flags/green_249x268.png"
cfg_flagWidth = 249
cfg_flagHeight = 268

cfg_delay = 1000

# http://www.kbdedit.com/manual/low_level_vk_list.html
cfg_flag1Key = 0x61 #VK_NUMPAD1
cfg_flag2Key = 0x62 #VK_NUMPAD2
cfg_flag3Key = 0x63 #VK_NUMPAD3

#
#############################################################

appName = "flagsignal"
logPrefix = appName + ": "

import ac
import acsys
import math
import os, platform, sys
if platform.architecture()[0] == "64bit":
    sys.path.insert(0, "apps/python/flagsignal/stdlib64")
else:
    sys.path.insert(0, "apps/python/flagsignal/stdlib")
os.environ['PATH'] = os.environ['PATH'] + ";."
import ctypes

ac.log(logPrefix + "Started, version v0.1")

appWindow = 0
flag1Label = 0
flag2Label = 0
flag3Label = 0
delayTimer = 0

# This function gets called by AC when the Plugin is initialised
# The function has to return a string with the plugin name
def acMain(ac_version):
    global appWindow, appName, logPrefix, flag1Label, flag2Label, flag3Label
    global cfg_flag1Image
    global cfg_flag2Image
    global cfg_flag3Image
    global cfg_flagWidth, cfg_flagHeight
    
    ac.console(logPrefix + "acMain")
    try:
        appWindow = ac.newApp(appName)
        ac.setTitle(appWindow, "")
        ac.setIconPosition(appWindow, -7000, -3000)
        ac.setSize(appWindow, cfg_flagWidth, cfg_flagHeight + 30)
        ac.drawBorder(appWindow, 0)
        ac.setBackgroundOpacity(appWindow, 0)

        flag1Label = ac.addLabel(appWindow, "")
        ac.setPosition(flag1Label, 0, 30)
        ac.setSize(flag1Label, cfg_flagWidth, cfg_flagHeight)
        ac.setBackgroundTexture(flag1Label, cfg_flag1Image)
        ac.setVisible(flag1Label, 0)
        
        flag2Label = ac.addLabel(appWindow, "")
        ac.setPosition(flag2Label, 0, 30)
        ac.setSize(flag2Label, cfg_flagWidth, cfg_flagHeight)
        ac.setBackgroundTexture(flag2Label, cfg_flag2Image)
        ac.setVisible(flag2Label, 0)
        
        flag3Label = ac.addLabel(appWindow, "")
        ac.setPosition(flag3Label, 0, 30)
        ac.setSize(flag3Label, cfg_flagWidth, cfg_flagHeight)
        ac.setBackgroundTexture(flag3Label, cfg_flag3Image)
        ac.setVisible(flag3Label, 0)
        
        ac.addRenderCallback(appWindow, onRender)
        ac.console(logPrefix + "Initialized")
    except:
        ac.console(logPrefix + "Initialize failed:", sys.exc_info()[0])

    return appName

def onRender(delta_t):
    global flag1Label, flag2Label, flag3Label, delayTimer
    global cfg_delay, cfg_flag1Key, cfg_flag2Key, cfg_flag3Key
    
    ac.glColor4f(1,1,1,1)
    ac.setBackgroundOpacity(appWindow, 0)
    
    if ctypes.windll.user32.GetAsyncKeyState(cfg_flag1Key):
        ac.setVisible(flag1Label, 1)
        ac.setVisible(flag2Label, 0)
        ac.setVisible(flag3Label, 0)
        delayTimer = cfg_delay / 1000
    elif cfg_delay == 0:
        ac.setVisible(flag1Label, 0)
    
    if ctypes.windll.user32.GetAsyncKeyState(cfg_flag2Key):
        ac.setVisible(flag2Label, 1)
        ac.setVisible(flag1Label, 0)
        ac.setVisible(flag3Label, 0)
        delayTimer = cfg_delay / 1000
    elif cfg_delay == 0:
        ac.setVisible(flag2Label, 0)
    
    if ctypes.windll.user32.GetAsyncKeyState(cfg_flag3Key):
        ac.setVisible(flag3Label, 1)
        ac.setVisible(flag1Label, 0)
        ac.setVisible(flag2Label, 0)
        delayTimer = cfg_delay / 1000
    elif cfg_delay == 0:
        ac.setVisible(flag3Label, 0)
    
    if delayTimer > 0:
        delayTimer -= delta_t
        if delayTimer <= 0:
            ac.setVisible(flag1Label, 0)
            ac.setVisible(flag2Label, 0)
            ac.setVisible(flag3Label, 0)
            delayTimer = 0
    