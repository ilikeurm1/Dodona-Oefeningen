password = str(input())

if len(password) < 8:
    print(f'uw wachtwoord is te kort')
elif len(password) == 8:
    print(f'uw wachtwoord is net lang genoeg')
else:
    print(f'uw wachtwoord is veilig')
    