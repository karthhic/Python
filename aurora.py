from lxml import html
import requests

page = requests.get('http://www.aurora-service.eu/aurora-forecast-non-flash/')
tree = html.fromstring(page.content)
forecast = tree.xpath('//span[@style="color: #0000ff;"]/text()')
forecast2 = tree.xpath('//h5[@style="text-align: center;"]/text()')

def prs(val):
    spli = val.split(" ")
    return(spli[1])
    #return(val)

def prs1(val):
    spli = val.split("  ")
    return(spli[1])
    #return(val)

print("Current value: "+str(prs1(forecast[0])))
print(str(forecast2[0])+str(forecast[1])+str(forecast2[1])+str(prs(forecast[2])))
print(str(forecast2[3])+str(forecast[3])+str(forecast2[4])+str(prs(forecast[4])))
print(str(forecast2[6])+str(forecast[5])+str(forecast2[7])+str(prs(forecast[6])))

