import json
from urllib.request import urlopen
import pandas as pd
import plotly.express as px
import random

def test():
    # Download the simplified geojson
    url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson"
    try:
        with urlopen(url) as response:
            france_geojson = json.load(response)
    except Exception as e:
        print(f"Error fetching GeoJSON: {e}")
        return

    random.seed(42)
    deps = [f"{i:02d}" for i in range(1, 96) if i != 20] + ["2A", "2B"]
    
    # Generate values that roughly match the mockup's coloring
    def get_val(d):
        if d in ["75", "92", "93", "94"]:
            return random.uniform(90, 100)
        elif d in ["69", "13", "59", "33", "44", "31", "06", "34", "67", "38"]:
            return random.uniform(70, 88)
        elif d in ["23", "15", "48", "04", "05", "09", "32", "46", "43", "48", "53", "55", "52", "09", "12"]:
            return random.uniform(8, 25)
        else:
            return random.uniform(30, 68)

    vals = [get_val(d) for d in deps]

    df_map = pd.DataFrame({
        "code": deps,
        "Taux d'urbanisation": vals
    })

    fig = px.choropleth(
        df_map,
        geojson=france_geojson,
        locations="code",
        featureidkey="properties.code",
        color="Taux d'urbanisation",
        color_continuous_scale="Blues",
        range_color=[0, 100],
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        coloraxis_colorbar=dict(
            title="Taux d'urbanisation",
            thicknessmode="pixels", thickness=15,
            lenmode="pixels", len=200,
            yanchor="top", y=0.8,
            ticksuffix="%",
        )
    )
    
    html = fig.to_html(full_html=True)
    with open("test_map.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Success: test_map.html generated!")

if __name__ == "__main__":
    test()
