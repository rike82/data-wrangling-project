import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Dictionary für Monatsabkürzungen
month_dict = {
    '1': 'Jan',
    '2': 'Feb',
    '3': 'Mar',
    '4': 'Apr',
    '5': 'May',
    '6': 'Jun',
    '7': 'Jul',
    '8': 'Aug',
    '9': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
}

def get_data(url):
    df = pd.read_excel(url)
    return df


def columns_rename_month_year(firstcol, columns):
    columns = firstcol + [pd.to_datetime(col) if not isinstance(col, pd.Timestamp) else col for col in columns[1:]]
    columns = firstcol + [col.strftime('%m/%Y') if isinstance(col, pd.Timestamp) else col for col in columns[1:]]
    return columns

def column_rename_months(firstcol, columns):
    new_columns = []

    # Iteriere über die Spaltennamen ab der zweiten Spalte
    for col in columns[1:]:  # Hier sollte columns und nicht columns1 stehen
        month, year = col.split('/')  # Spaltennamen aufteilen
        month_name = month_dict[str(int(month))]  # Monat durch Abkürzung ersetzen
        new_columns.append(f"{month_name} {year}")  # Neuer Spaltenname z.B. 'Jan 2018'
    
    columns = firstcol + new_columns  # Du musst firstcol als Liste hinzufügen
    return columns



def melt_and_filter (df, column, var, value, rows):
    values = df.melt(id_vars = column,
                    var_name = var,
                    value_name = value)
    filtered_values = values[values[column].isin(rows)]
    
    return filtered_values

# Plot
def create_graph (df, y_max, ticks, graph_title = None, axis_x = None, axis_y = None, df_column = None, rows_of_df = None):
    graph_title = input("Please enter graphs name: ")
    axis_x = input("What should the name of the x-axis be?: ")
    axis_y = input("What should the name of the y-axis be?: ")
    rows_of_df = input("Which row/s of your dataframe should be used (comma separated)?: ")
    rows_of_df = [row.strip() for row in rows_of_df.split(",")] if rows_of_df else []
    df_column = input("Which is the column these row/s is/are from?: ")


    plt.figure(figsize=(20, 12))
    ax = sns.barplot(x = axis_x, y = axis_y, hue = df_column, data = melt_and_filter(df, df_column, axis_x, axis_y, rows_of_df), palette = 'dark')
    plt.legend(fontsize=14)


    # Setzen von benutzerdefinierten y-Achsen-Ticks
    plt.yticks(ticks)

    plt.title(graph_title, fontsize = 16)
    plt.xlabel(axis_x, fontsize = 14)
    plt.ylabel(axis_y, fontsize = 14)
    ax.set_ylim(0,y_max )
    plt.xticks(rotation = 60)  # Für bessere Lesbarkeit
    plt.legend(title = df_column)

    plt.show()


def formatting_values_four_decimals(df):
    df.iloc[:, 1:] = df.iloc[:, 1:].round(4)

# Umwandeln der ersten Zeile in int, falls der Wert eine ganze Zahl darstellt
    df.iloc[0, 1:] = df.iloc[0, 1:].apply(lambda x: int(x) if isinstance(x, (float, int)) and x % 1 == 0 else x)

# Anpassen der Anzeigeoptionen, um wissenschaftliche Notation zu verhindern
    pd.options.display.float_format = '{:.4f}'.format
    return df
