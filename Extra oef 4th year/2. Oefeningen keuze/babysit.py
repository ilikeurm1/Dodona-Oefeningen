# https://dodona.be/nl/courses/107/series/1244/activities/1797346540

# Constants
Min_in_Hour = 60
failed = False

# Inputs
Start_Hour = int(input())
Start_Min = int(input())
End_Hour = int(input())
End_Min = int(input())

# Variables
# Money
Total_Money_earned = None
Money_Earned_After = None
Money_Earned_Before = None

# Time Worked
Total_Worked = None
Worked_Before = None
Worked_After = None

# Turn minutes to decimals
Start_Time = Start_Hour +  Start_Min / Min_in_Hour
End_Time = End_Hour + End_Min / Min_in_Hour

# Error
if End_Hour < Start_Hour or Start_Hour < 18 :
    print('ongeldige invoer')
    failed = True

Total_Worked = End_Time - Start_Time

if End_Time <= 21.5:
    Total_Money_earned = 2 * Total_Worked

elif End_Time > 21.5 and Start_Time < 21.5:
    # Time worked
    Worked_After = End_Time - 21.5
    Worked_Before = Total_Worked - Worked_After

    # Money Earned
    Money_Earned_After = Worked_After * 4
    Money_Earned_Before = Worked_Before * 2

    Total_Money_earned = Money_Earned_Before + Money_Earned_After

elif Start_Time > 21.5:
    # Same as if ended before 21:30 only 4 dollars per hour
    Total_Money_earned = 4 * Total_Worked


if not failed:
    print(Total_Money_earned)
