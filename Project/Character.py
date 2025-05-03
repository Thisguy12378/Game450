import json

class Character:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.loadCharacter()

    def loadCharacter(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.Load(f)
        except FileNotFoundError:
            print("Error: Character.json file not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding Character.json: {e}")
            return None
        
    def saveCharacter(self):
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.data, f, indent=4)
            print("Character.json updated successfully!")
        except Exception as e:
            print(f"Error saving Character.json: {e}")

    def updateStat(self, stat, value):
        match stat:
            case "vitality":
                self.data["vitality"] += value
                self.data["health"] *= 1.25
            case "strength":
                self.data["strength"] += value
                self.data["damage"] *= 1.25
            case "agility":
                self.data["agility"] += value
            case "intelligence":
                self.data["intelligence"] += value
                self.data["max_mana"] *= 1.25
            case "perception":
                self.data["perception"] += value
            case _:
                print(f"Stat {stat} not found in character.")
    
    def experience(self, exp):
        if "experience" not in self.data:
            self.data["experience"] = 0
        self.data["experience"] += exp
        
        if self.data["experience"] >= 100:
            self.data["experience"] -= self.data["experience_to_next_level"]
            self.data["experience_to_next_level"] *= 1.25
            
            self.level_up()

    def level_up(self):
        self.data["statPoints"] += 3
        print(f"Level up! You have {self.data['statPoints']} stat points to distribute.")
    
    def addToInventory(self, category, item):
        if "inventory" not in self.data:
            self.data["inventory"] = []
        self.data["inventory"][category].append(item)
    
    def removeFromInventory(self, category, item):
        if "inventory" in self.data and item in self.data["inventory"]:
            self.data["inventory"].remove(item)
            for i in self.data['equipment'][category]: # Come back here
                if i['name'] == item:
                    self.data['equipment'].remove(i)
                    break
        else:
            print(f"Item {item} not found in inventory.")

    def equipItem(self, item):
        slot = item["slot"]
        
        equipped = False

        if self.data["equipment"][slot] is not None:
            self.unequipItem(self.data["equipment"][slot])
        else:
            if "twoHanded" in item and item["twoHanded"]:
                self.datap["equipment"]["mainHand"] = item
                self.data["equipment"]["offHand"] = item
                equipped = True
            else:
                self.data["equipment"][slot] = item
                equipped = True
        
        if equipped:
            for stat, value in item["stats"].items():
                if stat in self.data:
                    self.data[stat] += value
                else:
                    self.data[stat] = value


    def unequipItem(self, item):
        slot = item["slot"]
        
        unequipped = True

        if slot == "mainHand":
            self.data["equipment"]["mainHand"] = None
        elif slot == "offHand":
            self.data["equipment"]["offHand"] = None
        elif slot == "armor":
            self.data["equipment"]["armor"] = None
        elif slot == "accessory":
            self.data["equipment"]["accessory"] = None
        else:
            unequipped = False

        if unequipped:
            for stat, value in item["stats"].items():
                if stat in self.data:
                    self.data[stat] -= value
                

    def display_character(self):
        print(json.dumps(self.data, indent=4))

    def displayInventory(self):
        if "inventory" in self.data:
            print(json.dumps(self.data["inventory"], indent=4))
        else:
            print("No inventory found.")

    def displayEquipment(self):
        if "equipment" in self.data:
            print(json.dumps(self.data["equipment"], indent=4))
        else:
            print("No equipment found.")

    