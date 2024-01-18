import numpy as np
def worldseriesbetting(Serieslength, probability, totalprofit):
    # Want this function to return an array of betting values at each stage of the series,
    # Where the result of the series is totalprofit amount for either team.
    # Series length refers to how many wins required to win.
    Maxlength = Serieslength
    Positionarray = np.empty((Maxlength + 1, Maxlength + 1), int)
    Betsarray = np.empty((Maxlength, Maxlength), int)
    #Initiate Base cases
    Positionarray[:, Maxlength] = totalprofit
    Positionarray[Maxlength, :] = - totalprofit
    # 4-4 result is never reached
    Positionarray[Maxlength, Maxlength] = 0
    #Iterate to find betting and position values
    for i in range(Serieslength-1, -1, -1):
        for j in range(Serieslength-1, -1, -1):
            Positionarray[i][j] = (Positionarray[i+1][j] + Positionarray[i][j+1])/2
            Betsarray[i][j] = abs(Positionarray[i+1][j] - Positionarray[i][j])
    return Positionarray, Betsarray
print(worldseriesbetting(4, 0.8, 1000)[0])
print(worldseriesbetting(4, 0.3, 1000)[1])

