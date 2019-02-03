from selenium import webdriver
import selenium
import folium

def get_volcano_list():
    driver = selenium.webdriver.Chrome("C:\Python\chromedriver.exe")
    driver.get("http://volcano.oregonstate.edu/volcano_table")
    d = {}
    for i in driver.find_elements_by_tag_name("tbody"):
        for a in i.find_elements_by_tag_name("tr"):
            cells = a.find_elements_by_tag_name("td")
            if len(cells[3].text) > 0 and len(cells[4].text) > 0:
                d[cells[0].text] = [float(cells[3].text), float(cells[4].text), int(cells[5].text)]
    driver.close()
    print(d)
    return (d)

def color_detector(a):
    if a < 1000:
        cvet = "green"
    elif 1000 < a <= 3000:
        cvet = "orange"
    elif a > 3000:
        cvet = "red"
    return cvet

map = folium.Map(zoom_start=10)
fg = folium.FeatureGroup(name="Map")

def points(dict):

    for el in dict:
        if "'" in el:
            fg.add_child(folium.Marker(location=[dict[el][0], dict[el][1]], popup=el.replace("'", " "), icon=folium.Icon(color=color_detector(dict[el][2]))))
        else:
            fg.add_child(folium.Marker(location=[dict[el][0], dict[el][1]], popup=el, icon=folium.Icon(color=color_detector(dict[el][2]))))
    map.add_child(fg)
    map.save("VOLCANOS.html")



points(get_volcano_list())

