import csv
from collections import defaultdict, Counter
import math
import os

def is_float(val):
    try:
        float(val)
        return True
    except:
        return False

def compute_stats(input_file, output_file):
    with open(input_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    stats = defaultdict(list)
    for row in data:
        for key, val in row.items():
            if val != '':
                stats[key].append(val)

    result = []
    for col, values in stats.items():
        row_data = {'Column': col, 'Count': len(values)}
        if all(is_float(v) for v in values):
            nums = list(map(float, values))
            mean = sum(nums) / len(nums)
            std = math.sqrt(sum((x - mean) ** 2 for x in nums) / len(nums))
            row_data.update({
                'Type': 'Numeric',
                'Mean': round(mean, 2),
                'Min': min(nums),
                'Max': max(nums),
                'StdDev': round(std, 2)
            })
        else:
            counter = Counter(values)
            row_data['Type'] = 'Categorical'
            row_data['Unique'] = len(counter)
            for i, (val, count) in enumerate(counter.most_common(3)):
                row_data[f'Top_{i+1}_Value'] = val
                row_data[f'Top_{i+1}_Count'] = count
        result.append(row_data)

    # Write to CSV
    os.makedirs("output", exist_ok=True)
    keys = sorted({key for d in result for key in d})
    with open(output_file, 'w', newline='', encoding='utf-8') as out:
        writer = csv.DictWriter(out, fieldnames=keys)
        writer.writeheader()
        writer.writerows(result)

# Run
compute_stats("data/2024_tw_posts_president_scored_anon.csv", "output/tw_posts_summary.csv")
