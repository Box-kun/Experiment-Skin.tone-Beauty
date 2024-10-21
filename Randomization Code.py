import random
import csv

# List of unique events
events = ["MN", "MI", "MS", "FN", "FI", "FS"]

# Function to generate random combinations
def generate_random_combinations(events, n_combinations=60):  # Modify 'n_combinations' for more/less combinations
    random_combinations = []
    for _ in range(n_combinations):
        random.shuffle(events)
        random_combinations.append(events.copy())
    return random_combinations

# Generate random combinations
random_combinations = generate_random_combinations(events, n_combinations=60)  # Modify 'n_combinations' here

# Create the table data
headers = ["Combination #"] + [f"Event {i+1}" for i in range(len(events))]  # Table headers
table_data = [[f"{i+1}"] + combination for i, combination in enumerate(random_combinations)]

# Save to CSV file
csv_filename = 'randomized_run_order.csv'
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write the header
    writer.writerows(table_data)  # Write the table data

print(f"Table has been saved as {csv_filename}")
