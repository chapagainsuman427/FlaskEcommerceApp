import unittest
from app import app
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# MongoDB connection class
class MongoDBTestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up MongoDB connection using the URI from environment variables.
        """
        mongodb_uri = os.getenv('MONGODB_URI')
        if not mongodb_uri:
            raise ValueError("MongoDB URI not found in environment variables.")
        cls.client = MongoClient(mongodb_uri)
        cls.db = cls.client['shop_db']
        cls.collection = cls.db['products']

# Test 1: Route Test
class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_invalid_method_on_products(self):
        """
        Test that a POST request to the /products route returns a 405 status code.
        """
        response = self.client.post('/products')
        self.assertEqual(response.status_code, 405)

# Test 2: Database Read Test
class TestDatabaseRead(MongoDBTestBase):
    def test_mongodb_connection(self):
        """
        Test MongoDB connection using the ping command.
        """
        try:
            self.client.admin.command('ping')
        except Exception as e:
            self.fail(f"MongoDB connection failed: {str(e)}")

# Test 3: Database Write Test
class TestDatabaseWrite(MongoDBTestBase):
    def setUp(self):
        """
        Set up test database and collection.
        """
        self.db = self.client['shop_db']
        self.collection = self.db['products']

    def tearDown(self):
        """
        Clean up test database after tests.
        """
        self.db.drop_collection('products')

    def test_write_data_to_db(self):
        """
        Test inserting a document into MongoDB and verify its presence.
        """
        new_data = {"name": "Test Product", "price": 100}
        self.collection.insert_one(new_data)
        inserted_data = self.collection.find_one({"name": "Test Product"})
        self.assertIsNotNone(inserted_data)
        self.assertEqual(inserted_data['name'], 'Test Product')
