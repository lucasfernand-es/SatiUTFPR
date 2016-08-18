from aenum import Enum


class Acess(Enum):
    Administrator = 0
    Instructor = 1
    Student = 2


class Status(Enum):
    Inativo = 0
    Ativo = 1
