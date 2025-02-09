class Class:

    warlock_spell_level_per_level = {1: 1,
                                     2: 1,
                                     3: 2,
                                     4: 2,
                                     5: 3,
                                     6: 3,
                                     7: 4,
                                     8: 4,
                                     9: 5,
                                     10: 5,
                                     11: 5,
                                     12: 5,
                                     13: 5,
                                     14: 5,
                                     15: 5,
                                     16: 5,
                                     17: 5,
                                     18: 5,
                                     19: 5,
                                     20: 5}
    
    def __init__(self, name, hit_die, spell_slots_by_level, spell_levels_by_level, warlock_spell_slots_by_level, armour_proficiencies, weapon_proficiencies, tool_proficiencies, saving_throws_proficiencies, skills_proficiencies):
        self.__name = name
        self.__hit_die = hit_die
        self.__spell_slots_by_level = spell_slots_by_level
        self.__warlock_spell_slots_by_level = warlock_spell_slots_by_level
        self.__spell_levels_by_level = spell_levels_by_level
        self.subclasses = []
        self.spells = []
        self.cantrips = []
        self.features = []
        self.armour_proficiencies = armour_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.saving_throws_proficiencies = saving_throws_proficiencies
        self.skills_proficiencies = skills_proficiencies
        self.starting_equipment = []

    def add_subclass(self, subclass):
        self.subclasses.append(subclass)

    def add_spell(self, spell):
        self.spells.append(spell)

    def add_cantrip(self, cantrip):
        self.cantrips.append(cantrip)

    def add_starting_equipment(self, equipment):
        self.starting_equipment.append(equipment)

    @property
    def name(self):
        return self.__name

    def hit_die(self):
        return self.__hit_die
    
    def spell_slots_by_level(self):
        return self.__spell_slots_by_level
    
    def warlock_spell_slots_by_level(self):
        return self.__warlock_spell_slots_by_level

    def spell_level_by_level(self):
        return self.__spell_levels_by_level
    
    def __str__(self):
        string = f"{self.name}:\n subclasses: {self.subclasses}\n cantrips: {self.cantrips}\n spells: {self.spells}\n features: {self.features}\n armour proficiencies: {self.armour_proficiencies}\n weapon proficiencies: {self.weapon_proficiencies}\n tool proficiencies: {self.tool_proficiencies}\n saving throws proficiencies: {self.saving_throws_proficiencies}\n skills proficiencies: {self.skills_proficiencies}\n starting equipment: {self.starting_equipment}"
        return string


class SubClass:
    
    def __init__(self, name, features):
        self.__name = name
        self.spells = []
        self.cantrips = []
        self.features = features

    @property
    def name(self):
        return self.__name

class ClassFeature:
    
    ## This will be expanded on later

    def __init__(self, name, description, required_level):
        self.name = name 
        self.description = description
        self.level_required = required_level