from gmaps.figure import FigureLayout
import pandas as pd
import gmaps
import gmaps.datasets
from ipywidgets.embed import embed_minimal_html

# docs: https://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html#heatmaps

API_KEY = "AIzaSyDKHoSJ2IquAFdaqitxPfF2ZsxyNK53siI"
DIR_PATH = "/Users/aaronbastian/Documents/MedicalSchool/NYIT/Granatosky_Lab/Python/DataAnalysis/Heatmap/"
data = pd.read_excel(DIR_PATH + "parrot-positional-behavior.xlsx").dropna()


def main():
    gmaps.configure(api_key='AIzaSyDKHoSJ2IquAFdaqitxPfF2ZsxyNK53siI')
    
    locs = get_locations()
    center_coords = (40.65231269593503, -73.9905872575025)
    figure_layout = {'width': '500px', 'margin': '0 auto 0 auto'}
    fig = gmaps.figure(map_type='HYBRID', center=center_coords ,zoom_level=14, layout=figure_layout)

    # UN-WEIGHTED
    # heatmap_layer = gmaps.heatmap_layer(
    #     locs[["latitude", "longitude"]],
    #     max_intensity = 100, point_radius = 5.0
    # )
    
    # WEIGHTED
    heatmap_layer = gmaps.heatmap_layer(
        locs[["latitude", "longitude"]], weights=locs["weights"],
        max_intensity = 100, point_radius = 5.0
    )

    fig.add_layer(heatmap_layer)
    embed_minimal_html(DIR_PATH + "WEIGHTED.html", views=[fig])




def get_locations():
    locs = {
        "latitude" : [],
        "longitude" : [],
        "weights" : []
    }

    for row in data.index:
        lat = data["Latitude"][row]
        long = data["Longitude"][row]
        weight = data["Number of individuals"][row]

        if isinstance(lat, str):
            # correctly formats incorrect data entries to floats
            lat = float(lat.replace("°", "").strip())
            long = float(long.replace("°", "").strip())

        if long < -180 or long > 180:  # Janky correction of values without decimal point
            long = long/1000000

        locs["latitude"].append(lat)
        locs["longitude"].append(long)
        locs["weights"].append(weight)
    
    return pd.DataFrame(locs)


if __name__ == "__main__":
    main()