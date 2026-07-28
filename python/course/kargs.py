def create_user(**kargs):
    for key, value in kargs.items():
        print(f"{key}: {value}")


create_user(username="master_aless", email="test@example.com", password="randon-string")
