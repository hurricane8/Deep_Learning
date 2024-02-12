import matplotlib.pyplot as plt
import seaborn as sns

class DataPlotter:
    def __init__(self):
        # Set the style and custom palette
        sns.set(style="whitegrid")
        #plt.style.use('seaborn-dark-palette')
        #plt.rcParams['figure.facecolor'] = 'white'
        
        
    def line_graph(self, x_data, y_data, x_label = '', y_label = '', title = '', line_label = 'Line 1'):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x_data, y_data, label= line_label, linewidth=4)
        ax.legend(loc="upper right", fontsize=15)
        ax.set_xlabel(x_label, fontsize=15)
        ax.set_ylabel(y_label, fontsize=15)
        ax.set_title(title, fontsize=15)
        fig.canvas.draw()
        plt.tight_layout()
        plt.show()
        

    def scatter(self, x_data, y_data, x_label = '', y_label = '', title = ''):
        plt.figure(figsize=(8, 6))
        plt.scatter(x_data, y_data)
        plt.xlabel(x_label, fontsize=15)
        plt.ylabel(y_label, fontsize=15)
        plt.title(title, fontsize=15)
        plt.tight_layout()
        plt.show()

    def bar_chart(self, x_data, y_data):
        sns.barplot(x=x_data, y=y_data)
        plt.tight_layout()
        plt.show()

    def pie_chart(self, data, labels):
        plt.pie(data, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
