import locale
import sys

class Base_Model():
    trim = 'normal'
    engine_litres = 1.5
    miles_range = 450
    tank_capacity = 45
    color = 'white'
    transmission = 'automatic'

    def __init__(self,price, transmission='automatic', color='white'):
        self.price = price
        self.transmission = transmission
        self.color = color

    def __str__(self):
        return 'a %s base model with %s transmission' %(self.color, self.transmission)
    
    @staticmethod
    def miles_per_liter(miles_range, tank_capacity):
        return miles_range/tank_capacity

    def miles_per_gallon(miles_range, tank_capacity):
        return Base_Model.miles_per_liter(miles_range, tank_capacity) * 3.78541
    miles_per_gallon = staticmethod(miles_per_gallon)

    def info(self):
        if sys.platform.startswith('win'):
            locale.setlocale(locale.LC_ALL, 'us')
        else:
            locale.setlocale(locale.LC_ALL, 'en_US.utf8')
        print('The price of %s was %s.' %(self, locale.currency(self.price)))
 

coop = Base_Model(color='green', transmission='automatic', price=25000)
coop.info()
print('the %s gets %4.2f miles per gallon' %(coop, coop.miles_per_gallon(coop.miles_range, coop.tank_capacity)))
print('the %s gets %4.2f miles per gallon' %(Base_Model, Base_Model.miles_per_gallon(Base_Model.miles_range, Base_Model.tank_capacity)))

class Sport_model(Base_Model):
    engine_litres = 2.0
    miles_range = 400

coop_sport = Sport_model(color='red', transmission='manual', price=26300)
coop_sport.info()
print('the %s gets %4.2f miles per gallon' %(coop_sport, coop_sport.miles_per_gallon(coop_sport.miles_range, coop_sport.tank_capacity)))
print('the %s gets %4.2f miles per gallon' %(Sport_model, Sport_model.miles_per_gallon(Sport_model.miles_range, Sport_model.tank_capacity)))
