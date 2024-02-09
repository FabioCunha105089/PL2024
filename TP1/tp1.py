import sys

ages = {}
genres = set()
fit_count = 0
total = 0

next(sys.stdin)

for i, line in enumerate(sys.stdin):
    _, _, _, _, _, age_str, _, _, genre, _, _, _, fit = line.split(',')
    age = int(age_str)
    if 't' in fit:
        fit_count += 1

    genres.add(genre)

    lower_bound = (age // 5) * 5
    interval = f"[{lower_bound}, {lower_bound + 4}]"

    if interval in ages:
        ages[interval] += 1
    else:
        ages[interval] = 1

    total += 1

genres_list = sorted(genres)
print(f"Modalidades: {', '.join(genres_list)}")

fit_athletes = fit_count / total * 100
unfit_athletes = 100 - fit_athletes
print(f"""Aptos: {fit_athletes}%
Inaptos: {unfit_athletes}%""")

print("Distribuição: ")
sorted_intervals = sorted(ages.keys())
for interval in sorted_intervals:
    percentage = ages[interval] / total * 100
    print(f"{interval}: {percentage:.2f}%")
