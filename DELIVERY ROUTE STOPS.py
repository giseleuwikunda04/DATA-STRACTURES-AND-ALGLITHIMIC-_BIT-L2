from array import array

print("=== Project 118: Delivery Route Stops ===\n")

# -----------------------------
# 🔢 Integers: Route Stops Data
# -----------------------------
route_stops = [12, 18, 9, 21, 15, 17, 14]

# Calculations
total_stops = sum(route_stops)
average_stops = total_stops / len(route_stops)
min_stops = min(route_stops)
max_stops = max(route_stops)

# -----------------------------
# 🔤 Strings: Formatted Report
# -----------------------------
report = (
    f"Total Delivery Route Stops: {total_stops}\n"
    f"Average Stops per Route: {average_stops:.2f}\n"
    f"Minimum Stops in a Route: {min_stops}\n"
    f"Maximum Stops in a Route: {max_stops}"
)
print(">> Route Stop Report")
print(report)

# --------------------------------------
# ✅ Booleans: Threshold & Status Check
# --------------------------------------
threshold = 16
if average_stops > threshold and max_stops > 20:
    print("\n>> Status: Above Standard\n")
else:
    print("\n>> Status: Below Standard\n")

# -----------------------------
# 📋 Lists: Modify & Display
# -----------------------------
print(">> Route Stops List - Original:")
print(route_stops)

# Add a new route
route_stops.append(13)

# Remove routes with less than 10 stops
route_stops = [stop for stop in route_stops if stop >= 10]

# Sort list
route_stops.sort()

print(">> Route Stops List - Modified & Sorted:")
print(route_stops)

# -----------------------------
# 📦 Arrays: Fixed-Size Subset
# -----------------------------
stops_array = array('i', route_stops[:5])  # First 5 elements

array_sum = sum(stops_array)
list_sum = sum(route_stops)

print(f"\n>> Array Sum (First 5 Stops): {array_sum}")
print(f">> Total Sum from List: {list_sum}")

# -----------------------------
# 📚 Dictionaries: Route Records
# -----------------------------
routes_data = [
    {'id': 1, 'name': 'Route A', 'value': 12},
    {'id': 2, 'name': 'Route B', 'value': 18},
    {'id': 3, 'name': 'Route C', 'value': 9},
    {'id': 4, 'name': 'Route D', 'value': 21}
]

# Update Route C
for route in routes_data:
    if route['id'] == 3:
        route['value'] = 14

# Delete Route B
routes_data = [route for route in routes_data if route['id'] != 2]

# Compute total value
total_value = sum(route['value'] for route in routes_data)

print("\n>> Updated Route Records:")
for route in routes_data:
    print(route)

print(f"\n>> Total 'value' from Route Records: {total_value}")
