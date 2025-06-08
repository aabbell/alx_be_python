from datetime import datetime, date, time, timedelta

def display_current_datetime():
    
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now().replace(microsecond=0) + timedelta(days=number_of_days)
    print(future_date)
calculate_future_date()
display_current_datetime()