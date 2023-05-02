from Utils.Offsets import *
from Utils.Utilities import is_pressed

def Aimbot(pm, CrossID, client, lTeam, CTeam, triggerkey):
    if is_pressed(aimbotkey) and 0 < CrossID < 64 and lTeam != CTeam:
        bone_matrix = '' """ent.get_bone_position(entity[1], bone_ids.get(dpg.get_value('c_aimbot_bone')))"""


        pm.write_int(client + dwForceAttack, 6)
