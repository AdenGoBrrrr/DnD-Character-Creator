import random


class Character:

    full_spell_casters = ["Wizard", "Sorcerer", "Bard", "Cleric", "Druid"]
    half_spell_casters = ["Paladin", "Ranger", "Artificer"]
    third_spell_casters = ["Eldritch Knight", "Arcane Trickster"]
    
    def __init__(self, name, class_chosen, strength, dex, con, intelligence, wis, cha):
        self.name = name
        self.__max_hp = class_chosen.hit_die() + self.ability_scores["con"]
        self.level = 1
        self.classes = {class_chosen: 1}
        self.sub_classes = {class_chosen: None}
        self.ability_scores = {"str": strength, "dex": dex, "con": con, "int": intelligence, "wis": wis, "cha": cha}
        if class_chosen.name == "Warlock":
            self.warlock_spell_slots = class_chosen.spell_slots_by_level(1)
            self.spell_slots = [0,0,0,0,0,0,0,0,0]
        else:
            self.spell_slots = class_chosen.spell_slots_by_level(1)
            self.warlock_spell_slots = [0,0,0,0,0]
        

    def level_up(self, class_chosen):
        self.level += 1
        self.classes[class_chosen] += 1
        self.__max_hp += random.randint(class_chosen.hit_die())

        if self.classes[class_chosen] == 3:
            print(f"choose a subclass for {class_chosen.name}:\n")
            for subclass in class_chosen.subclasses:
                print(f"- {subclass.name}\n")
            while True:
                subclass_chosen = input()
                if subclass_chosen in class_chosen.subclasses:
                    self.sub_classes[class_chosen] = subclass_chosen
                    break
                else:
                    print("Invalid subclass, please choose a subclass from the list\n")

        if class_chosen.name in self.full_spell_casters:
            # add all spell slots together 
            pass
        elif class_chosen.name in self.half_spell_casters:
            # Add half of the spell slots together rounding down
            pass
        else:
            if self.sub_classes.items in self.third_spell_casters :
                # Use spell slots from the subclass
                pass

    @property
    def max_hp(self):
        return self.__max_hp