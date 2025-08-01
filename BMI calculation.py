def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_status(bmi):
    if bmi < 18.5: return "Underweight"
    elif bmi < 25: return "Normal weight"
    elif bmi < 30: return "Overweight"
    else: return "Obesity"

def main():
    name = input("Enter your name: ")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    bmi = calculate_bmi(weight, height)
    status = get_status(bmi)
    print(f"\n{name}, your BMI is {bmi} ({status})")

if __name__ == "__main__":
    main()
