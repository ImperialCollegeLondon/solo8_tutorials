import numpy as np
from matplotlib.ticker import MultipleLocator, LinearLocator, AutoLocator, AutoMinorLocator, LogLocator
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=False)
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.titlepad'] = 20

black = "#272727"
blue = "#3498db"
green = "#2ecc71"
red = "#e74c3c"
orange = "#FF8000"
purple = "#9b59b6"
slate = "#34495e"
pink = "#FFC0CB"
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
color = [
    '#E8384F', # red
    '#FDAE33', # orange
    '#FFDD2B', # yellow
    '#62BB35', # green
    '#4178BC', # blue
    '#E37CFF', # magenta
    '#EA4E9D', # pink
    '#8D9F9B'] # gray

def subplots_adjust_inches(fig, left=1.0, bottom=1.0, right=0.5, top=0.5):
    """Adjust the space around the hull of the axes of a figure in inches

    Parameters
    ----------
    fig: matplotlib.figure.Figure
        The figure to adjust.
    left: float
        The margin between the left of the figure and the left side of the
        hull of the axes.
    bottom: float
        The margin between the bottom of the figure and the bottom side of
        the hull of the axes.
    right: float
        The margin between the right of the figure and the right side of the
        hull of the axes. Note that this differs from the
        `fig.subplots_adjust` method where the `right` parameter is the
        location of the right side of the hull of the axes wrt the left side
        of the figure.
    top: float
        The margin between the top of the figure and the top side of the
        hull of the axes. Note that this differs from the
        `fig.subplots_adjust` method where the `top` parameter is the
        location of the top side of the hull of the axes wrt the bottom side
        of the figure.
    """
    size_inches = fig.get_size_inches()
    if right is not None:
        right /= size_inches[0]
        right = 1-right
    if top is not None:
        top /= size_inches[1]
        top = 1-top
    if left is not None:
        left /= size_inches[0]
    if bottom is not None:
        bottom /= size_inches[1]
    fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top)


def use_grid_style(ax,
        x_major_locator=None, x_minor_locator=None,
        y_major_locator=None, y_minor_locator=None):
    for spine in ax.spines.keys():
        ax.spines[spine].set_color(black)
        ax.spines[spine].set_visible(True)
        ax.spines[spine].set_linewidth(4.0)
    ax.grid(False)
    ax.grid(which='major', linestyle='-', axis='both', color=black, alpha=0.125)
    ax.grid(which='minor', linestyle=':', axis='both', color=black, alpha=0.05)
    ax.xaxis.set_major_locator(x_major_locator if x_major_locator is not None else AutoLocator())
    ax.xaxis.set_minor_locator(x_minor_locator if x_minor_locator is not None else AutoMinorLocator())
    ax.yaxis.set_major_locator(y_major_locator if y_major_locator is not None else AutoLocator())
    ax.yaxis.set_minor_locator(y_minor_locator if y_minor_locator is not None else AutoMinorLocator())
    ax.tick_params(which='major', direction='in', axis='both', length=6, width=2, colors=black, pad=8.0, labelsize=10.0)
    ax.tick_params(which='minor', direction='in', axis='both', length=4, width=1, colors=black, pad=8.0, labelsize=10.0)