import requests
import pandas as pd

url = "https://www.sofascore.com/api/v1/unique-tournament/7/season/61644/top-teams/overall"

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    # Statistiques à extraire
    stats_paths = [
        "goalsScored",
        "shots",
        "shotsOnTarget",
        "successfulDribbles",
        "goalsConceded",
        "averageBallPossession",
        "bigChancesMissed",
        "bigChances"
    ]
    
    teams_stats = []

    for stat in stats_paths:
        for team_data in data["topTeams"].get(stat, []):
            team_name = team_data["team"]["name"]
            stat_value = team_data["statistics"].get(stat, None)
            
            team_entry = next((t for t in teams_stats if t["name"] == team_name), None)
            
            if team_entry:
                team_entry[stat] = stat_value
            else:
                team_entry = {"name": team_name, stat: stat_value}
                teams_stats.append(team_entry)

    df = pd.DataFrame(teams_stats)

    df.to_excel("top_teams_sstats.xlsx", index=False, engine="openpyxl")

    print("- top_teams_sstats.xlsx")

else:
    print("❌ Erreur:", response.status_code)
