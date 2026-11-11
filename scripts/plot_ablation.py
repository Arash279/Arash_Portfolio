"""Redraw the public 12-parameter summary; no optimization or model training."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
with (root / 'public/data/motor-ablation.csv').open(encoding='utf-8-sig') as f:
    rows = {r['script']: r for r in csv.DictReader(f)}
methods = [
    ('CurVer.py', 'Full workflow'),
    ('ablation_no_freq_weights.py', 'No frequency weights'),
    ('ablation_no_reim_scaling.py', 'No Re/Im scaling'),
    ('ablation_ls_only.py', 'Least squares only'),
    ('ablation_ga_ls.py', 'Genetic algorithm + LS'),
    ('ablation_de_only.py', 'Differential evolution only'),
]
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'svg.fonttype': 'none'})
fig, ax = plt.subplots(figsize=(10.8, 4.8), facecolor='white')
for i, (key, label) in enumerate(methods):
    r = rows[key]
    ax.errorbar(float(r['RMSE_raw__mean']), i, xerr=float(r['RMSE_raw__std']),
                fmt='o', color='#003366' if i == 0 else '#71879a',
                capsize=5, markersize=7, elinewidth=2)
ax.set_yticks(range(len(methods)), [m[1] for m in methods])
ax.invert_yaxis()
ax.set_xlim(0, 700)
ax.set_ylim(5.6, -.6)
ax.set_xlabel('Raw Re/Im RMSE (Ω) · mean ± 1 standard deviation', labelpad=12)
ax.set_title('12-parameter identification · 10 seeds per method', loc='left', pad=22, color='#003366', fontsize=14)
ax.grid(axis='x', color='#e3e8ed', linewidth=.8)
ax.set_axisbelow(True)
for side in ['top', 'right', 'left']:
    ax.spines[side].set_visible(False)
ax.spines['bottom'].set_color('#b9c4ce')
ax.tick_params(axis='y', length=0, pad=12)
fig.tight_layout(pad=2)
fig.savefig(root / 'public/images/motor-ablation.svg', metadata={'Date': None})
print('Saved public/images/motor-ablation.svg')
