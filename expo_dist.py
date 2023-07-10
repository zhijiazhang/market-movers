import numpy as np

"""
***DISCLAIMER***
hella basic data use for poisson. can be way more detailed and complex based on the data

"""

def simulate_runs(lineup_stats, adjusted_pitcher_stats):
    """Simulates the number of runs scored by a team using a Poisson distribution"""
    lineup_average_runs = np.sum(lineup_stats)
    pitcher_average_runs = np.sum(adjusted_pitcher_stats)

    average_runs = (lineup_average_runs + pitcher_average_runs) / 2

    #runs exponential distribution 100 times and gets expected runs.
    runs = np.random.exponential(average_runs, 100)
    return runs

# Example. will be populated with each players xwOBA which will be gathered from baseball savant or any site that has it
lineup_stats = [0.326, 0.436, 0.341, 0.375, 0.36, 0.342, 0.356, 0.344, 0.319]  # Fictional xwOBA for each player in the lineup
pitcher_stats = [4.89, 5.03]  # Fictional opposing pitcher's xERA. starter then bullpen. 
adjusted_pitcher_stats = [3.09, 1.86] #xERA divided by innings per start. assume starter throws 5.2 IP on avg each start. (15/27) * xERA to get adjusted

runs_scored = simulate_runs(lineup_stats, adjusted_pitcher_stats)

#average of all simulations
xruns = sum(runs_scored)/len(runs_scored)

print("Number of runs scored:", round(xruns,3))



###Different approach for stats. Use a teams xwOBA of the past 10 games. average it with their xwOBA for the season
#use baseball savant to get team xwOBA