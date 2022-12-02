import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from matplotlib.colors import Normalize
from matplotlib.textpath import TextPath
from matplotlib.transforms import Affine2D
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import csv
def avg(l): return sum(l)/len(l)
from time import time

class plane:
    def __init__(self, state = None):
        if state is None:
            self.longitude = None
            self.latitude = None
            self.vertical_rate = None
            self.velocity = None
            self.icao24 = None
            self.on_ground = None
            self.orientation = None
        else:    
            self.longitude = state.longitude
            self.latitude = state.latitude
            self.vertical_rate = state.vertical_rate
            self.velocity = state.velocity
            self.icao24 = state.icao24
            self.on_ground = state.on_ground
            self.orientation = state.true_track
    
    def __repr__(self):
        return f"{self.icao24} : ({self.longitude}x{self.latitude})"
    
    @classmethod
    def manual_init(cls, lon, lat, vrate, velo, icao24, on_ground, orientation):
        new = plane()
        new.longitude = lon
        new.latitude = lat
        new.vertical_rate = vrate
        new.velocity = velo
        new.icao24 = icao24
        new.on_ground = on_ground
        new.orientation = orientation
        return new


flights = []
headers = []

with open("flights_1day.csv") as tab:
    csv_reader = csv.reader(tab)
    for flight in csv_reader:
        flights.append(flight)
    headers = flights[0]
    flights = flights[1:]

headers[0] = "index"
tmp = {}
for i in range(len(headers)):
    tmp[headers[i]] = i
headers = tmp

def get_plane(icao24,flights):
    """
    lists all_data about one plane
    """
    print(len(flights))
    res = {}
    to_remove = []
    for flight in flights:
        if flight[headers["icao24"]] == icao24:
            res[flight[headers["time"]]] = plane.manual_init(
                flight[headers["lon"]], 
                flight[headers["lat"]], 
                flight[headers["vertrate"]], 
                flight[headers["velocity"]], 
                flight[headers["icao24"]], 
                flight[headers["onground"]], 
                flight[headers["heading"]])
            to_remove.append(flight)
    print(len(to_remove))
    for f in to_remove:
    #    print(f in flights)
        flights.remove(f)
    #    print(f in flights)
    print(len(flights))
    return res, flights




def plot(trajets, *args, **kwargs):
    
    X = []
    Y = []
    icao24 = ""
    for trajet in trajets:
        plane = trajets[trajet]
        X.append(float(plane.longitude))
        Y.append(float(plane.latitude))
        icao24 = plane.icao24
    
    Xmin = min(X)
    Xmax = max(X)
    Ymin = min(Y)
    Ymax = max(Y)
        
    fig = plt.figure(figsize=(15,15))
    tile=cimgt.GoogleTiles("RGB")
    # Create a GeoAxes in the tile's projection.
    ax = fig.add_subplot(1, 1, 1, projection=tile.crs)
    # Limit the extent of the map to a small longitude/latitude range.
    ax.set_extent([Xmin - 1, Xmax + 1, Ymin - 1, Ymax + 1], crs=ccrs.Geodetic())
    # Add the Stamen data at zoom level 8.
    ax.add_image(tile, 8)

    
    ax.plot(X,Y, transform = ccrs.Geodetic())


    fig.savefig(f"carte{icao24}.jpg")
    #plt.show()


plot(get_plane(flights[0][headers["icao24"]], flights)[0])

def plot_everything(flights):
    X_list = []
    Y_list = []
    list_icao = []
    
    print("go!")
    while len(flights) > 0:
        icao = flight[headers["icao24"]]
        list_icao.append(icao)
        X_list.append([])
        Y_list.append([])
        trajets, flights = get_plane(icao, flights)
        for trajet in trajets:
            plane = trajets[trajet]
            if plane.longitude and plane.latitude:
                X_list[-1].append(float(plane.longitude))
                Y_list[-1].append(float(plane.latitude))
            
    
    
    
    Xmin = min([min(dailyX) for dailyX in X_list])
    Xmax = max([max(dailyX) for dailyX in X_list])
    Ymin = min([min(dailyY) for dailyY in Y_list])
    Ymax = max([max(dailyY) for dailyY in Y_list])
    
    fig = plt.figure(figsize=(15,15))
    tile=cimgt.GoogleTiles("RGB")
    # Create a GeoAxes in the tile's projection.
    ax = fig.add_subplot(1, 1, 1, projection=tile.crs)
    # Limit the extent of the map to a small longitude/latitude range.
    ax.set_extent([Xmin - 1, Xmax + 1, Ymin - 1, Ymax + 1], crs=ccrs.Geodetic())
    # Add the Stamen data at zoom level 8.
    ax.add_image(tile, 8)
    print("go!")
    for i in range(len(list_icao)):
        ax.plot(X_list[i], Y_list[i], transform = ccrs.Geodetic())
    
    fig.savefig("carte_historique.jpg")
    plt.show()

#plot_everything(flights[:1000])