import matplotlib.pyplot as plt

def create_bar_chart(poll):
    figure = plt.figure(figsize=(10, 10))
    figure.subplots_adjust(bottom=0.35)
    axes = figure.add_subplot(1 ,1, 1)
    axes.set_title("Polls to their vote counts")
    axes.set_ylabel("Vote count")
    axes.set_xlabel("Vote poll")

    axes.bar(
        range(len(polls)),
        [poll[1] for poll in polls],
        tick_label=[poll[0] for poll in polls]
    )
    plt.xticks(rotation=30, ha="right")
    # Object oriented approach
    # axes.set_xticks(range(len(polls)))
    # axes.set_xticklabels([poll[0] for poll in polls], rotation=30)

    return figure