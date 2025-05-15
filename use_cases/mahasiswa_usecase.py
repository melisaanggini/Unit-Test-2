from interfaces.mahasiswa_repository import MahasiswaRepositoryInterface
from entities.mahasiswa import Mahasiswa

class MahasiswaUseCases:
    def __init__(self, repo: MahasiswaRepositoryInterface):
        self.repo = repo

    def browse(self):
        return self.repo.list_all()

    def read(self, mahasiswa_id):
        return self.repo.get_by_id(mahasiswa_id)

    def add(self, nama, jurusan):
        new_mhs = Mahasiswa(id=0, nama=nama, jurusan=jurusan)
        self.repo.add(new_mhs)
        return new_mhs

    def edit(self, mahasiswa_id, nama, jurusan):
        mhs = Mahasiswa(id=mahasiswa_id, nama=nama, jurusan=jurusan)
        return self.repo.update(mhs)

    def delete(self, mahasiswa_id):
        return self.repo.delete(mahasiswa_id)
