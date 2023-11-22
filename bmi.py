def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height * height)

    print("BMI = " + str(bmi))

    if bmi < 18.5 :
        print("Weight Class = Under Weight")
        return -1
    elif 18.5 <= bmi <= 25.0 :
        print("Weight Class = Normal Weight")
        return 0
    else :
        print("Weight Class = Over Weight")
        return 1


calculate_bmi(weight=45, height=1.73)