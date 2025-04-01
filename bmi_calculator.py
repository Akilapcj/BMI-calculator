# BMI Calculator

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to interpret BMI value
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main function to execute the calculator
def main():
    print("Welcome to the BMI Calculator!")
    
    # Taking user input for weight and height
    weight = float(input("Enter your weight in kilograms (36kg): "))
    height = float(input("Enter your height in meters (4.5m): "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Display BMI result
    print(f"Your BMI is: {bmi:.2f}")
    
    # Interpret the result
    result = interpret_bmi(bmi)
    print(f"Your BMI category is: {result}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
