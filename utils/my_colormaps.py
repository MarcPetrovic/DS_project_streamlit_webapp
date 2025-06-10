from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# Farbwerte definieren
colors = ['#C00000', '#191919', '#d9d9d9', '#f3f3f3', '#0097A7', '#097a80']

# Diskrete Farbkarte
my_cmap = ListedColormap(colors, name="my_cmap")

# Umgekehrte Farbkarte
my_cmap_r = my_cmap.reversed()

# Lineare, interpolierte Farbkarte
cmap_4 = LinearSegmentedColormap.from_list("custom_linear", colors)
