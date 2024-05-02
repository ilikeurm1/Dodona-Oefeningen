P = input()
if len(P) == 8:
    print('uw wachtwoord is net lang genoeg')
elif len(P) > 8:
    print('uw wachtwoord is veilig')
else:
    print('uw wachtwoord is te kort')
