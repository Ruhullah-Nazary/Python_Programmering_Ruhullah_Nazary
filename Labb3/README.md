Beskrivning av programmet:
Det här programmet klassificerar data från en oklassificerad datamängd och sedan visualiserar resultaten med en graf.
I programmet importerar och använder man Pythons tre populära bibliotek som Pandas (används för datamanipulation), Matplotlib.pyplot (används för visualisering) och Numpy (används för numeriska operationer).
Programmet börja läsa data från CSV-fil till en dataFrame med namnet data. Sedan byter man namnet på kolumnerna till x_values och y_values.
Sedan ritar man en linje mellan punkterna med numpy.arrays.
För att klassificera data skapar man en ny kolumn noll_ett i dataFrame och kopierar värde från x_values. Om y_values är större än x_values , sätts noll_ett till 0 annars sätts noll_ett till 1.
Man skapar en klassificering där data som har värdet 0 ligger över linjen och data som har värdet 1 ligger under linjen. I nästa steg bestämmer man att data som tillhör gruppen noll ska ha blå färg och data som tillhör gruppen ett ska ha orange färg. 
