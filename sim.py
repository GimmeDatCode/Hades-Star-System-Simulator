#!§usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from optimhades.system import System

def openSystem():
    return System.load("win.json")

sy = openSystem()

halfdays = 0 
while sy.creditCap() < 5000000:
    print(halfdays)
    sy.credits += sy.halfDayCreditYield()
    toUp = sy.findPlanetToUpgrade()
    if sy.credits >= toUp.typeUpCost() and toUp.upgradeTime == 0:
      sy.credits -= toUp.typeUpCost()
      toUp.upgrade()
    sy.tickUpgrades()
    halfdays +=1
print(halfdays / 2)
