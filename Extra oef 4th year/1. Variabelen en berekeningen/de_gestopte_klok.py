# https://dodona.be/nl/courses/107/series/1303/activities/1477235114

# Imports
import math

# Constants
Min_in_hour = 60

# Inputs
# Leaving home
Leaving_Home_Hour = int(input())
Leaving_Home_Min = int(input())

# Arrival Friend
Arrival_Friend_Hour = int(input())
Arrival_Friend_Min = int(input())

# Leaving Friend
Leaving_Friend_Hour = int(input())
Leaving_Friend_Min = int(input())

# Arrival back home
Arrival_Home_Hour = int(input())
Arrival_Home_Min = int(input())

# Making all Times decimals for ez math
Decimal_Leaving_Home = Leaving_Home_Hour + Leaving_Home_Min / Min_in_hour
Decimal_Arrival_Friend = Arrival_Friend_Hour + Arrival_Friend_Min / Min_in_hour
Decimal_Leaving_Friend = Leaving_Friend_Hour + Leaving_Friend_Min /  Min_in_hour
Decimal_Arrival_Home = Arrival_Home_Hour + Arrival_Home_Min / Min_in_hour

# Total Trip Time
Total_Trip = Decimal_Arrival_Home - Decimal_Leaving_Home

# Time spent biking / Going to friend
Time_Biking = (Total_Trip - (Decimal_Leaving_Friend - Decimal_Arrival_Friend)) / 2

# Calculating "Real" time

Real_Time_Full = Decimal_Leaving_Friend + Time_Biking
Real_Time_Hour = math.floor(Real_Time_Full)
Real_Time_Min = round((Real_Time_Full - Real_Time_Hour) * 60, 0)

if Leaving_Home_Hour > Arrival_Home_Hour:
    Real_Time_Hour += 12
if Real_Time_Hour > 24:
    Real_Time_Hour = Real_Time_Hour - 24

print(Real_Time_Hour)
print(int(Real_Time_Min))

# # https://dodona.be/nl/courses/107/series/1303/activities/1477235114

# # Inputs
# Leaving_Home_Hour = int(input())
# Leaving_Home_Min = int(input())

# Arrival_Friend_Hour = int(input())
# Arrival_Friend_Min = int(input())

# Leaving_Friend_Hour = int(input())
# Leaving_Friend_Min = int(input())

# Arrival_Home_Hour = int(input())
# Arrival_Home_Min = int(input())

# # Total Trip Time
# Total_Trip_Hour = Arrival_Home_Hour - Leaving_Home_Hour
# Total_Trip_Min = Arrival_Home_Min - Leaving_Home_Min

# # Time spent biking / Going to friend
# Time_Biking_Hour = (Total_Trip_Hour - (Leaving_Friend_Hour - Arrival_Friend_Hour)) / 2
# Time_biking_min = (Total_Trip_Min - (Leaving_Friend_Min - Arrival_Friend_Min)) / 2

# # Calculating "Real" time

# Real_Time_Hour = Leaving_Friend_Hour + Time_Biking_Hour
# Real_Time_Min = Leaving_Friend_Min + Time_biking_min

# print(int(Real_Time_Hour))
# print(int(Real_Time_Min))

