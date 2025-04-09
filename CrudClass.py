class zene:
    def __init__(self, sor):
        obliterate = sor.split(";")
        self.eloado = obliterate[0].strip()
        self.zenecim = obliterate[1].strip()
        self.hossz = obliterate[2].strip()