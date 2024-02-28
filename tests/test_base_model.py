import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    @patch('sys.stdout', new_callable=StringIO)
    def test_str(self, mock_stdout):
        print(self.base_model)
        expected_output = "[{}] ({}) {}".format(
            self.base_model.__class__.__name__,
            self.base_model.id,
            self.base_model.__dict__
        )
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch.object(storage, 'save')
    def test_save(self, mock_save):
        self.base_model.save()
        self.assertIsInstance(self.base_model.updated_at, datetime)
        mock_save.assert_called_once()

    def test_to_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'], self.base_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
