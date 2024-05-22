"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""


class Gato:

    def maullar(self):
        """
        Función maullar de la clase Gato.

        :author: Jaime Rabasco
        """
        self.miau = 'maullar'
        print(self.miau)


g = Gato()
g.maullar()
