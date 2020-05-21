import doctest
from animalShop.model.Animal import Animal
from animalShop.model.BiologicalClass import BiologicalClass
from animalShop.model.Sex import Sex


class AnimalManager:

    def __init__(self, animal_list=None):
        if animal_list is None:
            self.animal_list = []
        else:
            self.animal_list = animal_list

    def __del__(self):
        return

    def find_animals_by_biological_class(self, biological_class_to_find: BiologicalClass):
        """
        >>> animal1 = Animal('Birdie', 12, Sex.MALE, BiologicalClass.BIRD, 1, 1, 0.5, 'seeds', 100)
        >>> animal2 = Animal('Goldie', 6, Sex.FEMALE, BiologicalClass.FISH, 2, 1, 3, 'worms', 450)
        >>> animal3 = Animal('Kitty', 9, Sex.MALE, BiologicalClass.MAMMAL, 0.8, 0.7, 1.5, 'meat', 600)
        >>> animals = [animal1, animal2, animal3]
        >>> manager = AnimalManager(animals)
        >>> print(manager.find_animals_by_biological_class(BiologicalClass.BIRD))
        ['Birdie']
        >>> print(manager.find_animals_by_biological_class(BiologicalClass.FISH))
        ['Goldie']
        >>> print(manager.find_animals_by_biological_class(BiologicalClass.MAMMAL))
        ['Kitty']
        """
        result_animals = []
        for animal in self.animal_list:
            if animal.biological_class == biological_class_to_find:
                result_animals.append(animal.name)
            else:
                pass
        return result_animals


if __name__ == "__main__":
    doctest.testmod(verbose=True)
