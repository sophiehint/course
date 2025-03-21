

# Function 1: Train Cargo capacities from Austria (AT) to Poland (PL) per year
european_train_routes = 35000  # Total number of train routes in Europe
european_train_cargo_capacity_per_route = 300  # in tonnes (average capacity of each route)
relative_share_AT_PL = 0.01 # AT to PL train routes relative to whole EU train routes

def get_train_routes_and_capacities(european_train_routes, european_train_cargo_capacity_per_route, relative_share_AT_PL):
    total_cargo_capacity_AT_to_PL = european_train_routes * european_train_cargo_capacity_per_route * relative_share_AT_PL
    return total_cargo_capacity_AT_to_PL

total_cargo_capacity_solution = get_train_routes_and_capacities(european_train_routes, european_train_cargo_capacity_per_route, relative_share_AT_PL)
print(f"Annual total Cargo Capacity from AT to PL: {total_cargo_capacity_solution}")


# Function 2: Calculate how much Photovoltaik module scrap could be transported per year from Austria to Poland
photovoltaik_scrap_generated_annual_AT = 200000 # tonnes
transport_factor = 0.7

def calculate_photovoltaik_scrap_transport_per_year(photovoltaik_scrap_generated_annual_AT, transport_factor):
    scrap_transportable_from_AT_to_PL = photovoltaik_scrap_generated_annual_AT * transport_factor
    return scrap_transportable_from_AT_to_PL

scrap_transportable_from_AT_to_PL_solution = calculate_photovoltaik_scrap_transport_per_year(photovoltaik_scrap_generated_annual_AT, transport_factor)
print(f"Annual scrap transportable from AT to PL: {scrap_transportable_from_AT_to_PL_solution}")


# Function 3: Calculate how much Photovoltaik module scrap could be transported between 2030 and 2050
years = 20

def calculate_photovoltaik_scrap_transport_2030_2050(scrap_transportable_from_AT_to_PL_solution, years):
    total_scrap_transport = scrap_transportable_from_AT_to_PL_solution * years
    return total_scrap_transport

total_scrap_transport_solution = calculate_photovoltaik_scrap_transport_2030_2050(scrap_transportable_from_AT_to_PL_solution, years)
print(f"Total scrap transport from AT to PL 2030 to 2050: {total_scrap_transport_solution}")

# Function 4: To check if enough train cargo capacity for transportation exists
def enough_train_cargo_capacity(scrap_transportable_from_AT_to_PL_solution, total_cargo_capacity_solution):
    enough = scrap_transportable_from_AT_to_PL_solution / total_cargo_capacity_solution
    return enough

enough_solution = enough_train_cargo_capacity(140000, 105000)
print(f"if > 1 then we have not enough train cargo capacity to transport all the scrap from AT to PL; if < 1 we have enough: {enough_solution}")

