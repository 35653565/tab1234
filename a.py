
sp500 = {'lll': '3', 'kkkk':'4', '888':'2'}
forcast = {'lll': 3, 'kkkk': 4, '888':2}
newDict = {}

for keys in sp500:
    newDict[keys] = forcast[keys] * int(sp500[keys]) / 100
print(newDict)
for keys in sp500:
    newDict[keys] = int(float(conv_percentage(forcast[keys]))) * int(float(sp500[keys])) / 100
    print(newDict)
    if keys == 'NWS':