import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from .text import arab
from .ticks import custom_formatter, custom_log_formatter


def arabic_2d_axis_formatter(ax, log=False, labelsize=16, *, invert_x=True, y_on_right=True,
                             tick_direction='in', tick_length=6, tick_labelsize=None):
    if not log:
        ax.xaxis.set_major_formatter(FuncFormatter(custom_formatter))
        ax.yaxis.set_major_formatter(FuncFormatter(custom_formatter))
    elif log:
        ax.xaxis.set_major_formatter(FuncFormatter(custom_log_formatter))
        ax.yaxis.set_major_formatter(FuncFormatter(custom_log_formatter))
        
    # Inverse the x-axis
    if invert_x:
        ax.invert_xaxis()
    else:
        ax.xaxis.set_inverted(False)
    
    # Move the y-axis to the right
    if y_on_right:
        ax.yaxis.set_label_position("right")
        ax.yaxis.tick_right()
    else:
        ax.yaxis.set_label_position("left")
        ax.yaxis.tick_left()

    #set tick size
    ax.tick_params(axis='both', which='major',
                   labelsize=labelsize-6 if tick_labelsize is None else tick_labelsize,
                   direction=tick_direction, length=tick_length)
    
    # Set axis labels
    ax.set_xlabel(arab('س'), fontsize=labelsize)
    ax.set_ylabel(arab('ص'), fontsize=labelsize)
    


def arabic_3d_axis_formatter(ax, log=False, labelsize=16, *, invert_x=True, invert_y=True,
                             tick_direction='in', tick_length=6, tick_labelsize=None):
    if not log:
        ax.xaxis.set_major_formatter(FuncFormatter(custom_formatter))
        ax.yaxis.set_major_formatter(FuncFormatter(custom_formatter))
        ax.zaxis.set_major_formatter(FuncFormatter(custom_formatter))
    elif log:
        ax.xaxis.set_major_formatter(FuncFormatter(custom_log_formatter))
        ax.yaxis.set_major_formatter(FuncFormatter(custom_log_formatter))
        ax.zaxis.set_major_formatter(FuncFormatter(custom_log_formatter))
        
    # Inverse the x-axis
    if invert_x:
        ax.invert_xaxis()
    else:
        ax.xaxis.set_inverted(False)
    if invert_y:
        ax.invert_yaxis()
    else:
        ax.yaxis.set_inverted(False)

    # Tick font size
    ax.tick_params(axis='both', which='major',
                   labelsize=labelsize-6 if tick_labelsize is None else tick_labelsize,
                   direction=tick_direction, length=tick_length)

    
    # Move the y-axis to the right
    # ax.yaxis.set_label_position("right")
    # ax.yaxis.tick_right()
    
    # Set axis labels
    ax.set_xlabel(arab('س'), fontsize=labelsize)
    ax.set_ylabel(arab('ص'), fontsize=labelsize)
    ax.set_zlabel(arab('ع'), fontsize=labelsize)


def arabic_3d_plot_formatter(log, *, invert_x=True, invert_y=True):
    # Apply the custom formatting to the axis
    if not log:
        plt.gca().xaxis.set_major_formatter(FuncFormatter(custom_formatter))
        plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
        plt.gca().zaxis.set_major_formatter(FuncFormatter(custom_formatter))
    elif log:
        plt.gca().xaxis.set_major_formatter(FuncFormatter(custom_log_formatter))
        plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_log_formatter))
        plt.gca().zaxis.set_major_formatter(FuncFormatter(custom_log_formatter))
        
    # Flip the x-y-axis
    if invert_x:
        plt.gca().invert_xaxis()
    else:
        plt.gca().xaxis.set_inverted(False)
    if invert_y:
        plt.gca().invert_yaxis()
    else:
        plt.gca().yaxis.set_inverted(False)
