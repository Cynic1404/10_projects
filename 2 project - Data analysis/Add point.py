"""
import folium
map = folium.Map(zoom_start=2)
fg = folium.FeatureGroup(name="Sranaya india")
fg.add_child(folium.Marker(location=[1, 1], popup=("hhh"), icon=folium.Icon(icon_color="green", color="orange")))
map.add_child(fg)

map.save("conas.html")
"""

import folium
map = folium.Map(zoom_start=2)
fg = folium.FeatureGroup(name="Point")
fg.add_child(folium.CircleMarker(location=[10,15], radius=5, popup="ahahahahahahaha", fill_color = "blue",  color = "black", fill_opacity = 0.7, fill = True))
map.add_child(fg)

map.save("2.html")