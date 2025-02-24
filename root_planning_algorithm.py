# Function to calculate the total distance and fuel used for a route
def calculate_fuel_consumption(van, route):
    """
    This function figures out how far the van travels and how much fuel it burns.
    - van: A tuple like (capacity, fuel_per_km) that describes the van's capacity and fuel efficiency.
    - route: A list of stops the van makes, like [(0, "start"), (-1, "pick"), ...].
    Returns: Total distance (in km) and total fuel used.
    """
    _, fuel_per_km = van  # Grab the van's fuel efficiency (fuel used per km)
    total_distance = 0  # Start counting the distance from zero
    previous_location = 0  # The van begins its journey at the warehouse (position 0)
    
    # Go through each stop in the route
    for location, _ in route:
        # Calculate the distance from the last stop to this one
        distance = abs(location - previous_location)
        total_distance += distance  # Add this distance to the total
        previous_location = location  # Update the last stop to the current one
    
    # Calculate the total fuel used: distance × fuel efficiency
    fuel_used = total_distance * fuel_per_km
    return total_distance, fuel_used


# Function to plan the best route for the van to deliver all packages
def plan_best_route(van_capacity, packages):
    """
    This function plans the most efficient route for the van to pick up and deliver all packages.
    - van_capacity: The maximum weight the van can carry at once.
    - packages: A list of packages, each with a pickup location, dropoff location, and weight.
    Returns: A list of stops the van will make, like [(0, "start"), (-1, "pick"), ...].
    """
    # Sort the packages by pickup location, starting with the ones closest to the warehouse
    sorted_packages = sorted(packages, key=lambda pkg: abs(pkg[0]))
    
    # Start the route at the warehouse
    route = [(0, "start")]
    current_load = 0  # Track how much weight the van is carrying
    delivered_packages = set()  # Keep track of which packages have been delivered
    
    # Keep planning the route until all packages are delivered
    while len(delivered_packages) < len(packages):
        # Pick up packages until the van is full
        for pkg in sorted_packages:
            pickup_location, dropoff_location, weight = pkg
            # If the package hasn't been delivered and the van can carry it, pick it up
            if pkg not in delivered_packages and current_load + weight <= van_capacity:
                route.append((pickup_location, "pick"))  # Add the pickup stop to the route
                current_load += weight  # Update the van's current load
                delivered_packages.add(pkg)  # Mark the package as picked up
        
        # Deliver all the packages the van has picked up
        for pkg in sorted_packages:
            pickup_location, dropoff_location, weight = pkg
            # If the package has been picked up but not delivered, drop it off
            if pkg in delivered_packages and (dropoff_location, "drop") not in route:
                route.append((dropoff_location, "drop"))  # Add the drop-off stop to the route
                current_load -= weight  # Update the van's current load
        
        # If there are more packages to pick up, continue without going back to the warehouse
        if len(delivered_packages) < len(packages):
            # Find the next package to pick up
            next_pkg = next((pkg for pkg in sorted_packages if pkg not in delivered_packages), None)
            if next_pkg:
                route.append((next_pkg[0], "pick"))  # Add the pickup stop to the route
                current_load += next_pkg[2]  # Update the van's current load
                delivered_packages.add(next_pkg)  # Mark the package as picked up
    
    # Return to the warehouse at the end of the route
    route.append((0, "end"))
    
    return route


# Function to find the best van and its most fuel-efficient route
def find_best_van_and_route(vans, packages):
    """
    This function finds the best van and the most fuel-efficient route to deliver all packages.
    - vans: A list of vans, each described by (capacity, fuel_per_km).
    - packages: A list of packages, each with a pickup location, dropoff location, and weight.
    Returns: The best van, the optimal route, total distance, and total fuel used.
    """
    best_van = None  # Track the best van
    best_route = None  # Track the best route
    min_fuel = float('inf')  # Track the minimum fuel used (start with infinity)
    min_distance = float('inf')  # Track the minimum distance traveled (start with infinity)
    
    # Try each van to find the best one
    for van in vans:
        van_capacity, _ = van  # Grab the van's capacity
        # Plan the best route for this van
        route = plan_best_route(van_capacity, packages)
        
        # Calculate the total distance and fuel used for this route
        distance, fuel = calculate_fuel_consumption(van, route)
        
        # If this route uses less fuel, update the best van and route
        if fuel < min_fuel:
            min_fuel = fuel
            min_distance = distance
            best_van = van
            best_route = route
    
    return best_van, best_route, min_distance, min_fuel


