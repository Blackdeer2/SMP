from DAL.DataAnalyzer import DataAnalyzer
from DAL.DataLoader import DataLoader
from DAL.DataPreparer import DataPreparer
from Lab_8.AdvancedVisualizer import AdvancedVisualizer
from Lab_8.BasicVisualizer import BasicVisualizer
from Lab_8.MultiPlotVisualizer import MultiPlotVisualizer
from UI.MenuItem import MenuItem
from UI.MenuBuilder import MenuBuilder


class VisualizationApp:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.prepared_data = self._prepare_data()

    def _prepare_data(self):
        """Автоматичне завантаження, аналіз та підготовка даних."""
        print("Завантаження даних...")
        loader = DataLoader(self.filepath)
        data = loader.get_data()

        print("Аналіз даних...")
        analyzer = DataAnalyzer(data)
        print("Екстремальні значення:")
        print(analyzer.get_extreme_values())

        print("Підготовка даних для візуалізації...")
        preparer = DataPreparer(data)
        return preparer.prepare_data_for_visualization()

    def plot_line_chart(self):
        """Побудова лінійного графіка."""
        visualizer = BasicVisualizer(self.prepared_data)
        visualizer.plot_line_chart('Mileage__c', 'Sale_Price__c')

    def plot_scatter_and_bar(self):
        """Побудова точкового графіка та гістограми."""
        visualizer = AdvancedVisualizer(self.prepared_data)
        visualizer.plot_scatter('Mileage__c', 'Sale_Price__c')
        visualizer.plot_bar_chart('Engine_Power__c', 'Sale_Price__c')

    def plot_multiple(self):
        """Побудова кількох графіків."""
        visualizer = MultiPlotVisualizer(self.prepared_data)
        visualizer.plot_multiple()


def main():
    filepath = "C:/VOVA/5 semester/SMP/calculator/Source/CarsCSV.csv"
    app = VisualizationApp(filepath)

    menu_items = [
        MenuItem("1", "Побудувати лінійний графік", app.plot_line_chart),
        MenuItem("2", "Побудувати точковий графік і гістограму", app.plot_scatter_and_bar),
        MenuItem("3", "Побудувати кілька графіків", app.plot_multiple),
        MenuItem("0", "Вийти", exit),
    ]

    menu = MenuBuilder(menu_items)
    while True:
        menu.initialize()
