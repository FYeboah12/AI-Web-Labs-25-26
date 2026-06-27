import random
def createBracket(teams,myTeam,constraints): 
    poss_bracket = []
    match_up = {t1:"" for t1 in teams}
    #match up will be each team with a partner (yes duplicates)
    if check_complete(teams,myTeam,poss_bracket,constraints): return poss_bracket
    var = select_var(match_up,teams,myTeam,constraints,poss_bracket)
    if isValid(var,myTeam,match_up,constraints):
        return match_up 
    return poss_bracket

def check_complete(teams,myTeam, poss_bracket, constraints):
    if myTeam not in poss_bracket: return False
    if len(poss_bracket) != len(teams): return False
    for i in range(len(poss_bracket)-2):
        bracket = poss_bracket[i:i+2]
        team1,team2 = bracket[0],bracket[1]
        winner = None
        if team1 not in constraints:
            winner = team2
        elif team2 not in constraints:
            winner = team1
        else:
            if team1 in constraints[team2]:
                winner = team2
            else:
                winner = team1
        if winner not in constraints[myTeam]:
            return False
    return True
                
def select_var(teams,myTeam,constraints,poss_bracket):
    ind = random.randint(0,len(teams)-1)
    while teams[ind] not in poss_bracket:
        ind = random.randint(0,len(teams)-1)
    return teams[ind]
 
def isValid(team,myTeam,constraints): #might not work for bigger teams but we'll see
    if team not in constraints:
        return True
    #if it is possible for my team to beat current team return true
    if team in constraints[myTeam]:
        return True
    parents_of_losers = constraints[myTeam]
    for p in parents_of_losers:
        if p in constraints and team in constraints[p]:
            return True
    return False



teams  = ['Duke','Gonzaga','Kansas','Kentucky','Michigan State','North Carolina','Villanova','UCLA']
constraints = {
    'Kansas': ['Gonzaga','North Carolina','Duke'],
    'Gonzaga': ['Duke','Kentucky'],
    'Duke': ['Michigan State','UCLA'],
    'Kentucky': ['Villanova','Kansas','UCLA'],
    'UCLA': ['North Carolina']
}
print(createBracket(teams, 'Kentucky', constraints))