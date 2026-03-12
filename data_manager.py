import json
import os

FILE = "scores.json"

def save_score(name, time):
    scores = load_scores()
    if name not in scores or time < scores[name]:
        scores[name] = time
        with open(FILE, "w") as f:
            json.dump(scores, f, indent=4)

def load_scores():
    if not os.path.exists(FILE): return {}
    with open(FILE, "r") as f: return json.load(f)

def show_leaderboard():
    scores = load_scores()
    if not scores: return
    print("\n--- 🏆 GALACTIC TOP PILOTS ---")
    for name, t in sorted(scores.items(), key=lambda x: x[1]):
        print(f"{name.upper()}: {t}s")