from datetime import datetime


def days_between_dates(date1_str, date2_str):
    # Define the date format
    date_format = "%Y-%m-%d"

    # Convert the string dates to datetime objects
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    # Calculate the difference between the two dates
    difference = date2 - date1

    # Return the number of days
    return abs(difference.days)


# Example usage
date1 = "2025-02-04"
date2 = "2025-03-21"

print(f"Days between {date1} and {date2}: {days_between_dates(date1, date2)}")
