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

    #runs exponential distribution once and gets expected runs. Should ideally run 1000+ times and get avg
    runs = np.random.exponential(average_runs, 100)
    return runs

# Example. will be populated with each players xwOBA which will be gathered from baseball savant or any site that has it
lineup_stats = [0.3, 0.35, 0.38, 0.42, 0.35, 0.3, 0.37, 0.34, 0.33]  # Fictional xwOBA for each player in the lineup
pitcher_stats = [3.95, 2.95]  # Fictional opposing pitcher's xERA. starter then bullpen. 
adjusted_pitcher_stats = [2.49, 1.09] #xERA divided by innings per start. assume starter throws 5.2 IP on avg each start. (15/27) * xERA to get adjusted

runs_scored = simulate_runs(lineup_stats, adjusted_pitcher_stats)

xruns = sum(runs_scored)/len(runs_scored)

print("Number of runs scored:", round(xruns,3))