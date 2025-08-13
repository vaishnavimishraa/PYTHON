#Q7.

total_seconds = int(input("Enter the total number of seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
remaining_seconds = total_seconds % 60

print("Converted time: {} hours, {} minutes, and {} seconds".format(hours, minutes, remaining_seconds))
