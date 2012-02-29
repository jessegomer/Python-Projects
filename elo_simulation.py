#made by jesse gomer
import random
import math
'''
This program simulates elo rating for a tournament of games that are
5v5. I used it to try to determine the effectiveness of using the elo
system for non 1v1 games
'''

number_players=1000
number_games=10000
number_intervals=20

class player_class:
    elo=1000
    games_played=0
    distance=0
    skill=0
    def int_elo(self):
        self.elo=int(self.elo)
    def set_skill(self):
        self.skill=random.randint(3,7)
    
players = []
for each in range(number_players): players.append(player_class())


def elo_average(team):
    total=0
    i=0
    for each in range(5):
        player_num=team[i]
        total+=players[player_num].elo
        i+=1
    avg=total/5
    return avg

def find_winner(team1, team2):
    t1t=0
    t2t=0
    dif=0
    i=0
    for each in range(5):
        t1t+=players[team1[i]].skill
        i+=1
        
    i=0
    for each in range(5):
        t2t+=players[team2[i]].skill
        i+=1
    dif= t1t - t2t
    x=5+(dif+dif)
    if(x>=random.randint(1,10)):
        return 1
    else:
        return 2
    

def do_change(elo_change,team,win):
    i=0
    elo_change*=win
    for each in range(5):
        player_num=team[i] 
        players[player_num].elo+=elo_change
        players[player_num].games_played+=1
        i+=1
        
i=0
while(i<number_players):
    players[i].skill=random.randint(3,7)
    i+=1


for each in range(number_games):
    both_teams=random.sample(range(number_players), 10)
    team_1=both_teams[:5]
    team_2=both_teams[5:]
    if( find_winner(team_1, team_2)==1):
        elo_change=(32*(1-1/(10**(-(elo_average(team_1)-elo_average(team_2)))+1)))
        do_change(elo_change,team_1,1)
        do_change(elo_change,team_2,-1)
    else:
        elo_change=(32*(1-1/(10**(-(elo_average(team_2)-elo_average(team_1)))+1)))
        do_change(elo_change,team_2,1)
        do_change(elo_change,team_1,-1)

i=0
while(i<number_players):
    players[i].int_elo()
    players[i].distance=int(math.fabs(1000-players[i].elo))
    i+=1

i=0
players.sort(key=lambda x: x.elo, reverse=True)

while (i < number_players):
        print(players[i].elo,",",players[i].skill)
        i+=1
"""i=0
while(i<number_players):
    print(players[i].distance,",",players[i].games_played)
    i+=1"""
'''
i=0
while(i<number_players):
    players[i].int_elo()
    i+=1'''
    
# random.sample(range(number_players), 10)
