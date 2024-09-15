import plotly.graph_objects as go

# Dane
names = ["Mark", "John", "Daniel", "Greg"]
salaries = [1000, 1500, 2300, 5000]

# Tworzenie wykresu
fig = go.Figure(data=[go.Bar(x=names, y=salaries)])

# Dodanie tytułu i etykiet
fig.update_layout(
    title='Pensje pracowników',
    xaxis_title='Imię',
    yaxis_title='Pensja',
    yaxis=dict(tickprefix="$")
)

# Wyświetlenie wykresu
fig.show()
