from dataLoader import DataLoader
from analysis import Analyzer
from visuals import Visualizer
import matplotlib.pyplot as plt

def main():
    path = "Books.csv"  
    loader = DataLoader(path)
    df = loader.load_data()

    analyzer = Analyzer(df)
    visualizer = Visualizer()

    while True:
        print("\n📚 Dream Book Shop - CLI Data Explorer")
        print("1. Books Published Per Year")
        print("2. Top 5 Authors")
        print("3. Language Distribution")
        print("4. Books Per Publisher")
        print("5. Missing ISBN Count")
        print("6. Books Per Year by Language")
        print("0. Exit\n")

        choice = input("Enter choice number: ")

        if choice == "1":
            data = analyzer.books_per_year()
            print("\nBooks Published Per Year:\n", data)
            visualizer.show_bar(data, "Books Published Per Year")

        elif choice == "2":
            data = analyzer.top_authors()
            print("\nTop 5 Authors:\n", data)
            visualizer.show_bar(data, "Top 5 Authors")

        elif choice == "3":
            data = analyzer.language_distribution()
            print("\nLanguage Distribution:\n", data)
            visualizer.show_pie(data, "Language Distribution")

        elif choice == "4":
            data = analyzer.books_per_publisher().head(10)
            print("\nBooks Per Publisher (Top 10):\n", data)
            visualizer.show_bar(data, "Top 10 Publishers")

        elif choice == "5":
            missing, percent = analyzer.missing_isbn()
            print(f"\nMissing ISBNs: {missing} ({percent:.2f}%)")

        elif choice == "6":
            data = analyzer.books_year_language()
            print("\nBooks Per Year by Language:\n", data)
            data.plot(kind='bar', stacked=True, figsize=(12,6), title="Books/Year by Language")
            plt.tight_layout()
            plt.show()

        elif choice == "0":
            print("👋 Exiting the program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main()
