from datetime import date
from math import ceil
from fuel_prices import PRICES

# kodėl nenurodant pvz. categories_present default value: SyntaxError: parameter without a default follows parameter with a default
class Driver:
    def __init__(self,
                 vacation_date: tuple[date, date] = None,
                 categories_present: set = None,
                 charge_for_km: float = 0.33,
                 fullname = "Ratenis Vairavičius",
                 binging_issues: bool = False
    ):
        self.vacation_date = vacation_date
        self.categories_present = categories_present
        self.charge_for_km = charge_for_km
        self.fullname = fullname
        self.binging_issues = binging_issues

class Vehicle:
    def __init__(self,
                 annual_mileage: int = 1,
                 license_plate: str = "",
                 fuel_type: str = "gasoline",
                 fuel_consumption: int = 5,
                 fixed_costs: int = 1000,
                 inspection_date: date = date(2000,1,1),
                 insurance_until: date = date(2000,1,1),
                 driver_category_required = "B",
    ):
        self.annual_mileage = annual_mileage
        self.license_plate = license_plate
        self.fuel_type = fuel_type
        self.fixed_costs = fixed_costs
        self.inspection_date = inspection_date
        self.insurance_until = insurance_until
        self.driver_category_required= driver_category_required
        self.fuel_consumption = fuel_consumption

    def if_driver_can_work(self, driver: Driver, when: date = date.today()) -> bool:
        # check for license
        if self.driver_category_required not in driver.categories_present:
            print(f"{driver.fullname} neturi tinkamos kategorijos.")
            return False
        print(f"{driver.fullname} turi tinkamą kategoriją,")

        #check if driver is not in vacation
        if driver.vacation_date and driver.vacation_date[0] <= when <= driver.vacation_date[1]:
            print(f"bet atostogauja nuo {driver.vacation_date[0]} iki {driver.vacation_date[1]}.")
            if driver.binging_issues:
                print("Ieškokite kito vairuotojo.")
            return False
        print("dirbti gali.")
        return True

    def if_papers_in_order(self) -> bool:
        inspection = self.check_inspection_term()
        insurance = self.check_insurance_term()
        return inspection and insurance


    def check_inspection_term(self) -> bool:
        print("Tikrinam technikinę...")
        expires_in = (self.inspection_date - date.today()).days
        if expires_in > 30:
            print(f"Techninė apžiūra tvarkoje, ji dar galios {expires_in}d.")
            return True
        elif expires_in > 0:
            print(f"DĖMESIO! Nepamirškite prasitęsti technikinęs, nes ji tegalios tik {expires_in}d.")
        else:
            print(f"DĖMESIO! Vairuoti negalima! Technikinė nebegalioja {-expires_in}d.")
        return False

    def check_insurance_term(self) -> bool:
        print("Tikrinam draudimą...")
        expires_in = (self.insurance_until - date.today()).days
        if expires_in > 30:
            print(f"Draudimas tvarkoje, jis dar galios {expires_in}d.")
            return True
        elif expires_in > 0:
            print(f"DĖMESIO! Nepamirškite prasitęsti draudimo, nes jis tegalios tik {expires_in}d.")
        else:
            print(f"DĖMESIO! Draudimas pasibaigęs prieš {-expires_in}d.!")
        return False

    def calculate_cost_per_km(self):
        # ! Calculates expenses for vehicle only, excluding driver's fee
        # apply .try for improving?
        cost_per_km = self.fixed_costs / self.annual_mileage + self.fuel_consumption/100 * PRICES[self.fuel_type]
        print(f"{self.fuel_consumption}l/100km,{self.fuel_type}({PRICES[self.fuel_type]}e/l), +fix: {round(cost_per_km, 2)}e/km,")
        return cost_per_km

# pasidomėti dėl (kw)argsų panaudojimo
class Car(Vehicle):
    def __init__(self,
                 annual_mileage,
                 license_plate,
                 fuel_type,
                 fuel_consumption,
                 fixed_costs,
                 inspection_date,
                 insurance_until,
    ):
        super().__init__(annual_mileage, license_plate, fuel_type, fuel_consumption,
                         fixed_costs, inspection_date, insurance_until, driver_category_required = "B")

