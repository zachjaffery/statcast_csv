import requests
import pandas as pd
import sys

def team_to_id(team_name):
    """
    3 letter code -> API ID \n
    Ex: team_to_id(CHC) -> 112
    """
    try:
        query = "team_ids.csv"
        df = pd.read_csv(query)
        return df.loc[df["Abbreviation"] == team_name].iloc[0].iloc[0]
    except:
        print(f"Error: Team '{team_name}' not found, or not of proper format.")


def get_stats(team_1, team_2=None, player_type="batter"):
    t1_id = team_to_id(team_1)
    if team_2:
        t2_id = team_to_id(team_2)
        url = f"https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfAB=&hfGT=R%7C&hfPR=&hfZ=&hfStadium=&hfBBL=&hfNewZones=&hfPull=&hfC=&hfSea=2026%7C&hfSit=&player_type={player_type}&hfOuts=&home_road=&pitcher_throws=&batter_stands=&hfSA=&hfEventOuts=&hfEventRuns=&hfABSFlag=&game_date_gt=&game_date_lt=&hfMo=&hfTeam={t1_id}%7C{t2_id}%7C&hfOpponent=&hfRO=&position=&hfInfield=&hfOutfield=&hfInn=&hfBBT=&hfFlag=&metric_1=&group_by=name&min_pitches=0&min_results=0&min_pas=0&sort_col=pitches&player_event_sort=api_p_release_speed&sort_order=desc&chk_stats_pa=on&chk_stats_abs=on&chk_stats_hrs=on&chk_stats_so=on&chk_stats_bb=on&chk_stats_bb_percent=on&chk_stats_whiffs=on&minors=false&wbc=false"
    else:
        url = f"https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfAB=&hfGT=R%7C&hfPR=&hfZ=&hfStadium=&hfBBL=&hfNewZones=&hfPull=&hfC=&hfSea=2026%7C&hfSit=&player_type={player_type}&hfOuts=&home_road=&pitcher_throws=&batter_stands=&hfSA=&hfEventOuts=&hfEventRuns=&hfABSFlag=&game_date_gt=&game_date_lt=&hfMo=&hfTeam={t1_id}%7C&hfOpponent=&hfRO=&position=&hfInfield=&hfOutfield=&hfInn=&hfBBT=&hfFlag=&metric_1=&group_by=name&min_pitches=0&min_results=0&min_pas=0&sort_col=pitches&player_event_sort=api_p_release_speed&sort_order=desc&chk_stats_pa=on&chk_stats_abs=on&chk_stats_hrs=on&chk_stats_so=on&chk_stats_bb=on&chk_stats_bb_percent=on&chk_stats_whiffs=on&minors=false&wbc=false"

    response = requests.get(url)
    with open("stats.csv", "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    t1 = sys.argv[1]
    try:
        t2 = sys.argv[2]
    except IndexError:
        t2 = None
    try:
        p_type = sys.argv[3]
    except IndexError:
        p_type = "batter"
    get_stats(t1, t2, p_type)
