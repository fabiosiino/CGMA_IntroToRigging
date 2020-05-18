########################## Pin Control ##########################

from maya import cmds

def pinControl():
    pinCtl = cmds.curve( p=([0,0,0], [0,10,0]), d=1 )
    circleA = cmds.circle(c=(0,11,0), nr = [1,0,0])
    circleB = cmds.circle(c=(0,11,0), nr = [0,1,0])
    circleC = cmds.circle(c=(0,11,0), nr = [0,0,1])
    pinControl = cmds.parent (cmds.listRelatives(circleA, s=1),cmds.listRelatives(circleB, s=1),cmds.listRelatives(circleC, s=1), pinCtl, s=1, r=1)
    cmds.delete(circleA,circleB,circleC)
    return pinCtl

jntSel = cmds.ls(sl=1)
jntName = jntSel[0].split("_JNT")
ctl = pinControl()
controlPin = cmds.rename(ctl, (jntName[0] + "FK_CTL"))
cmds.select(cl=1)
offGrp = cmds.group(empty=1, n=(jntName[0] + "FKOffset_GRP"))
cmds.parent(controlPin,offGrp)
parCon = cmds.parentConstraint(jntSel[0], offGrp, mo=0)
cmds.delete(parCon)

########################## Cube Control ##########################

from maya import cmds

def cubeControl():
    cube = cmds.curve(d= 1, p=[ (1,1,1),(-1,1,1),(-1,-1,1),(1,-1,1),(1,1,1),(1,1,-1),(1,-1,-1), (-1,-1,-1), (-1,1,-1), (1,1,-1), (-1,1,-1),(-1,1,1), (-1,-1,1),(-1,-1,-1), (1,-1,-1), (1,-1,1)])
    return cube

jntSel = cmds.ls(sl=1)
jntName = jntSel[0].split("_JNT")
ctl = cubeControl()
controlCube = cmds.rename(ctl, (jntName[0] + "FK_CTL"))
cmds.select(cl=1)
offGrp = cmds.group(empty=1, n=(jntName[0] + "FKOffset_GRP"))
cmds.parent(controlCube ,offGrp)
parCon = cmds.parentConstraint(jntSel[0], offGrp, mo=0)
cmds.delete(parCon)

########################## Circle Control ##########################

from maya import cmds

def circleControl():
    circleCtl = cmds.circle( ch=0, o=1, nr = [1,0,0])[0]
    return circleCtl

jntSel = cmds.ls(sl=1)
jntName = jntSel[0].split("_JNT")
ctl = circleControl()
controlCircle = cmds.rename(ctl, (jntName[0] + "FK_CTL"))
cmds.select(cl=1)
offGrp = cmds.group(empty=1, n=(jntName[0] + "FKOffset_GRP"))
cmds.parent(controlCircle ,offGrp)
parCon = cmds.parentConstraint(jntSel[0], offGrp, mo=0)
cmds.delete(parCon)

########################## Diamond Control ##########################

from maya import cmds

def diamondControl():
    diamond = cmds.curve(d= 1, p=[ (0 ,1, 0),( 0, 0, 1),( 0 ,-1, 0), (0 ,0 ,-1), (0, 1, 0) , (-1 ,0,0) ,(0 ,-1 ,0) ,( 1,0 ,0), (0, 1, 0), (-1 ,0 ,0), (0, 0,1), (1 ,0 ,0) , (0 ,0 ,-1) ,( -1 ,0, 0)])
    return diamond

jntSel = cmds.ls(sl=1)
jntName = jntSel[0].split("_JNT")
ctl = diamondControl()
controlDiamond = cmds.rename(ctl, (jntName[0] + "FK_CTL"))
cmds.select(cl=1)
offGrp = cmds.group(empty=1, n=(jntName[0] + "FKOffset_GRP"))
cmds.parent(controlDiamond ,offGrp)
parCon = cmds.parentConstraint(jntSel[0], offGrp, mo=0)
cmds.delete(parCon)

########################## Double Arrow Control ##########################

from maya import cmds

def doubleArrowControl():
    double_arrow = cmds.curve(d= 1, p=[ (-4 ,0, 0), (-2, 0, -2), (-2,0,-1), (2,0,-1), (2,0,-2), (4,0,0), (2,0,2), (2,0,1), (-2,0,1), (-2,0,2), (-4,0,0)])
    return doubleArrow

jntSel = cmds.ls(sl=1)
jntName = jntSel[0].split("_JNT")
ctl = doubleArrowControl()
controlDoubleArrow = cmds.rename(ctl, (jntName[0] + "FK_CTL"))
cmds.select(cl=1)
offGrp = cmds.group(empty=1, n=(jntName[0] + "FKOffset_GRP"))
cmds.parent(controlDoubleArrow ,offGrp)
parCon = cmds.parentConstraint(jntSel[0], offGrp, mo=0)
cmds.delete(parCon)

########################## Arrow Control ##########################

from maya import cmds

def arrowControl():
    arrow = cmds.curve(d= 1, p=[ (-4 ,0, 0), (-2, 0, -2), (-2,0,-1), (2,0,-1), (2,0,-1), (2,0,1), (-2,0,1), (-2,0,2), (-4,0,0)])
    return arrow

jntSel = cmds.ls(sl=1)
jntName = jntSel[0].split("_JNT")
ctl = arrowControl()
controlArrow = cmds.rename(ctl, (jntName[0] + "FK_CTL"))
cmds.select(cl=1)
offGrp = cmds.group(empty=1, n=(jntName[0] + "FKOffset_GRP"))
cmds.parent(controlArrow ,offGrp)
parCon = cmds.parentConstraint(jntSel[0], offGrp, mo=0)
cmds.delete(parCon)
