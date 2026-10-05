import unittest
from check_csv import check


class CheckTests(unittest.TestCase):
    def test_valid_quoted_multiline(self):
        self.assertEqual(check('id,name\n1,"A, B"\n2,"C\nD"'), {"valid": True, "rows": 2, "errors": []})

    def test_width_error_does_not_leak_values(self):
        result = check('id,name\n1,PRIVATE,extra')
        self.assertEqual(result['errors'], [{"code": "row_width", "record": 2}])
        self.assertNotIn('PRIVATE', str(result))

    def test_empty_duplicate_malformed(self):
        for text in ['', 'id,id\n1,2', 'id\n"unclosed']:
            with self.subTest(text=text):
                self.assertFalse(check(text)['valid'])
