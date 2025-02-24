# 🚚 Van Route Optimization & Fuel Consumption Calculator

Welcome to the **Van Route Optimization** program! 🚐💨 This tool helps plan the most **fuel-efficient** delivery routes and calculates the **fuel consumption** 🚗💧. Whether you have a single van or a small fleet 🚚🚚, this will help you optimize your logistics! 📦

## 📋 Features

- **Route Optimization**: 📍 Plan the best routes to pick up and deliver packages, minimizing distance and fuel usage! 🛣️
- **Fuel Calculation**: ⛽ Calculate the total distance traveled and fuel used based on van fuel efficiency and route details. 
- **Multiple Vans Support**: 🚐🚐 Optimize routes for multiple vans, choosing the best one for the job! 
- **User-Friendly**: 📝 Easy-to-follow prompts for entering van capacities, fuel efficiency, and package details.

## 🧑‍💻 Functions

### 1. `calculate_fuel_consumption(van, route)` ⛽📏
Calculates **total distance** and **fuel consumption** for a given van and route.
- **van**: 🛻 Tuple `(capacity, fuel_per_km)`, representing the van’s load capacity and fuel efficiency.
- **route**: 📍 List of stops `[(0, "start"), (2, "pick"), ...]`.

**Returns**: 🛣️ Total distance (km) and fuel used.

---

### 2. `plan_best_route(van_capacity, packages)` 📍🛣️
Plans the **best route** for delivering packages based on the van’s **capacity** and **package details**.
- **van_capacity**: 🛻 Max weight the van can carry.
- **packages**: 📦 List of packages with `(pickup_location, dropoff_location, weight)`.

**Returns**: 📍 The best route list showing stops like `[(0, "start"), (2, "pick"), ...]`.

---

### 3. `find_best_van_and_route(vans, packages)` 🚐💨
Finds the **best van** and **optimal route** to minimize **fuel usage** and **maximize capacity**.
- **vans**: 🚚 List of vans with `(capacity, fuel_per_km)`.
- **packages**: 📦 List of packages with `(pickup_location, dropoff_location, weight)`.

**Returns**: 🚐 Best van, optimal route, total distance, and fuel usage.

---

### 4. `find_optimal_route_for_multiple_vans(vans, packages)` 🚐🚐💨
Optimizes routes for **multiple vans** to balance **load** and minimize **fuel consumption**.
- **vans**: 🚚 List of vans with `(capacity, fuel_per_km)`.
- **packages**: 📦 List of packages.

**Returns**: 📍 List of routes for each van, including total distance and fuel used.

---

### 5. `take_user_input()` 📝💡
Prompts the user to input details for **vans** and **packages**, ensuring everything is validated correctly. 

**Returns**: 🛻 Tuple of vans and packages entered by the user.

---

## 🚀 How to Use

### 1️⃣ Input Van and Package Details 🛻📦

- Enter the number of vans (max 3) 🚐.
- Provide the **capacity** and **fuel efficiency** for each van 🚚💨.
- Enter details for each **package**: pickup & dropoff locations, and weight 📦🛠️.

### 2️⃣ Get the Best Route 🗺️

- The program will **calculate** the most efficient route for **one van** or **multiple vans**, making sure each van is used optimally 🚐💡.

### 3️⃣ View Results 📊

- After the calculations, you’ll see:
  - 🛻 The chosen van.
  - 📍 The optimal route.
  - 🚗 Total **distance** and **fuel usage**.

---

## 🔧 Example

Here's an example of how you’ll interact with the program:

```bash
👨‍💻 Enter the number of vans (max 3): 1
🚐 Enter details for Van 1:
  - Capacity: 1000 kg 🏋️‍♂️
  - Fuel per km: 5 liters/km ⛽

📦 Enter the number of packages (max 5): 2
📦 Enter details for Package 1:
  - Pickup location: 0 📍
  - Dropoff location: 10 📍
  - Weight: 500 kg 🏋️‍♂️

📦 Enter details for Package 2:
  - Pickup location: 20 📍
  - Dropoff location: 30 📍
  - Weight: 700 kg 🏋️‍♂️
