import matplotlib.pyplot as plt
from Lab_8.BasicVisualizer import BasicVisualizer


class MultiPlotVisualizer(BasicVisualizer):
    """A class for visualizing multiple plots in a grid layout."""

    def plot_multiple(self):
        """
        Creates a 2x2 grid of subplots displaying multiple visualizations including:
        - Sale Price Over Year (line plot)
        - Mileage vs Sale Price (scatter plot)
        - Condition Distribution (bar chart)
        - Fuel Type Distribution (pie chart)
        """
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))

        # Sale Price Over Year (line plot)
        average_price_per_year = self.data.groupby('Year_of_Manufacture__c')['Sale_Price__c'].mean()
        axs[0, 0].plot(average_price_per_year.index, average_price_per_year.values, marker='o', linestyle='-')
        axs[0, 0].set_title('Sale Price Over Year')

        # Mileage vs Sale Price (scatter plot)
        axs[0, 1].scatter(self.data['Mileage__c'], self.data['Sale_Price__c'])
        axs[0, 1].set_title('Mileage vs Sale Price')

        # Condition Distribution (bar chart)
        self.data['Condition__c'].value_counts().plot(kind='bar', ax=axs[1, 0], color=['blue', 'orange'])
        axs[1, 0].set_title('Condition Distribution')

        # Fuel Type Distribution (pie chart)
        self.data['Fuel_Type__c'].value_counts().plot(kind='pie', ax=axs[1, 1], autopct='%1.1f%%')
        axs[1, 1].set_title('Fuel Type Distribution')

        plt.tight_layout()
        plt.show()
