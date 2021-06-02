import matplotlib.pyplot as plt

def plot_problem(disks: [], rect, filename=None):
    '''Visualises the data of the problem'''
    
    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    ax.set_xlim(rect.x_min, rect.x_max)
    ax.set_ylim(rect.y_min, rect.y_max)
    # print(rect.y_min, rect.y_max)
    for d in disks:
        circle = plt.Circle((d.x, d.y), d.r, color='r')
        ax.add_patch(circle)
        print(d.x, d.y, d.r)

    ax.set_title('Problem visualisation')
    if filename:
        fig.savefig(filename)
    else:
        fig.show()