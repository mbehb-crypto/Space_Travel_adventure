import time
import winsound
import random


def play_alert(freq, duration):
    try:
        winsound.Beep(freq, duration)
    except:
        pass  # Fallback for non-Windows systems


def get_mission_data(player_name, planet, limit):
    data = {'planet': planet}
    print(f"\n🚀 {player_name.upper()} | MISSION: {planet.upper()} | Limit: {limit}s")

    start_time = time.time()
    prompts = [
        ('name', "Hero Name: "), ('adj', "Adjective: "),
        ('noun', "Noun: "), ('verb', "Verb (-ing): ")
    ]

    for key, prompt in prompts:
        # 20% chance of an asteroid hazard
        if random.random() < 0.20:
            print("\n☄️ ASTEROID! Type 'DODGE'!")
            if input("ACTION: ").upper() != "DODGE":
                print("💥 HIT! Time penalty applied.")
                start_time -= 4

        data[key] = input(prompt)
        elapsed = time.time() - start_time

        if elapsed > limit:
            play_alert(200, 500)
            return None

    data['duration'] = round(time.time() - start_time, 2)
    play_alert(1500, 300)
    return data