# Function 1: Train Cargo capacities from Austria (AT) to Poland (PL) per year
def get_train_routes_and_capacities(european_train_routes, european_train_cargo_capacity_per_route, relative_share_AT_PL):
    total_cargo_capacity_AT_to_PL = european_train_routes * european_train_cargo_capacity_per_route * relative_share_AT_PL
    return total_cargo_capacity_AT_to_PL

# Function 2: Calculate how much Photovoltaik module scrap could be transported per year from Austria to Poland
def calculate_photovoltaik_scrap_transport_per_year(photovoltaik_scrap_generated_annual_AT, transport_factor):
    scrap_transportable_from_AT_to_PL = photovoltaik_scrap_generated_annual_AT * transport_factor
    return scrap_transportable_from_AT_to_PL

# Function 3: Calculate how much Photovoltaik module scrap could be transported between 2030 and 2050
def calculate_photovoltaik_scrap_transport_2030_2050(scrap_transportable_from_AT_to_PL_solution, years):
    total_scrap_transport = scrap_transportable_from_AT_to_PL_solution * years
    return total_scrap_transport

# Function 4: To check if enough train cargo capacity for transportation exists
def enough_train_cargo_capacity(scrap_transportable_from_AT_to_PL_solution, total_cargo_capacity_solution):
    enough = scrap_transportable_from_AT_to_PL_solution / total_cargo_capacity_solution
    return enough


# Test 1: Test get_train_routes_and_capacities function
def test_get_train_routes_and_capacities():
    european_train_routes = 35000
    european_train_cargo_capacity_per_route = 300
    relative_share_AT_PL = 0.01
    expected_capacity = european_train_routes * european_train_cargo_capacity_per_route * relative_share_AT_PL
    result = get_train_routes_and_capacities(european_train_routes, european_train_cargo_capacity_per_route, relative_share_AT_PL)
    assert result == expected_capacity, f"Expected {expected_capacity}, but got {result}"

# Test 2: Test calculate_photovoltaik_scrap_transport_per_year function
def test_calculate_photovoltaik_scrap_transport_per_year():
    photovoltaik_scrap_generated_annual_AT = 200000
    transport_factor = 0.7
    expected_scrap_transportable = photovoltaik_scrap_generated_annual_AT * transport_factor
    result = calculate_photovoltaik_scrap_transport_per_year(photovoltaik_scrap_generated_annual_AT, transport_factor)
    assert result == expected_scrap_transportable, f"Expected {expected_scrap_transportable}, but got {result}"

# Test 3: Test calculate_photovoltaik_scrap_transport_2030_2050 function
def test_calculate_photovoltaik_scrap_transport_2030_2050():
    scrap_transportable_from_AT_to_PL_solution = 140000
    years = 20
    expected_total_scrap_transport = scrap_transportable_from_AT_to_PL_solution * years
    result = calculate_photovoltaik_scrap_transport_2030_2050(scrap_transportable_from_AT_to_PL_solution, years)
    assert result == expected_total_scrap_transport, f"Expected {expected_total_scrap_transport}, but got {result}"

# Test 4: Test enough_train_cargo_capacity function
def test_enough_train_cargo_capacity():
    scrap_transportable_from_AT_to_PL_solution = 140000
    total_cargo_capacity_solution = 105000
    expected_enough_capacity = scrap_transportable_from_AT_to_PL_solution / total_cargo_capacity_solution
    result = enough_train_cargo_capacity(scrap_transportable_from_AT_to_PL_solution, total_cargo_capacity_solution)
    assert result == expected_enough_capacity, f"Expected {expected_enough_capacity}, but got {result}"


# Run all tests
def run_tests():
    print("Running tests...")

    try:
        test_get_train_routes_and_capacities()
        print("Test 1 passed: get_train_routes_and_capacities")
    except AssertionError as e:
        print(f"Test 1 failed: {e}")

    try:
        test_calculate_photovoltaik_scrap_transport_per_year()
        print("Test 2 passed: calculate_photovoltaik_scrap_transport_per_year")
    except AssertionError as e:
        print(f"Test 2 failed: {e}")

    try:
        test_calculate_photovoltaik_scrap_transport_2030_2050()
        print("Test 3 passed: calculate_photovoltaik_scrap_transport_2030_2050")
    except AssertionError as e:
        print(f"Test 3 failed: {e}")

    try:
        test_enough_train_cargo_capacity()
        print("Test 4 passed: enough_train_cargo_capacity")
    except AssertionError as e:
        print(f"Test 4 failed: {e}")


# Execute tests
if __name__ == "__main__":
    run_tests()
