import random
from settings import PLANETS, LEVELS
from engine import get_mission_data, play_alert
from data_manager import save_score, show_leaderboard


def main():
    print("--- 🌌 UNIVERSAL SPACE RACE 3.0 🌌 ---")
    show_leaderboard()

    # Difficulty Selection
    print("\nSelect Difficulty: [1] Scout [2] Pilot [3] Commander")
    choice = input(">> ")
    diff_name, time_limit = LEVELS.get(choice, LEVELS["2"])
    print(f"Mode: {diff_name} ({time_limit}s)")

    p1 = input("\nPilot 1: ")
    p2 = input("Pilot 2: ")

    # Randomly assign a planet from settings.py
    mission_planet = random.choice(PLANETS)

    res1 = get_mission_data(p1, mission_planet, time_limit)
    res2 = get_mission_data(p2, mission_planet, time_limit)

    if res1: save_score(p1, res1['duration'])
    if res2: save_score(p2, res2['duration'])

    if res1 and res2:
        winner = p1 if res1['duration'] < res2['duration'] else p2
        print(f"\n🏁 WINNER: {winner.upper()} on {mission_planet}!")
        for f in [1000, 1200, 1500]: play_alert(f, 150)
    elif not res1 and not res2:
        print("\n💀 BOTH PILOTS LOST IN THE VOID.")

    show_leaderboard()


if __name__ == "__main__":
    main()