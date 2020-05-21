import doctest
from animalShop.model.Animal import Animal
from animalShop.model.BiologicalClass import BiologicalClass
from animalShop.model.Sex import Sex
from animalShop.model.SortType import SortType


class AnimalManagerUtils:

    def __init__(self, animals_list=None):
        if animals_list is None:
            self.animals_list = []
        else:
            self.animals_list = animals_list

    def __del__(self):
        return

    def sort_animals_by_name(self, type_of_sort: str):
        """
        >>> animal1 = Animal('Birdie', 12, Sex.MALE, BiologicalClass.BIRD, 1, 1, 0.5, 'seeds', 100)
        >>> animal2 = Animal('Goldie', 6, Sex.FEMALE, BiologicalClass.FISH, 2, 1, 3, 'worms', 450)
        >>> animal3 = Animal('Kitty', 9, Sex.MALE, BiologicalClass.MAMMAL, 0.8, 0.7, 1.5, 'meat', 600)
        >>> animal4 = Animal('Sunny', 5, Sex.MALE, BiologicalClass.BIRD, 0.4, 0.2, 0.6, 'seeds', 200)
        >>> animal5 = Animal('Oscar', 7, Sex.FEMALE, BiologicalClass.FISH, 1, 0.5, 1, 'worms', 520)
        >>> animals = [animal1, animal2, animal3, animal4, animal5]
        >>> manager_utils = AnimalManagerUtils(animals)
        >>> sorted_animals = manager_utils.sort_animals_by_name(SortType.ASCENDING.value)
        >>> for animal in sorted_animals: print(animal.name)
        Birdie
        Goldie
        Kitty
        Oscar
        Sunny
        >>> sorted_animals = manager_utils.sort_animals_by_name(SortType.DESCENDING.value)
        >>> for animal_1 in sorted_animals: print(animal_1.name)
        Sunny
        Oscar
        Kitty
        Goldie
        Birdie
        """
        sorted_animals = sorted(self.animals_list, key=lambda animal: animal.name)
        if type_of_sort == SortType.ASCENDING.value:
            return sorted_animals
        elif type_of_sort == SortType.DESCENDING.value:
            return sorted_animals[::-1]
        else:
            return sorted_animals

    def sort_animals_by_price(self, type_of_sort: str):
        """
        >>> animal1 = Animal('Birdie', 12, Sex.MALE, BiologicalClass.BIRD, 1, 1, 0.5, 'seeds', 100)
        >>> animal2 = Animal('Goldie', 6, Sex.FEMALE, BiologicalClass.FISH, 2, 1, 3, 'worms', 450)
        >>> animal3 = Animal('Kitty', 9, Sex.MALE, BiologicalClass.MAMMAL, 0.8, 0.7, 1.5, 'meat', 600)
        >>> animal4 = Animal('Sunny', 5, Sex.MALE, BiologicalClass.BIRD, 0.4, 0.2, 0.6, 'seeds', 200)
        >>> animal5 = Animal('Oscar', 7, Sex.FEMALE, BiologicalClass.FISH, 1, 0.5, 1, 'worms', 520)
        >>> animals = [animal1, animal2, animal3, animal4, animal5]
        >>> manager_utils = AnimalManagerUtils(animals)
        >>> sorted_animals = manager_utils.sort_animals_by_price(SortType.ASCENDING.value)
        >>> for animal in sorted_animals: print(animal.name)
        Birdie
        Sunny
        Goldie
        Oscar
        Kitty
        >>> sorted_animals = manager_utils.sort_animals_by_price(SortType.DESCENDING.value)
        >>> for animal_1 in sorted_animals: print(animal_1.name)
        Kitty
        Oscar
        Goldie
        Sunny
        Birdie
        """
        sorted_animals = sorted(self.animals_list, key=lambda animal: animal.price_in_UAH)
        if type_of_sort == SortType.ASCENDING.value:
            return sorted_animals
        elif type_of_sort == SortType.DESCENDING.value:
            return sorted_animals[::-1]


if __name__ == "__main__":
    doctest.testmod(verbose=True)
