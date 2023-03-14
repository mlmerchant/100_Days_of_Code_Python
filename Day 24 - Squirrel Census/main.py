import pandas

# Squirrel Data Available at following URL:
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
data = pandas.read_csv("Squirrel_Data.csv")

fur_color = data["Primary Fur Color"]
gray_count = len(fur_color[fur_color == "Gray"])
cinnamon_count = len(fur_color[fur_color == "Cinnamon"])
black_count = len(fur_color[fur_color == "Black"])

fur_color_count_dict = {
    "Color": ['grey', 'red', 'black'],
    "Count": [gray_count, cinnamon_count, black_count]
}

data = pandas.DataFrame(fur_color_count_dict)
data.to_csv('Squirrel_Count.csv')

