# Define the sets of flight destinations
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to
common_destinations = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", common_destinations)

# 2. Destinations unique to your airline
unique_to_our_airline = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_our_airline)

# 3. Whether there are any destinations that neither airline shares
all_destinations = our_routes.union(competitor_routes)
neither_airline_destinations = all_destinations.difference(our_routes).difference(competitor_routes)
print("Destinations neither airline shares:", neither_airline_destinations)
