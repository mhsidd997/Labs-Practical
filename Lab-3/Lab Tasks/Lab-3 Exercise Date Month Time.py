dt_string = input("Enter a datetime string (yyyy-mm-dd hh:mm:ss): ")
get_date_time = lambda dt_string: (dt_string[:4], dt_string[5:7], dt_string[8:10], dt_string[11:19])
year, month, date, time = get_date_time(dt_string)

print("Year:", year)
print("Month:", month)
print("Date:", date)
print("Time:", time)