# Function to find the most fuel-efficient routes for multiple vans
def find_optimal_route_for_multiple_vans(vans, packages):
    """
    This function finds the most fuel-efficient routes for multiple vans to deliver all packages.
    - vans: A list of vans, each described by (capacity, fuel_per_km).
    - packages: A list of packages, each with a pickup location, dropoff location, and weight.
    Returns: A list of tuples, where each tuple contains:
             - The van used.
             - The optimal route for that van.
             - The distance traveled by that van.
             - The fuel used by that van.
    """
    # Sort vans by fuel efficiency (most efficient first)
    sorted_vans = sorted(vans, key=lambda van: van[1])
    
    # Sort packages by weight (heaviest first)
    sorted_packages = sorted(packages, key=lambda pkg: pkg[2], reverse=True)
    
    van_routes = []
    undeliverable_packages = []
    
    for van in sorted_vans:
        van_capacity, _ = van
        van_packages = []
        remaining_packages = []
        
        # Assign packages to the current van
        for pkg in sorted_packages:
            if pkg[2] <= van_capacity:
                van_packages.append(pkg)
                van_capacity -= pkg[2]
            else:
                remaining_packages.append(pkg)
        
        # Plan the route for the current van
        if van_packages:
            route = plan_best_route(van[0], van_packages)
            distance, fuel = calculate_fuel_consumption(van, route)
            van_routes.append((van, route, distance, fuel))
        
        # Update the list of remaining packages
        sorted_packages = remaining_packages
    
    # Check for undeliverable packages
    for pkg in sorted_packages:
        if all(pkg[2] > van[0] for van in vans):
            undeliverable_packages.append(pkg)
    
    # If there are undeliverable packages, notify the user
    if undeliverable_packages:
        print("Warning: The following packages cannot be delivered by any van:")
        for pkg in undeliverable_packages:
            print(f"Package with weight {pkg[2]} (Pickup: {pkg[0]}, Dropoff: {pkg[1]})")
    
    return van_routes


# Function to take input from the user with validation
def take_user_input():
    """
    This function takes input from the user for vans and packages, with validation.
    Returns: A tuple containing:
             - A list of vans (capacity, fuel_per_km).
             - A list of packages (pickup_location, dropoff_location, weight).
    """
    vans = []
    packages = []
    
    # Input for vans (max 3 vans)
    num_vans = int(input("Enter the number of vans (max 3): "))
    if num_vans > 3:
        print("Error: Maximum of 3 vans allowed.")
        return [], []
    
    for i in range(num_vans):
        print(f"Enter details for Van {i+1}:")
        capacity = int(input("  Capacity: "))
        fuel_per_km = int(input("  Fuel per km: "))
        vans.append((capacity, fuel_per_km))
    
    # Input for packages (max 5 packages)
    num_packages = int(input("Enter the number of packages (max 5): "))
    if num_packages > 5:
        print("Error: Maximum of 5 packages allowed.")
        return [], []
    
    for i in range(num_packages):
        print(f"Enter details for Package {i+1}:")
        pickup = int(input("  Pickup location: "))
        dropoff = int(input("  Dropoff location: "))
        weight = int(input("  Weight: "))
        
        # Check if the package weight exceeds the capacity of all vans
        if all(weight > van[0] for van in vans):
            print(f"Error: Package {i+1} weight ({weight}) exceeds the capacity of all vans.")
            return [], []
        
        packages.append((pickup, dropoff, weight))
    
    return vans, packages


# Main program
if __name__ == "__main__":
    # Take input from the user
    vans, packages = take_user_input()
    
    # Check if input is valid
    if not vans or not packages:
        print("Invalid input. Exiting program.")
    else:
        # Find the best van and route (single van)
        print("\nSingle Van Solution:")
        selected_van, optimal_route, route_length, fuel_used = find_best_van_and_route(vans, packages)
        print(f"Selected Van: {selected_van}")
        print(f"Optimal Route: {optimal_route}")
        print(f"Route Length: {route_length} km")
        print(f"Fuel Used: {fuel_used} units")
        print()
        
        # Find the optimal routes for multiple vans
        print("Multiple Vans Solution:")
        results = find_optimal_route_for_multiple_vans(vans, packages)
        for van, route, distance, fuel in results:
            print(f"Van: {van}")
            print(f"Route: {route}")
            print(f"Distance: {distance} km")
            print(f"Fuel Used: {fuel} units")
            print()