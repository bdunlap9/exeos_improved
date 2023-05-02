from Utils.Offsets import *
from Utils.Utilities import is_pressed
"""
    Shoots if the trigger key is pressed, the CrossID is valid, and the teams are different.
    
    Parameters:
    pm (Pymem): Pymem object for memory manipulation.
    CrossID (int): ID of the entity the crosshair is on.
    client (int): Player's client module address.
    lTeam (int): Local player's team.
    CTeam (int): Crosshair entity's team.
    triggerkey (str): Keybind for the trigger.
"""

def shootTrigger(pm, CrossID, client, lTeam, CTeam, triggerkey):
    if is_pressed(triggerkey) and 0 < CrossID < 64 and lTeam != CTeam:
        pm.write_int(client + dwForceAttack, 6)
