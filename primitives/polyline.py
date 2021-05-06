class polyline:
    def __init__(self, coords = []):
        # verification que les coordonnees sont de la forme [(number,number)*]
        try:
            all(isinstance(c, tuple) and all([isinstance(x, (int, float)) for x in c]) for c in coords)
        except:
            print("all coordinates should be tuple of numbers")

        self.coords = coords


    def len(self):
        return len(self.coords)

    def __getitem__(self, index):
        return self.coords[index]

    def addPt(self, p):
        try:
            all([isinstance(x, (int, float)) for x in p])
        except:
            print("all coordinates should be tuple of numbers")
        self.coords.append(p)

    def toHPGL(self):
        cmd = []
        cmd += 'PU' + str(self.coords[0].first) + ',' + str(self.coords[0].second) + ';PD'
        for c in self.coords:
            cmd += str(self.coords[i].first) + ',' + str(self.coords[i].second) + ','
        cmd[-1] = ';'
