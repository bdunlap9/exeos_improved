from Utils.Offsets import *
from math import *
from Utils.Vector3 import Vec3
from Utils.Offsets import *

def checkangles(x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True

def nanchecker(first, second):
    if isnan(first) or isnan(second):
        return False
    else:
        return True

def rcse_old(pm, player, engine_pointer, oldpunch, newrcs, punch, rcs):
    if pm.read_uint(player + m_iShotsFired) > 2:
        rcs.x = pm.read_float(engine_pointer + dwClientState_ViewAngles)
        rcs.y = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
        punch.x = pm.read_float(player + m_aimPunchAngle)
        punch.y = pm.read_float(player + m_aimPunchAngle + 0x4)
        newrcs.x = rcs.x - (punch.x - oldpunch.x) * 2
        newrcs.y = rcs.y - (punch.y - oldpunch.y) * 2
        oldpunch.x = punch.x
        oldpunch.y = punch.y
        if nanchecker(newrcs.x, newrcs.y) and checkangles(newrcs.x, newrcs.y):
            pm.write_float(engine_pointer + dwClientState_ViewAngles, newrcs.x)
            pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, newrcs.y)
    else:
        oldpunch.x = 0.0
        oldpunch.y = 0.0
        newrcs.x = 0.0
        newrcs.y = 0.0
    return oldpunch

def rcse(pm, player, engine_pointer, oldpunch, newrcs, punch, rcs, smoothing_factor=2.5):
    """
    Recoil control system for smoothing out recoil.

    Parameters:
    pm (Pymem): Pymem object for memory manipulation.
    player (int): Player's base address.
    engine_pointer (int): Engine pointer address.
    oldpunch (Vec2): Previous punch angle.
    newrcs (Vec2): New RCS angle.
    punch (Vec2): Current punch angle.
    rcs (Vec2): Current view angles.
    smoothing_factor (float, optional): Factor to determine the smoothness of recoil control. Default is 2.0.
    """
    if pm.read_uint(player + m_iShotsFired) > 2:
        rcs.x = pm.read_float(engine_pointer + dwClientState_ViewAngles)
        rcs.y = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
        punch.x = pm.read_float(player + m_aimPunchAngle)
        punch.y = pm.read_float(player + m_aimPunchAngle + 0x4)
        
        newrcs.x = rcs.x - (punch.x - oldpunch.x) * smoothing_factor
        newrcs.y = rcs.y - (punch.y - oldpunch.y) * smoothing_factor
        
        # Apply interpolation for smoother transition
        newrcs.x = rcs.x + (newrcs.x - rcs.x) / smoothing_factor
        newrcs.y = rcs.y + (newrcs.y - rcs.y) / smoothing_factor
        
        oldpunch.x = punch.x
        oldpunch.y = punch.y
        if nanchecker(newrcs.x, newrcs.y) and checkangles(newrcs.x, newrcs.y):
            pm.write_float(engine_pointer + dwClientState_ViewAngles, newrcs.x)
            pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, newrcs.y)
    else:
        oldpunch.x = 0.0
        oldpunch.y = 0.0
        newrcs.x = 0.0
        newrcs.y = 0.0
    return oldpunch
