import pandas as pd
import matplotlib
import matplotlib.animation
from matplotlib import pyplot as plt

# Animations: https://matplotlib.org/stable/api/animation_api.html
# Transparent Background: https://stackoverflow.com/questions/15857647/how-to-export-plots-from-matplotlib-with-transparent-background
# basic animations: https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
# plotting NAN values: https://matplotlib.org/devdocs/gallery/lines_bars_and_markers/masked_demo.html

raw_data = pd.read_excel("DataAnalysis/Heatmap/ForceGraphs/graphs_sample.xlsx").fillna(value=0)
fig = plt.figure(facecolor=(0,0,0,0), dpi=300, figsize=(4.267, 3.6))

ax = fig.add_subplot(111)
ax.set_facecolor((1,1,1,0))
thickness = 2
ax.xaxis.set_tick_params(width=thickness)
ax.yaxis.set_tick_params(width=thickness)
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(thickness)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontweight('bold') for label in labels]

plt.rcParams['axes.facecolor'] = (1,1,1,0)
plt.rcParams["font.size"] = "12"
plt.ylim([-0.06, 0.40])
plt.xlim([0, 100])

TIME = list(raw_data["TIME"])
FORCE_1 = list(raw_data["FORCE_1"])
FORCE_2 = list(raw_data["FORCE_2"])
FORCE_3 = list(raw_data["FORCE_3"])

time, force_1, force_2, force_3 = [], [], [], []
def animate(idx):
    time.append(TIME[idx])
    force_1.append(FORCE_1[idx])
    force_2.append(FORCE_2[idx])
    force_3.append(FORCE_3[idx])
    
    plt.plot(time, force_1, "dodgerblue", label="force_1", antialiased=True, linewidth=2)
    plt.plot(time, force_2, "orange", label="force_2", antialiased=True, linewidth=2)
    plt.plot(time, force_3, "forestgreen", label="force_3", antialiased=True, linewidth=2)

    plt.legend(["Force 1", "Force 2", "Force 3"])

anim = matplotlib.animation.FuncAnimation(fig, animate, frames=len(TIME), interval=10, repeat=False)

save_file = "DataAnalysis/Heatmap/ForceGraphs/output_graph.gif"
# anim.save(save_file, writer='ffmpeg')
plt.show()
print("FINISH")