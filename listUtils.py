# %%

class Lista:
    def __init__(self, lista: list = None):
        self.l = lista[:] if lista else []


    def add(self, item: any, position: int = -1) -> "Lista":
        if position < 0:
            position = len(self.l) + 1 + position
        l = self.l[:position] + [item] + self.l[position:]
        return Lista(l)

    def pops(self, item: any = None, position: int = None) -> "Lista":
        l = self.l
        if item:
            self._remove(item)
            return Lista(self.l)
        
        if position:
            l = []
            if position < 0:
                position = len(self.l)+1 + position
            
            for n, i in enumerate(self.l):
                if n != position:
                    l.append(i)
            self.l = l
            return Lista(self.l)
    
    def index(self, item: any) -> tuple:
        return self._index(item)
        
    def _index(self,item) -> tuple:
        indexes = []
        for n, i in enumerate(self.l):
            if i == item:
                indexes.append(n)
        return tuple(indexes)
    
    def _remove(self, item: any) -> "Lista":
        self.l = [i for i in self.l if i != item]
        return Lista(self.l)

    def replace(self, *shifts: list | tuple) -> "Lista":
        l = []
        for i in self.l:
            appended = False
            
            for shift in shifts:
                old = shift[0]
                new = shift[1]

                if i == old:
                    l.append(new)
                    appended = True
            if not appended:
                l.append(i)
        self.l = l
        return Lista(self.l)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return Lista(self.l[key])
        return self.l[key]

    def __iter__(self) -> iter:
        return iter(self.l)

    def __len__(self) -> int:
        return len(self.l)

    def __str__(self) -> str:
        return str(self.l)

    def __setitem__(self, item, posicion: int) -> 'Lista':
        self.l[posicion] = item
        return self.l

    def __contains__(self, item) -> bool:
        return item in self.l

    def __add__(self, other) -> 'Lista': # mejorar
        if isinstance(other, Lista):
            return Lista(self.l + other.l)
        elif isinstance(other, list):
            return Lista(self.l + other)
        return Lista(self.l + [other])

    def __call__(self, *args: any, **kwds: any) -> 'Lista':
        return [i for i in self.l]

    def __repr__(self):
        return str(self.l)


