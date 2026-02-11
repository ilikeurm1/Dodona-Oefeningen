# Set vars
v = 1 # meter / minute
T = -1 # expired minutes

# Inputs 
y = int(input("Afstand y tussen bloempot en afgrond (m): "))
A = int(input("Afstand A tussen Goomba A en afgrond (m): ")) # initial position of Goomba A
VA = v if input("Start Goomba A naar Links of Rechts (L/R) ?") == "L" else -v
B = int(input("Afstand B tussen Goomba B en afgrond (m): ")) # idem for B
VB = v if input("Start Goomba B naar Links of Rechts (L/R) ?") == "L" else -v

# Let the goomba's run as long as they are not in the AG
while (A >= 0 or B >= 0):
    A = A + VA
    B = B + VB
    # check for collision with BP
    if A == y: 
        VA = -VA
    if B == y:
        VB = -VB
    if A == B:
        VB = -VB
        VA = -VA
    T = T + 1
    if T == 10 * y: # Something is wrong here
        break

print(f"Het duurt {T} minuten tot beide Goomba's weg zijn")
