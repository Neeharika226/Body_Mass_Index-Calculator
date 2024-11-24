def bmi():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers!")
            return
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        print(f"\nYour Body Mass Index is: {bmi:.2f}")
        print(f"You are categorized as: {category}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")
if __name__ == "__main__":
    bmi()
