import re

# Example text
text = "Contact us at support@example.com or sales@example.com."

# Define a regex pattern for emails
pattern = r'[\w\.-]+@[\w\.-]+'

# Find all matches
matches = re.findall(pattern, text)

print("Found email addresses:")
for email in matches:
    print(email)

# Using groups
date_text = "Today's date is 2025-07-10."
date_pattern = r'(\d{4})-(\d{2})-(\d{2})'

match = re.search(date_pattern, date_text)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")