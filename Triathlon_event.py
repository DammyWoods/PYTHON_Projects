#Variables swimming_t, cycling_t and running_t were introduced 
#To represent the swimming, cycling and running times in minutes respectively

swimming_t = int(input("Enter swimming time (in minutes): "))
cycling_t = int(input("Enter cycling time (in minutes): "))
running_t= int(input("Enter running time (in minutes): "))

#award_time, award_time2 and award_time3 represents the qualifying time limit a participant should attain to qualify for any of the awards
#award_time represents the 100 minutes qualifying time-frame first award
#award_time2 variable signiifies that an extra 5minutes time-frame qualifies for the second award
#while award_time3 variable signifies that an additional 5minutes time-frame after award_time2 qualifies for the third award

award_time = 100
award_time2 = award_time + 5
award_time3 = award_time2 + 5

#total_time represents the total time taken for the participant to complete the three activities
total_time = swimming_t + cycling_t + running_t

#Assuming no participant can complete the three events in less than 60 minutes
#Also assuming no participant can complete each event in less than 20 minutes

if (swimming_t != 0 and cycling_t != 0 and running_t != 0):
    if (swimming_t < 20 or cycling_t < 20 or running_t < 20):
        print("\n One or more of your competition time is less than 20 minutes!\n This is unrealistic. Please input the correct time in minutes")
    elif (total_time >= 60) and (total_time <= award_time):
        print("\n Your total triathlon time is: ", total_time)
        print("Congratulations!!! You have qualified for the Provincial Colours award")
    elif (total_time > award_time) and (total_time <= award_time2):
        print("\n Your total triathlon time is: ", total_time)
        print("Congratulations!!! You have qualified for the Provincial Half Colours award")
    elif (total_time > award_time2) and (total_time <= award_time3):
        print("\n Your total triathlon time is: ", total_time)
        print("Congratulations!!! You have qualified for the Provincial Scroll award")
    else :
        print("\n Your total triathlon time is: ", total_time)
        print("Unfortunately, You have exceeded the triathlon time to qualify for an award.\nCurrently, You have not qualified for any of the awards")  
else :
    print("\n This is a triathlon event. \n Unfortunately! You have not completed one or more of the three competitions. \n Hence, you do not qualify for any of the awards")
