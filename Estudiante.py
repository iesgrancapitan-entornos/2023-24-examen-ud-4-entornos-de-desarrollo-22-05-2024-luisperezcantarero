"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
nombre
apellidos
nif
"""


class Persona:
    apellidos = "Apellidos";
    nombre = "Nombre";
    nif = "11111111Z";

    def __init__(self):
        """
        Constructor de la clase Persona.

        :author: Luis Pérez Cantarero
        """
        self.__nif = value
        self.__nombre = value
        self.__apellidos = value


class Estudiante(Persona):
    curso = "Primaria";

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Constructor de la clase Estudiante.
        :author: Jaime Rabasco

        :param nif:
        :param curso:
        :param nombre:
        :param apellidos:
        """
        self.nif = nif;
        self.curso = curso;
        self.nombre = nombre;
        self.apellidos = apellidos;

    @property
    def nif(self):
        """
        Getter de nif de la clase Estudiante.
        :author: Jaime Rabasco
        :return:
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        Setter de nif de la clase Estudiante.
        :author: Jaime Rabasco
        :param value:
        """
        self.__nif = value

    @property
    def curso(self):
        """
        Getter de curso de la clase Estudiante.
        :author: Jaime Rabasco
        :return:
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Setter de curso de la clase Estudiante.
        :author: Jaime Rabasco
        :param value:
        """
        self.__curso = value

    @property
    def nombre(self):
        """
        Getter de nombre de la clase Estudiante.
        :author: Jaime Rabasco
        :return:
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Setter de nombre de la clase Estudiante.
        :author: Jaime Rabasco
        :param value:
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """
        Getter de apellidos de la clase Estudiante.
        :author: Jaime Rabasco
        :return:
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        Setter de apellidos de la clase Estudiante.
        :author: Jaime Rabasco
        :param value:
        """
        self.__apellidos = value
