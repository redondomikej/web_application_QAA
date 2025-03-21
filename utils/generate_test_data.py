import csv

# Define test data
test_data = [
    {"username": "student", "password": "Password123", "message": "Logged In Successfully"},
    {"username": "student", "password": "wrongpass", "message": "Invalid login"},
    {"username": "invalid", "password": "Password123", "message": "Invalid login"},
]

# CSV file path
csv_file = "utils/test_data.csv"

# Generate CSV file
def generate_csv():
    with open(csv_file, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password", "message"])
        writer.writeheader()  # Write column headers
        writer.writerows(test_data)  # Write test data
    print(f"✅ CSV file '{csv_file}' has been generated successfully!")

if __name__ == "__main__":
    generate_csv()
