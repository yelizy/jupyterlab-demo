import seaborn as sns


# this one is simple but let us imagine something very lengthy
def fancy_plot(x_values, y_values, color):
    """
    Fancy function creating fancy plots.
    """
    sns.jointplot(x=x_values, y=y_values, kind="hex", color=color)