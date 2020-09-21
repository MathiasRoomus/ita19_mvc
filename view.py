class View:

    def kuva_elemendid(self, elemendid):
        print("Kogu andmestik:")

        print("{:<10}   |   {:>10.2f}".format(element['nimetus'], element['hind'], element['kogus']))
    print("")


    def kuva_element(self, nimetus, element):

        print("Kuvame elemendi {} andmed:".format(nimetus))
        print("{:<10} | {:>10} | {:>10}".format('nimetus', 'hind', 'kogus'))
        print("------------------------------------")
        print("{:<10} | {:>10.2f} | {:>10}".format(element['nimetus'], element['hind'], element['kogus']))



    def veateade(self, tekst):
        print('Tekkis viga: {}.'.format(nimetus))
        print("")
