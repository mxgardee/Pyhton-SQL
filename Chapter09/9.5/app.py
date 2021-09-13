import matplotlib.pyplot as plt
from data import polls

poll_titles = [poll[0] for poll in polls]
poll_men = [poll[1] for poll in polls]
poll_women = [poll[2] for poll in polls]

poll_x_cordinates = range(len(polls))

figure = plt.figure(figsize=(6, 6), linewidth=5)
figure.subplots_adjust(bottom=0.35)
axes = figure.add_subplot()


men_plot = axes.bar(
    poll_x_cordinates,
    poll_men,
)
women_plot = axes.bar(
    poll_x_cordinates,
    poll_women,
    bottom=poll_men,
)

axes.legend((men_plot, women_plot), ("Men", "Women"))

plt.xticks(poll_x_cordinates, poll_titles, rotation=30, ha="right")

save_results_to = 'C:/Computer Files/Code College/SQL/My Queries/Project03/9. Matplotlib/9.5 Export Image/'
figure.savefig(save_results_to + "graph5.png", bbox_inches="tight", facecolor="#5c44fd", edgecolor="#ff0000")