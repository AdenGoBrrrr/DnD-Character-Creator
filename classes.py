class Class:
    
    def __init__(self, name, hit_die, spell_slots_by_level, armour_proficiencies, weapon_proficiencies, tool_proficiencies, saving_throws_proficiencies, skills_proficiencies):
        self.name = name
        self.__hit_die = hit_die
        self.__spell_slots_by_level = spell_slots_by_level
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
    def hit_die(self):
        return self.__hit_die
    
    def spell_slots_by_level(self):
        return self.__spell_slots_by_level
    
    def __str__(self):
        string = f"{self.name}:\n subclasses: {self.subclasses}\n cantrips: {self.cantrips}\n spells: {self.spells}\n features: {self.features}\n armour proficiencies: {self.armour_proficiencies}\n weapon proficiencies: {self.weapon_proficiencies}\n tool proficiencies: {self.tool_proficiencies}\n saving throws proficiencies: {self.saving_throws_proficiencies}\n skills proficiencies: {self.skills_proficiencies}\n starting equipment: {self.starting_equipment}"
        return string


class SubClass:
    pass

class ClassFeature:
    pass