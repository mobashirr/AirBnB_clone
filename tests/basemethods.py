import unittest
from unittest.mock import MagicMock
from datetime import datetime
from .. import BaseModel, storage

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        self.assertIsInstance(str(self.base_model), str)

    def test_save(self):
        storage.new = MagicMock()
        storage.save = MagicMock()
        self.base_model.save()
        self.assertTrue(storage.new.called)
        self.assertTrue(storage.save.called)

    def test_to_dict(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)


unittest.main()

# python3 -m unittest  discover tests
