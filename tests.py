import unittest

from contenttype import ContentType


class ContentTypeTests(unittest.TestCase):
    EXAMPLES = {
        'text/html; charset=utf-8': {
            'type': 'text',
            'prefix': None,
            'subtype': 'html',
            'suffix': None,
            'parameters': {'charset': 'utf-8'},
            'charset': 'utf-8',
        },
        'text/html': {
            'type': 'text',
            'prefix': None,
            'subtype': 'html',
            'suffix': None,
            'parameters': {},
            'charset': None,
        },
        'application/rss+xml; charset=utf-8': {
            'type': 'application',
            'prefix': None,
            'subtype': 'rss',
            'suffix': 'xml',
            'parameters': {'charset': 'utf-8'},
            'charset': 'utf-8',
        },
        'application/vnd.ms-excel': {
            'type': 'application',
            'prefix': 'vnd',
            'subtype': 'ms-excel',
            'suffix': None,
            'parameters': {},
            'charset': None,
        }
    }

    def test_content_types(self):
        for value, expected in self.EXAMPLES.items():
            result = ContentType.parse(value)

            with self.subTest(i=f'content type: "{value}"'):
                self.assertEqual(result.value, value)
                self.assertEqual(result.type, expected['type'])
                self.assertEqual(result.prefix, expected['prefix'])
                self.assertEqual(result.subtype, expected['subtype'])
                self.assertEqual(result.suffix, expected['suffix'])
                self.assertDictEqual(result.parameters, expected['parameters'])
                self.assertEqual(result.charset, expected['charset'])


if __name__ == '__main__':
    unittest.main()
