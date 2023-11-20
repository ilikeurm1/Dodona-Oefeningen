password = str(input())

if len(password) < 8:
    print('uw wachtwoord is te kort')
elif len(password) == 8:
    print('uw wachtwoord is net lang genoeg')
else:
    print('uw wachtwoord is veilig')
    