# Week 1: Learning Python Functions

# Function 1: Display a greeting
def greet(name):
    print("Hello,", name)
    print("Welcome to your AI engineering journey!")

 # Function 2: Calculate annual study hours


def calculate_annual__hours(hours_per_week):
    annual_hours = hours_per_week * 52
    return annual_hours

# Function 3: calculate monthly study hours


def calculate_monthly_hours(annual_hours):
    monthly_hours = annual_hours / 12
    return monthly_hours


# Call the functions
greet("Antony")

weekly_hours = 15
yearly_total = calculate_annual__hours(weekly_hours)
monthly_total = calculate_monthly_hours(yearly_total)

print("my weekly study hours:", weekly_hours)
print("my annual study hours:", yearly_total)
print("my average monthly study hours:", monthly_total)
