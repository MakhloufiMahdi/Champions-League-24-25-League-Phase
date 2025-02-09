import requests
import pandas as pd

def get_team_statistics(team_id, team_name):
    url = f"https://www.sofascore.com/api/v1/team/{team_id}/unique-tournament/7/season/61644/statistics/overall"
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        stats = data.get('statistics', {})
        
        keys = [
            "accurateLongBalls", "accurateLongBallsPercentage", "accurateCrosses", "accurateCrossesPercentage",
            "accurateOwnHalfPasses", "accurateOwnHalfPassesAgainst", "accurateOwnHalfPassesPercentage",
            "accuratePasses", "accuratePassesAgainst", "accuratePassesPercentage", "averageBallPossession",
            "aerialDuelsWon", "aerialDuelsWonPercentage", "ballRecovery"
        ]
        
        extracted_stats = {key: stats.get(key, 'N/A') for key in keys}
        extracted_stats['team'] = team_name
        return extracted_stats
    else:
        return None

teams = [
    (44, "Liverpool"),
    (2817, "Barcelona")
]

all_stats = []
for team_id, team_name in teams:
    stats = get_team_statistics(team_id, team_name)
    if stats:
        all_stats.append(stats)

df = pd.DataFrame(all_stats)

df.to_excel("teamm.xlsx", index=False)

