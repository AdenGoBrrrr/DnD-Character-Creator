from classes import *
from spells import *
from items import *
from races import *
from characters import *


def build_artificer():
    pass

def build_barbarian():
    pass

def build_bard():
    pass

def build_cleric():
    pass

def build_druid():
    pass

def build_fighter():
    pass

def build_monk():
    pass

def build_paladin():
    hit_die = 10
    spell_slots_by_level = {1: [0,0,0,0,0,0,0,0,0],
                            2: [2,0,0,0,0,0,0,0,0],
                            3: [3,0,0,0,0,0,0,0,0],
                            4: [3,0,0,0,0,0,0,0,0],
                            5: [4,2,0,0,0,0,0,0,0],
                            6: [4,2,0,0,0,0,0,0,0],
                            7: [4,3,0,0,0,0,0,0,0],
                            8: [4,3,0,0,0,0,0,0,0],
                            9: [4,3,2,0,0,0,0,0,0],
                            10: [4,3,2,0,0,0,0,0,0],
                            11: [4,3,3,0,0,0,0,0,0],
                            12: [4,3,3,0,0,0,0,0,0],
                            13: [4,3,3,1,0,0,0,0,0],
                            14: [4,3,3,1,0,0,0,0,0],
                            15: [4,3,3,2,0,0,0,0,0],
                            16: [4,3,3,2,0,0,0,0,0],
                            17: [4,3,3,3,1,0,0,0,0],
                            18: [4,3,3,3,1,0,0,0,0],
                            19: [4,3,3,3,2,0,0,0,0],
                            20: [4,3,3,3,2,0,0,0,0] }
    pass

def build_ranger():
    pass

def build_rogue():
    pass

def build_sorcerer():
    pass

def build_warlock():
    pass

def build_wizard():
    pass

def build_classes():
    build_artificer()
    build_barbarian()
    build_bard()
    build_cleric()
    build_druid()
    build_fighter()
    build_monk()
    build_paladin()
    build_ranger()
    build_rogue()
    build_sorcerer()
    build_warlock()
    build_wizard()

def main():
    build_classes()