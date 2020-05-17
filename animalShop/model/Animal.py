class Animal:

    def __init__(self, name=None, age_in_months=None, sex=None, biological_class=None, height_in_meters=None, length_in_meters=None, food_per_day_in_kg=None, food_type=None, price_in_UAH=None):
        self.name = name
        self.age_in_months = age_in_months
        self.sex = sex
        self.biological_class = biological_class
        self.height_in_meters = height_in_meters
        self.length_in_meters = length_in_meters
        self.food_per_day_in_kg = food_per_day_in_kg
        self.food_type = food_type
        self.price_in_UAH = price_in_UAH

    def __del__(self):
        return

    def __str__(self):
        name = 'Name: {}\n'.format(self.name)
        age_in_months = 'Age: {}\n'.format(self.age_in_months)
        sex = 'Sex: {}\n'.format(self.sex)
        biological_class = 'Class: {}\n'.format(self.biological_class)
        height_in_meters = 'Height: {}\n'.format(self.height_in_meters)
        length_in_meters = 'Length: {}\n'.format(self.length_in_meters)
        food_per_day_in_kg = 'Food amount: {}\n'.format(self.food_per_day_in_kg)
        food_type = 'Food type: {}\n'.format(self.food_type)
        price_in_UAH = 'Price: {}\n'.format(self.price_in_UAH)
        return name + age_in_months + sex + biological_class + height_in_meters + length_in_meters + food_per_day_in_kg + food_type + price_in_UAH


class Bird:

    def __init__(self, wing_span_in_meters=None, nest_form=None):
        self.wing_span_in_meters = wing_span_in_meters
        self.nest_form = nest_form

    def __del__(self):
        return

    def __str__(self):
        wing_span_in_meters = f'Wing span: {self.wing_span_in_meters}'
        nest_form = f'Nest form: {self.nest_form}'
        return wing_span_in_meters + nest_form

class Fish:

    def __init__(self, caviar_count_per_season=None):
        self.caviar_count_per_season = caviar_count_per_season

    def __del__(self):
        return

    def __str__(self):
        caviar_count_per_season = f'Caviar count: {self.caviar_count_per_season}'
        return caviar_count_per_season

class Mammal:

    def __init__(self, fur_length_in_meters=None):
        self.fur_length_in_meters = fur_length_in_meters

    def __del__(self):
        return

    def __str__(self):
        fur_length_in_meters = f'Fur length: {self.fur_length_in_meters}'
        return fur_length_in_meters