class Bus(Vehicle):
    def __init__(self,
                 annual_mileage,
                 license_plate,
                 fuel_type,
                 fuel_consumption,
                 fixed_costs,
                 inspection_date,
                 insurance_until,
                 seating_capacity: int = 15
                 ):
        super().__init__(annual_mileage, license_plate, fuel_type, fuel_consumption, fixed_costs, inspection_date, insurance_until, driver_category_required = "C")
        self.seating_capacity = seating_capacity

    def calculate_trips(self, passengers: int):
        trips = ceil(passengers / self.seating_capacity)
        print(f"{trips} kelionių prireiks {passengers} keleivių nuvežimui.")
        return trips

    def calculate_estimate_cost(self, passengers: int, distance: int, driver: Driver, when = None):
        # checking drivers capability
        if not self.if_driver_can_work(driver, when):
            return False

        number_of_trips = self.calculate_trips(passengers = passengers)
        auto_charge_per_km = self.calculate_cost_per_km()
        total_cost = round(distance * number_of_trips * (auto_charge_per_km + driver.charge_for_km), 2)
        print(f"""
        Samata:
        *********
        Nuvežimo savikaina {total_cost}e:
        ---------
        {number_of_trips} reisų po {distance}km,
        Vairuotojo atlyginimas {driver.charge_for_km}e/km 
        Transporto dalis: {round(auto_charge_per_km, 2)}e/km
        **********
        """)
        return total_cost

class Truck(Vehicle):
    def __init__(self,
                 annual_mileage,
                 license_plate,
                 fuel_type,
                 fuel_consumption,
                 fixed_costs,
                 inspection_date,
                 insurance_until,
                 cargo_capacity,
                 wagon_option: bool = False,
                 wagon_capacity: int = 0,
                 ):
        super().__init__(annual_mileage, license_plate, fuel_type, fuel_consumption,
            fixed_costs, inspection_date, insurance_until, driver_category_required = "D")
        self.cargo_capacity = cargo_capacity
        self.wagon_option = wagon_option or wagon_capacity
        self.wagon_capacity = wagon_capacity

    def calculate_optimal_delivery(self, cargo_to_deliver):
        minimum_number_of_trips = ceil(cargo_to_deliver/(self.wagon_capacity + self.cargo_capacity))
        trips_without_wagon = minimum_number_of_trips
        capacity_to_check = self.cargo_capacity * minimum_number_of_trips

        while cargo_to_deliver > capacity_to_check:
            capacity_to_check += self.wagon_capacity
            trips_without_wagon -= 1

        print(f"Optimalu nuvežti {minimum_number_of_trips-trips_without_wagon} kartų su priekaba ir {trips_without_wagon} be, viso: {minimum_number_of_trips}.")

    def if_driver_can_work_with_truck(self, driver, when: date = date.today()):
        if self.if_driver_can_work(driver = driver, when = when):
            print(f"Gali vairuoti sunkvežimius {'su priekaba' if 'E' in driver.categories_present else 'be priekabos'}.")
            return True
        return False


#starting from this line there be code for testing
driver_steponas = Driver(
    # vacation_date=(date(2025, 1, 1), date(2025, 6, 30)),
    categories_present = {"A2","B","C","D"},
    charge_for_km = 0.33,
    fullname = "Steponas Kirilinamasapavičius"
)


car = Car(
    annual_mileage = 10000,
    license_plate = "CDK852",
    fuel_type = "petrol",
    fuel_consumption = 5,
    fixed_costs = 0,
    inspection_date = date(2001,5,1),
    insurance_until = date(2001,5,7),
)

bus = Bus(
    annual_mileage = 1000,
    license_plate = "CDB852",
    fuel_type = "gasoline",
    fuel_consumption = 5,
    fixed_costs = 1000,
    inspection_date = date(2025,1,1),
    insurance_until = date(2025,5,7),
    seating_capacity = 20
)

truck = Truck(
    annual_mileage=1000,
    license_plate="BBB888",
    fuel_type="gas",
    fuel_consumption=16,
    fixed_costs=1000,
    inspection_date=date(2025, 10, 1),
    insurance_until=date(2026, 5, 7),
    cargo_capacity = 12,
    wagon_capacity= 5,
)
# truck.calculate_optimal_delivery(cargo_to_deliver=36)
# truck.if_driver_can_work(driver_steponas)
# car.if_papers_in_order()

# bus.calculate_estimate_cost(passengers=20, distance=100, driver=driver_steponas)

# bus.calculate_estimate_cost(passengers=61, distance=100)
# bus.if_papers_in_order()