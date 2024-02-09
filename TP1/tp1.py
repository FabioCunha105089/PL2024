import sys

first = True
ages = {}
genres = set()
fit = 0
total = 0
for i, line in enumerate(sys.stdin):
    if first:
        continue

    _, _, _, _, _, age, _, _, genre, _, _, _, fit = line.split(',')
    if fit:
        fit += 1

    genres.add(genre)

    r = age % 10
    if r < 5:
        ages.update({f"[{age - r}, {age + 4 - r}]": age})
    else:
        ages.update({f"[{age - r + 5}, {age + 9 - r}]": age})

    total += 1

genres_list = sorted(genres)
print(', '.join(genres_list))

fit_athletes = fit / total * 100
unfit_athletes = 100 - fit_athletes
print(f"""Fit -> {fit_athletes}%
Unfit -> {unfit_athletes}%""")

for interval, athlete_ages in ages.items():
    print(f"{interval} -> {len(athlete_ages/total*100)}%")
