names = ["Alice", "Bob", "Charlie", "David", "Eve"]
emails = [
    "Alice@gmail.com",
    "Bob@gmail.com",
    "Charlie@gmail.com",
    "David@gmail.com",
    "Eve@gmail.com",
]

# Slicing

selected_names = names[1:4]
print(selected_names)

reversed_names = names[::-1]
print(reversed_names)

doubled_names = names[::2]
print(doubled_names)

last_names = names[3:]
print(last_names)

validated_emails = [email[: email.index("@")] for email in emails]
print(validated_emails)

reversed_emails = emails[::-1]
print(reversed_emails)

reversed_emails_names = [
    validated_email[::-1] for validated_email in validated_emails
]  # Or: [email[: email.index("@")][::-1] for email in emails]
print(reversed_emails_names)
