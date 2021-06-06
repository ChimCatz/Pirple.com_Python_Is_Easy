# -----------------------------------------------------------------------------------
# HOMEWORK #9: CLASSES
# -----------------------------------------------------------------------------------


class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needs_maintenance = False
        self.trips_since_maintenance = 0

    def repair(self):
        self.needs_maintenance = False
        self.trips_since_maintenance = 0


class Car(Vehicle):
    def __init__(self, make, model, year, weight):
        super(Car, self).__init__(make, model, year, weight)
        self.is_driving = False

    def drive(self):
        self.is_driving = True
        self.trips_since_maintenance += 1

        if self.trips_since_maintenance > 100:
            self.needs_maintenance = True

    def stop(self):
        self.is_driving = False


bugatti = Car(make='S.A.S', model='2015', year=2015, weight=1838)
koenigsegg = Car(make='AB', model='Agera', year=2018, weight=1395)
nissan = Car(make='Nissan', model='R35', year=2007, weight=1740)

bugatti.drive()
bugatti.drive()
koenigsegg.drive()
nissan.drive()
bugatti.drive()
bugatti.drive()
nissan.drive()

sentence = '{} is a {} {} built in {} weighing {}kg.\nIt was used {} times since its last maintenance and it is {} that it needs another.\n\n'

print(sentence.format('The Bugatti Veyron', bugatti.make, bugatti.model, bugatti.year, bugatti.weight,
                      bugatti.trips_since_maintenance, str(bugatti.needs_maintenance).lower()))
print(sentence.format('koenigsegg', koenigsegg.make, koenigsegg.model, koenigsegg.year, koenigsegg.weight, koenigsegg.trips_since_maintenance,
                      str(koenigsegg.needs_maintenance).lower()))
print(sentence.format('Enzo\'sride', nissan.make, nissan.model, nissan.year, nissan.weight,
                      nissan.trips_since_maintenance, str(nissan.needs_maintenance).lower()))

nissan.trips_since_maintenance = 100
nissan.drive()

print(
    f'Jin is a prolific driver and it is {str(nissan.needs_maintenance).lower()} that his car needs maintenance.\n')


# ---------------------------------extra--------------------------------------------------


class Plane(Vehicle):
    def __init__(self, make, model, year, weight):
        super().__init__(make, model, year, weight)
        self.is_flying = False

    def fly(self):
        if self.needs_maintenance:
            print('This plane cannot take off until repaired.')
        else:
            self.is_flying = True
            self.trips_since_maintenance += 1

    def land(self):
        self.is_flying = False


comac = Plane('Airliner', 'C919', 2011, 450000)

print(sentence.format('The Comac C919', comac.make, comac.model, comac.year, comac.weight,
                      comac.trips_since_maintenance, str(comac.needs_maintenance).lower()))

comac.fly()
print('It is flying:', comac.is_flying)
comac.land()
print('The Comac is flying:', comac.is_flying)
comac.needs_maintenance = True
comac.fly()
