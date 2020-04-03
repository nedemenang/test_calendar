import json
import os
import unittest
basedir = os.path.abspath(os.path.dirname(__file__))

from app import app, db

TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        # Disable sending emails during unit testing
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def add_interview(self, candidate, interviewer, date, time, duration):
        return self.app.post(
            '/add-interview',
            data=json.dumps(dict(candidate=candidate, interviewer=interviewer, date=date, time=time, duration=duration)),
            content_type='application/json',
            follow_redirects=True
        )

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_valid_interview(self):
        response = self.add_interview("Nnamso", "John", "01/01/2020", "2020-04-03 17:43:33.864691", "10")
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Interview Successfully added', response.data)

    def test_invalid_interview(self):
        response = self.add_interview("Nnamso", "John", "01/01/2020", "2020-04-03 17:43:33.864691", "10")
        response2 = self.add_interview("Nnamso", "John", "01/01/2020", "2020-04-03 17:43:33.864691", "10")
        self.assertEqual(response2.status_code, 400)
        self.assertIn(b'There is a conflicting interview', response2.data)

if __name__ == "__main__":
    unittest.main()
