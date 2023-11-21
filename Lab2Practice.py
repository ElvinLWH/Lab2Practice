import statistics
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def calc_average(input_list):
    average = sum(input_list) / len(input_list)

    print("Average = " + str(average))

    return average

def find_min_max(input_list):
    value_min = min(input_list)
    value_max = max(input_list)

    min_max_list = [value_min,value_max]

    print("Min, Max = " + str(min_max_list))

    return min_max_list

def sort_temperature(input_temp_list):
    temp_sort = sorted(input_temp_list)

    print("Temp in ascending order = " + str(temp_sort))

    return temp_sort

def calc_median_temperature(input_temp_list):
    median_temp = statistics.median(input_temp_list)

    print("Median Temperature = " + str(median_temp))

    return median_temp

def calc_average_temperature(input_temp_list):
    average_temp = sum(input_temp_list) / len(input_temp_list)

    print("Average Temperature = " + str(average_temp))

    return average_temp

def calc_min_max_temperature(input_temp_list):
    min_temp = min(input_temp_list)
    max_temp = max(input_temp_list)

    min_max_temp_list = [min_temp, max_temp]

    print("Min Temp, Max Temp = " + str(min_max_temp_list))

    return(min_max_temp_list)

def get_user_input():
    user_text = input()
    split_text = user_text.split(",")
    user_list_string = split_text
    user_list_num = [float(num) for num in user_list_string]

    print(user_list_num)

    return(user_list_num)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    user_input_1 = get_user_input()
    calc_average(user_input_1)
    find_min_max(user_input_1)

    display_main_menu()
    user_input_2 = get_user_input()

    sort_temperature(user_input_2)
    calc_median_temperature(user_input_2)
    calc_average_temperature(user_input_2)
    calc_min_max_temperature(user_input_2)


if __name__ == "__main__":
    main()

