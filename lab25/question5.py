import re


def check_string_for_email(text):
    # Pattern to match emails with alphanumeric characters, dots, and hyphens
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # re.search checks if the pattern exists anywhere in the string
    match = re.search(email_pattern, text)

    if match:
        return f"Found email: {match.group()}"
    else:
        return "No email address found."


# Test with your email string
my_text = "Please reach out to me at 265hsbd026@ibab.ac.in for updates."
print(check_string_for_email(my_text))