def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height * height)

    print("BMI = " + str(bmi))

    if bmi < 18.5 :
        print("Weight Class = Under Weight")
    elif 18.5 <= bmi <= 25.0 :
        print("Weight Class = Normal Weight")
    else :
        print("Weight Class = Over Weight")


calculate_bmi(weight=45, height=1.73)