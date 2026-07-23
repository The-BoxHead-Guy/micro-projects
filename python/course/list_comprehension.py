# Traditional Approach

emails = ["anna@example.com", "bob@example.com", "charlie@example.com", "", None]

valid_emails = []
for email in emails:
    if email:
        valid_emails.append(email)

print(valid_emails)

# List Comprehension Approach

valid_emails_through_comprehension = [email for email in emails if email]
print(valid_emails_through_comprehension)
