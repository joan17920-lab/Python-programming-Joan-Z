Denna programm kommer att klassifiera punkterna enligt linjer, de som ligger till vänster/under labelleras till 0, högre/ovan till 1 och en ny csv fil skapas som innehåller data och label. Programmen visar ochså en graf med klassiferade punter och linjer.

För att använda program behöver classified.py, Labb3.py och unlabelled_data.csv laddas ner i en map, sedan kör Labb3.py.

 __obs:__ du behöver justera path till fil. 

 - unlabelled = np.loadtxt("../Python-programming-Joan-Z/Labs/Labb3/unlabelled_data.csv", delimiter=",")
 - np.savetxt("../Python-programming-Joan-Z/Labs/Labb3/labelled_data.csv",labeled, delimiter=",", fmt=["%.16f", "%.16f", "%d"])
