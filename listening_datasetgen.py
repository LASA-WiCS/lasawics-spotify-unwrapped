import csv, random
from datetime import datetime, timedelta

artists = [
    ("Clairo", ["Juna", "Bags", "Amoeba", "Facing Away", "Sofia"], "Indie Pop"),
    ("ILLIT", ["Cherish (My Love)", "Tick-Tack", "Almond Chocolate", "NOT CUTE ANYMORE", "Magnetic"], "K-Pop"),
    ("Olivia Rodrigo", ["maggots for brains", "the cure", "lacy", "expectations", "so american"], "Pop"),
    ("Tate McRae", ["Revolving door", "Housewife", "Just Keep Watching", "Siren sounds", "greedy"], "Pop"),
    ("Frank Ocean", ["Pink + White", "Nights", "Ivy", "Thinkin Bout You"], "R&B"),
    ("Kendrick Lamar", ["luther", "tv off", "squabble up", "All The Stars", "HUMBLE."], "Hip-Hop"),
    ("Ariana Grande", ["twilight zone", "dandelion", "warm", "supernatural", "the boy is mine"], "Pop"),
    ("Malcolm Todd", ["Obsessica", "Breathe", "Earrings", "Roommates", "Sweet Boy"], "Indie"),
    ("keshi", ["MISS ME", "Soft Spot", "Say", "Inside Out", "LIMBO"], "Alt R&B")
]

weights = [28, 22, 16, 13, 9, 5, 4, 2, 1]
rows = []
base = datetime(2026, 1, 1, 8, 0, 0)

for i in range(10000):
    artist, tracks, genre = random.choices(artists, weights=weights, k=1)[0]
    track = random.choice(tracks)
    ms = random.randint(2500, 28000) if random.random() < 0.2 else random.randint(135000, 240000)
    ts = (base + timedelta(minutes=i * random.randint(3, 18))).isoformat()
    rows.append([ts, track, artist, genre, ms])

binge = datetime(2026, 6, 15, 14, 0, 0)
for j in range(14):
    rows.append([(binge + timedelta(minutes=j * 3)).isoformat(), "NOT CUTE ANYMORE", "ILLIT", "K-Pop", 154000])

random.shuffle(rows)
with open("listening_history.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["timestamp", "track_name", "artist", "genre", "ms_played"])
    w.writerows(rows)

print("filled list with 10,014 rows")
