# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Query for all games
    gamefinder = leaguegamefinder.LeagueGameFinder()
    games = gamefinder.get_data_frames()[0]

    # Optionally, you can limit the number of games using DataFrame operatio ns.
    # For example, to get the first 100 games:
    games_subset = games.head(10)

    # Display the games
    print(games_subset)

    games.to_csv('Datasets/NBA_API_Games.csv')
