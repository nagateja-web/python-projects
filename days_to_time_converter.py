calculation_to_seconds = 24
name_of_unit = "hours"


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days } days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number,days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you enter a '0', please enter a valid number.")
        else:
            print("you entered a negative number, no conversion for u!")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program")


user_input = ''
while user_input != 'exit':
    user_input = input("Hey user, enter a number of days and conversion unit: ")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days":days_and_unit[0],"unit":days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_execute()

    
    
    
    
    
""" OUTPUT
    Hey user, enter a number of days and conversion unit: 20:hours
['20', 'hours']
{'days': '20', 'unit': 'hours'}
20 days are 480 hours
Hey user, enter a number of days and conversion unit: 40:minutes
['40', 'minutes']
{'days': '40', 'unit': 'minutes'}
40 days are 57600 minutes
Hey user, enter a number of days and conversion unit: exit
['exit']
    """    
