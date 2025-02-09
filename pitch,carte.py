import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns


df = pd.read_excel("teamm.xlsx")

metrics = ["COUNTER ATTACKS", "averageBallPossession"]
df_selected = df.set_index("team")[metrics]

fig, ax = plt.subplots(figsize=(10, 6)) 
pitch = Pitch(pitch_type='statsbomb', pitch_color='green')  
pitch.draw(ax=ax)

barcelona_stats = {
    'counterAttacks': df_selected.loc['Barcelona', 'COUNTER ATTACKS'],
    'averageBallPossession': df_selected.loc['Barcelona', 'averageBallPossession']
}

liverpool_stats = {
    'counterAttacks': df_selected.loc['Liverpool', 'COUNTER ATTACKS'],
    'averageBallPossession': df_selected.loc['Liverpool', 'averageBallPossession']
}

ax.annotate("", xy=(45, 40), xytext=(30, 40),
            arrowprops=dict(arrowstyle="->", lw=2, color='black'))
ax.annotate(f"{barcelona_stats['counterAttacks']}", xy=(30, 40), xytext=(25, 38),
            fontsize=12, fontweight='bold', color='purple')

ax.annotate("", xy=(45, 35), xytext=(30, 35),
            arrowprops=dict(arrowstyle="->", lw=2, color='blue'))
ax.annotate(f"{barcelona_stats['averageBallPossession']}%", xy=(30, 35), xytext=(25, 33),
            fontsize=12, fontweight='bold', color='purple')

ax.annotate("", xy=(55, 40), xytext=(70, 40),
            arrowprops=dict(arrowstyle="->", lw=2, color='black'))
ax.annotate(f"{liverpool_stats['counterAttacks']}", xy=(70, 40), xytext=(75, 38),
            fontsize=12, fontweight='bold', color='red')

ax.annotate("", xy=(55, 35), xytext=(70, 35),
            arrowprops=dict(arrowstyle="->", lw=2, color='blue'))
ax.annotate(f"{liverpool_stats['averageBallPossession']}%", xy=(70, 35), xytext=(75, 33),
            fontsize=12, fontweight='bold', color='red')

# Titre
plt.title("Comparaison des statistiques de Counter Attacks et Ball Possession", fontsize=14, fontweight='bold')

ax.text(30, 90, "Barcelona", ha='center', va='center', fontsize=14, fontweight='bold', color='purple')
ax.text(70, 90, "Liverpool", ha='center', va='center', fontsize=14, fontweight='bold', color='red')

ax.text(70, 86, "Counter Attacks", ha='center', va='center', fontsize=12, color='black')
ax.text(40, 86, "Ball Possession", ha='center', va='center', fontsize=12, color='blue')

plt.show()

metrics = ["COUNTER ATTACKS", "aerialDuelsWon", "accuratePasses", "accurateCrosses", 
           "accurateOwnHalfPasses", "averageBallPossession"]
df_selected = df.set_index("team")[metrics]

# 🔹 1. Carte thermique
plt.figure(figsize=(8, 5))

cmap = sns.diverging_palette(250, 20, as_cmap=True)  

sns.heatmap(df_selected, annot=True, fmt=".1f", cmap=cmap, linewidths=0.5, linecolor="white", cbar_kws={'shrink': 0.8})
plt.title("Carte thermique des performances (Barcelone vs Liverpool)", fontsize=14, fontweight='bold')
plt.xticks(rotation=15)
plt.gca().set_facecolor('lightgrey') 
plt.show()  