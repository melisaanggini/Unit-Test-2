import unittest
from use_cases.mahasiswa_usecase import MahasiswaUseCases
from infrastructure.in_memory_repo import InMemoryMahasiswaRepository

class TestMahasiswaUseCase(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryMahasiswaRepository()
        self.usecase = MahasiswaUseCases(self.repo)

    # --- ADD ---
    def test_add_mahasiswa(self):
        mhs = self.usecase.add("Budi", "Informatika")
        self.assertEqual(mhs.nama, "Budi")
        self.assertEqual(mhs.jurusan, "Informatika")

    def test_add_duplicate_name(self):
        self.usecase.add("Doni", "Matematika")
        self.usecase.add("Doni", "Hukum")
        self.assertEqual(len(self.usecase.browse()), 2)

    def test_add_with_empty_fields(self):
        mhs = self.usecase.add("", "")
        self.assertEqual(mhs.nama, "")
        self.assertEqual(mhs.jurusan, "")

    # --- EDIT ---
    def test_edit_mahasiswa(self):
        mhs = self.usecase.add("Andi", "Biologi")
        self.usecase.edit(mhs.id, "Andi Wijaya", "Kimia")
        updated = self.usecase.read(mhs.id)
        self.assertEqual(updated.nama, "Andi Wijaya")
        self.assertEqual(updated.jurusan, "Kimia")

    def test_edit_non_existing(self):
        result = self.usecase.edit(999, "Zahra", "Akuntansi")
        self.assertFalse(result)

    # --- DELETE ---
    def test_delete_mahasiswa(self):
        mhs = self.usecase.add("Sari", "Fisika")
        deleted = self.usecase.delete(mhs.id)
        self.assertTrue(deleted)

    def test_delete_invalid_id(self):
        result = self.usecase.delete(999)
        self.assertFalse(result)

    # --- READ ---
    def test_read_invalid_id(self):
        self.assertIsNone(self.usecase.read(999))

    # --- BROWSE ---
    def test_browse_multiple_mahasiswa(self):
        self.usecase.add("Budi", "Informatika")
        self.usecase.add("Dina", "Sastra")
        self.usecase.add("Eko", "Teknik")
        data = self.usecase.browse()
        self.assertEqual(len(data), 3)

    def test_browse_after_delete_all(self):
        m1 = self.usecase.add("Lina", "Biologi")
        m2 = self.usecase.add("Rina", "Fisika")
        self.usecase.delete(m1.id)
        self.usecase.delete(m2.id)
        self.assertEqual(self.usecase.browse(), [])

if __name__ == "__main__":
    unittest.main()
