# administration/repositories.py
from abc import ABC, abstractmethod
from .models import Computer

class ComputerRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self):
        pass

class DjangoORMComputerRepository(ComputerRepositoryInterface):
    def get_all(self):
        return Computer.objects.all()
