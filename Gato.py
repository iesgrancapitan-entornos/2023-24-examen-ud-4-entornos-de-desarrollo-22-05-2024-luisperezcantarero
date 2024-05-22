"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""


class Gato:

    def maullar(self):
        self.miau = 'maullar'  # Refactorizacion 1 Gato - Luis Pérez Cantarero
        print(self.miau)


g = Gato()
g.maullar()