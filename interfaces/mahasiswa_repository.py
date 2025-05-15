from typing import List, Optional
from entities.mahasiswa import Mahasiswa

class MahasiswaRepositoryInterface:
    def list_all(self) -> List[Mahasiswa]: pass
    def get_by_id(self, mahasiswa_id: int) -> Optional[Mahasiswa]: pass
    def add(self, mahasiswa: Mahasiswa) -> None: pass
    def update(self, mahasiswa: Mahasiswa) -> bool: pass
    def delete(self, mahasiswa_id: int) -> bool: pass
