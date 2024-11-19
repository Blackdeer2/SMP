import matplotlib.pyplot as plt
import pandas as pd


class BasicVisualizer:
    """A class for basic visualization of data."""

    def __init__(self, data):
        """
        Initializes the BasicVisualizer with data.

        Args:
            data (pandas.DataFrame): The data to be visualized.
        """
        self.data = data

    def plot_line_chart(self, x_column, y_column):
        """
        Plots a line chart showing the average sale price per year.

        Args:
            x_column (str): The column to be used on the x-axis.
            y_column (str): The column to be used on the y-axis.
        """
        average_price_per_year = self.data.groupby('Year_of_Manufacture__c')['Sale_Price__c'].mean()

        # Build the line chart
        plt.figure(figsize=(10, 6))
        plt.plot(average_price_per_year.index, average_price_per_year.values, marker='o', color='g', linestyle='-')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid(True)
        plt.show()
