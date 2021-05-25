import datetime

user_input = input("Enter your goal with a deadline seperated by colon: ")
input_list = user_input.split(':')
goal = input_list[0]
deadline = input_list[1]
deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
# calculate how many days from till deadline
time_till = deadline_date-today_date

print(f"time remaining for your goal: {goal} is {int(time_till.days)} days")

