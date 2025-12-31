# ✅ CSV File Operations
import csv

# -------------------------------
# Writing to a CSV file
# -------------------------------
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': 14, 'Grade': '9'})
    writer.writerow({'Name': 'Bob', 'Age': 15, 'Grade': '10'})
    writer.writerow({'Name': 'Charlie', 'Age': 13, 'Grade': '8'})

# -------------------------------
# Reading from a CSV file
# -------------------------------
print("\nReading data.csv:")
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}")
        print(row)

# -------------------------------
# Appending to a CSV file
# -------------------------------
with open('data.csv', 'a', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'Name': 'David', 'Age': 16, 'Grade': '11'})
    writer.writerow({'Name': 'Eva', 'Age': 14, 'Grade': '9'})

# -------------------------------
# Reading the updated CSV file
# -------------------------------
print("\nUpdated data.csv:")
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}")

# -------------------------------
# Reading from a CSV file with different delimiter and skipinitialspace
# -------------------------------
print("\nReading data1.csv (with ; delimiter):")
try:
    with open('data1.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', skipinitialspace=True)
        for row in reader:
            print(f"Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}")
            print(row)
except FileNotFoundError:
    print("⚠️ 'data1.csv' not found. Please create it with ';' as delimiter.")

# -------------------------------
# Reading with custom fieldnames
# -------------------------------
print("\nReading data2.csv (with custom fieldnames):")
try:
    with open('data2.csv', 'r') as csvfile:
        fnames = ['Name', 'Age', 'Grade']
        reader = csv.DictReader(csvfile, fieldnames=fnames, delimiter=';', skipinitialspace=True)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("⚠️ 'data2.csv' not found. Please create it with ';' as delimiter.")

# -------------------------------
# Writing using csv.writer
# -------------------------------
data = [
    ['name', 'age', 'city'],
    ['Abbot', 11, 'New York'],
    ['Ben', 12, 'Los Angeles'],
    ['Charlie', 13, 'Chicago']
]

with open('data3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
    writer.writerow(['David', 14, 'Houston'])
    writer.writerow(['Eva', 15, 'Phoenix'])

print("\ndata3.csv file created successfully!")

# -------------------------------
# Employee salary calculation
# -------------------------------
print("\nCalculating employee salary details...")

# Create a sample employee_details.csv file if not present
try:
    with open('employee_details.csv', 'x', newline='') as csvfile:
        fieldnames = ['name', 'emp_id', 'dept', 'salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'name': 'John', 'emp_id': 'E001', 'dept': 'IT', 'salary': 50000})
        writer.writerow({'name': 'Maya', 'emp_id': 'E002', 'dept': 'HR', 'salary': 40000})
        writer.writerow({'name': 'Arjun', 'emp_id': 'E003', 'dept': 'Finance', 'salary': 45000})
except FileExistsError:
    pass  # File already exists, continue

# Compute DA, HRA, and Gross salary
with open('employee_details.csv', 'r') as infile:
    reader = csv.DictReader(infile)

    fieldnames = ['emp_id', 'HRA', 'DA', 'Gross_Salary']

    with open('emp_sal.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            try:
                salary = float(row['salary'])
                da = 0.18 * salary  # 18% of salary
                hra = 0.02 * salary  # 2% of salary
                gross = salary + da + hra

                writer.writerow({
                    'emp_id': row['emp_id'],
                    'HRA': round(hra, 2),
                    'DA': round(da, 2),
                    'Gross_Salary': round(gross, 2)
                })
            except (ValueError, KeyError):
                print(f"⚠️ Skipping invalid row: {row}")

print("✅ emp_sal.csv file created successfully!")

# -------------------------------
# Display emp_sal.csv content
# -------------------------------
print("\nGenerated emp_sal.csv contents:")
with open('emp_sal.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)