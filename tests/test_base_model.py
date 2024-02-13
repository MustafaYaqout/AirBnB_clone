import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        base_model = BaseModel()

        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))

    def test_save_method(self):
        base_model = BaseModel()
        base_model.save()
        self.assertTrue(hasattr(base_model, 'updated_at'))

    def test_to_dict_method(self):
        base_model = BaseModel()
        result = base_model.to_dict()
        
        self.assertEqual(result['__class__'], 'BaseModel')
        self.assertEqual(result['id'], base_model.id)
        self.assertEqual(result['created_at'], base_model.created_at.isoformat())
        self.assertEqual(result['updated_at'], base_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
