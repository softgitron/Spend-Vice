import sys
from pymongo import MongoClient
import datetime
import random

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.io import export_png


class Product:
        def __init__(self, name, purchaseDate, price, usage):
                self.name = name
                self.purchaseDate = purchaseDate
                self.price = price
                self.usage = usage
                self.dateDiff = datetime.datetime.now() - purchaseDate
                self.eurPerWeek = price / usage
                self.nextSixMonths = [0, 0, 0, 0, 0, 0]
                counter = self.usage - round(self.dateDiff.days / 7, 0)
                index = 0
                while (counter > 0 and index <= 5):
                        if (self.usage <= 4):
                                self.nextSixMonths[index] = self.price
                        else:
                                self.nextSixMonths[index] = round(4* self.eurPerWeek, 0)
                        index += 1
                        counter -= 4
                
        def __str__(self):
                return("name {0}\ndate {1}\nprice {2}\nusage {3}".format(self.name, self.purchaseDate, self.price, self.usage))

def main():
        products = []
        if (len(sys.argv) > 1): 
                username = sys.argv[1]
        else:
                username ="JokuPelle"

        client = MongoClient('mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas')
        #print(client.list_database_names())
        db = client['Datas']
        #print(db.list_collection_names())

        collection = db.buymodels


        for user in collection.find( {'username': '{0}'.format(username)} ):
                for product in db.datamodels.find( {'ean': user["ean"] } ):
                        products.append(Product(product["name"], user["buydate"], product["price"], product["usage"]))



        client.close()

        plot(products)


def plot(products):
        months = ["November", "December", "January", "February", "March", "April"]
        purchases = []

        colors = ["#BAFD00", "#95CB00", "#719A00", "#537200", "#1B7200", "#27A600", "#32D800", "#40F50A", "#66FF37", "#B0FF98"]

        data = {'months' : months}
        for product in products:
                purchases.append(product.name)
                data[product.name] = product.nextSixMonths

        colors = colors[0:len(purchases)]



        output_file("stacked.html")

        p = figure(x_range=months, plot_height=250, title="Price breakdown for the next six months", toolbar_location=None, tools="")

        p.vbar_stack(purchases, x='months', width=0.45, color=colors, source=data, legend_label=purchases)


        p.y_range.start = 0
        p.y_range.end = 50
        #Don't touch, will F up formatting if more than ~3 items.
        #p.plot_width = 400
        p.x_range.range_padding = 0.1
        p.xgrid.grid_line_color = None
        p.axis.minor_tick_line_color = None
        p.outline_line_color = None
        p.legend.location = "top_left"
        p.legend.orientation = "horizontal"

        show(p)
        
        if (len(sys.argv) > 2): 
                path = sys.argv[1]
        else:
                path = "."
        randomInt = random.randrange(100000, 99999999)
        export_png(p, filename="{0}/plot{1}.png".format(path, randomInt))
        print("{0}/plot{1}.png".format(path, randomInt))
        sys.stdout.flush()

main()