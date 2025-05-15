from interfaces.mahasiswa_repository import MahasiswaRepositoryInterface
from entities.mahasiswa import Mahasiswa

class InMemoryMahasiswaRepository(MahasiswaRepositoryInterface):
    def __init__(self):
        self.mahasiswa_data = {}
        self.counter = 1

    def list_all(self):
        return list(self.mahasiswa_data.values())

    def get_by_id(self, mahasiswa_id):
        return self.mahasiswa_data.get(mahasiswa_id)

    def add(self, mahasiswa):
        mahasiswa.id = self.counter
        self.mahasiswa_data[self.counter] = mahasiswa
        self.counter += 1

    def update(self, mahasiswa):
        if mahasiswa.id in self.mahasiswa_data:
            self.mahasiswa_data[mahasiswa.id] = mahasiswa
            return True
        return False

    def delete(self, mahasiswa_id):
        if mahasiswa_id in self.mahasiswa_data:
            del self.mahasiswa_data[mahasiswa_id]
            return True
        return False
