import matplotlib.pyplot as plt

class Visualizer:
    def show_bar(self, data, title):
        data.plot(kind='bar', title=title)
        plt.tight_layout()
        plt.show()

    def show_pie(self, data, title):
        data.plot(kind='pie', autopct='%1.1f%%', title=title)
        plt.ylabel('')
        plt.tight_layout()
        plt.show()
