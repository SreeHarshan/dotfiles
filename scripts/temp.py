#!/usr/bin/python3
import random

def calc2(sub,tenth,long):
    sub=sub/100*30
    sub+=(88/100)*40
    sub+=tenth
    if long:
        sub=sub/100*80
        sub+=20-random.randint(1,3)
    else:
        sub=sub/100*70
        sub+=30-random.randint(1,3)
    sub=round(sub,0)
    return sub

def calc(tenth,eng,math,phy,che,comp):

    tenth=tenth/100*30
    
    eng=calc2(eng,tenth,True)
    print("Eng:",eng)

    math=calc2(math,tenth,True)
    print("Math:",math)

    phy=calc2(phy,tenth,False)
    print("Phy:",phy)

    che=calc2(che,tenth,False)
    print("Che:",che)

    comp=calc2(che,tenth,False)
    print("Comp:",comp)

    cutoff = (phy+che)/2 + math
    print("Cutoff:",cutoff)

calc(91,75,48,53,74,80)
