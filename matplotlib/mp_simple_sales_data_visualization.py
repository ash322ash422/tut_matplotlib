import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate sample data
def generate_data():
    dates = pd.date_range('2023-01-01', periods=12, freq='M')
    sales = np.random.randint(1000, 5000, size=12)
    expenses = np.random.randint(500, 2500, size=12)
    profits = sales - expenses

    # Creating a DataFrame for easy data manipulation
    data = pd.DataFrame({
        'Date': dates,
        'Sales': sales,
        'Expenses': expenses,
        'Profits': profits
    })
    # data.to_csv("junk.csv")
    # data.to_excel("junk.xlsx") # need module 'openpyxl' installed
    return data

# Plotting a Line Plot for Sales, Expenses, and Profits over Time
def plot_line_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Sales'], label='Sales', marker='o')
    plt.plot(data['Date'], data['Expenses'], label='Expenses', marker='o')
    plt.plot(data['Date'], data['Profits'], label='Profits', marker='o')

    plt.title('Sales, Expenses, and Profits Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount in USD')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plotting a Bar Chart for Monthly Sales vs Expenses
def plot_bar_chart(data):
    months = data['Date'].dt.month_name()
    x = np.arange(len(months))

    plt.figure(figsize=(10, 6))
    bar_width = 0.35
    plt.bar(x - bar_width/2, data['Sales'], bar_width, label='Sales', color='b')
    plt.bar(x + bar_width/2, data['Expenses'], bar_width, label='Expenses', color='r')

    plt.title('Sales vs Expenses in Each Month')
    plt.xlabel('Month')
    plt.ylabel('Amount in USD')
    plt.xticks(x, months, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Plotting a Pie Chart for Sales Proportions
def plot_pie_chart(data):
    total_sales = data['Sales'].sum()
    total_expenses = data['Expenses'].sum()
    total_profits = data['Profits'].sum()

    labels = ['Sales', 'Expenses', 'Profits']
    sizes = [total_sales, total_expenses, total_profits]
    colors = ['gold', 'lightcoral', 'lightgreen']
    explode = (0.1, 0, 0)  # "explode" the Sales section

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.title('Proportions of Sales, Expenses, and Profits')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# Plotting a Histogram for the Distribution of Profits
def plot_histogram(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data['Profits'], bins=6, color='lightblue', edgecolor='black', alpha=0.7)

    plt.title('Distribution of Profits')
    plt.xlabel('Profit in USD')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Plotting a Scatter Plot for Sales vs Profits
def plot_scatter_plot(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Sales'], data['Profits'], color='purple', label='Sales vs Profits')

    plt.title('Scatter Plot of Sales vs Profits')
    plt.xlabel('Sales in USD')
    plt.ylabel('Profits in USD')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main function to generate data and display plots
def main():
    data = generate_data()
    print("Generated Data:")
    print(data)

    # Call functions to display each type of plot
    plot_line_chart(data)
    plot_bar_chart(data)
    plot_pie_chart(data)
    plot_histogram(data)
    plot_scatter_plot(data)

if __name__ == "__main__":
    main()
