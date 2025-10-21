### README
Detta program klassificerar datapunkter i förhållande till givna linjer.
Punkter som ligger till **vänster eller under** linjen får etiketten **0**, medan punkter **ovanför eller till höger** får etiketten **1**.
Ett nytt CSV-dokument skapas som innehåller både de ursprungliga datapunkterna och deras tilldelade etiketter.

Programmet visar även en grafisk visualisering där datapunkterna och klassificeringslinjerna ritas ut.

### Användning

För att köra programmet behöver följande filer finnas i samma mapp och kör därefter filen Labb3.py.:
| Filnamn | Beskrivning |
|----------|--------------|
| classified.py | Klassificeringsfunktion |
| Labb3.py | Huvudprogram |
| unlabelled_data.csv | Ursprunglig data |


>  **Obs**: Du behöver justera sökvägarna (path) till filerna i koden.

```unlabelled = np.loadtxt("../path/unlabelled_data.csv", delimiter=",")

np.savetxt("../path/labelled_data.csv",labeled, delimiter=",", fmt=["%.16f", "%.16f", "%d"])```