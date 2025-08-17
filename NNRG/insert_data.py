from . import models
team_list = ['KKR','DC',"RR"]
cap_list = ['Nithish Rana', 'David warner','Sanju Samson']
trophes = [2,0,1]
for i,j,k in team_list,cap_list , trophes:
    obj = models.teams()
    obj.name = i
    obj.captain = j
    obj.trophy = k
    obj.save()

