class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.iscaught = False

mypokemon = Pokemon("Pikachu", ["Electric"])


class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })

squirtle = Pokemon("Squirtle", ["Water"])
squirtle.print_pokemon()

{
    "name": "Squirtle",
    "types": ["Water"],
    "is_caught": True
}
squirtle.is_caught = True
squirtle.print_pokemon()


class Pokemon:

    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({'name': self.name, 
               'types': self.types,
               'is_caught': self.is_caught
             })

    # New code:
    def catch(self):
        self.is_caught = True

class Pokemon():
    def  __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
        
    def print_pokemon(self):
        print( {
          "name": self.name,
          "types": self.types,
          "is_caught": self.is_caught
        })
  
    def catch(self):
        self.is_caught = True
      
    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")



class Pokemon():
    def  __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print( {
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })

    def catch(self):
        self.is_caught = True   

    def choose(self):
        if self.is_caught:
                print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

    # New Code
    def add_type(self, new_type):
        self.types.append(new_type)