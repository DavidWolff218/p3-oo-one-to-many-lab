class Pet:
    
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    
    all = []
    
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self) 
        
        
    @property
    def pet_type(self):
        print("retrieving...")
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            print("SETTING")
            self._pet_type = pet_type
        else:
            raise Exception("oops")
    
    def return_name(self):
        return self.name
    

class Owner:
    
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
        
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input object is not of type Pet")
        pet.owner = self
    
    # def get_sorted_pets(self):
    #     # pet_names = list(map(Pet.return_name, self.pets()))
    #     return(sorted(self.pets(), key=Pet.return_name))
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)