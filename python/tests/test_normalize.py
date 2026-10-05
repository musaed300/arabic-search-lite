import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))

from arabic_search_lite import normalize  # noqa: E402

VECTORS = os.path.join(HERE, '..', '..', 'vectors', 'normalize.json')
FULL = os.path.join(HERE, '..', '..', '..', 'arabic-search', 'vectors', 'vectors.json')


def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


class NormalizeTests(unittest.TestCase):
    def test_shared_vectors(self):
        cases = load(VECTORS)['normalize']
        self.assertGreaterEqual(len(cases), 75)
        for c in cases:
            self.assertEqual(normalize(c['in']), c['out'], c['in'])

    def test_examples(self):
        self.assertEqual(normalize('مُذَكِّرَةُ'), 'مذكره')
        self.assertEqual(normalize('الإجابة'), 'الاجابه')
        self.assertEqual(normalize('مستشفى'), 'مستشفي')
        self.assertEqual(normalize('سؤال'), 'سوال')
        self.assertEqual(normalize('كتـــاب'), 'كتاب')
        self.assertEqual(normalize('٢٠٢٦'), '٢٠٢٦')
        self.assertEqual(normalize(None), '')

    @unittest.skipUnless(os.path.exists(FULL), 'only inside the dovmem repository')
    def test_vectors_match_the_full_library(self):
        self.assertEqual(load(VECTORS)['normalize'], load(FULL)['normalize'])

    def test_no_prefix_stripping(self):
        # The lite version only normalizes. Finding words behind ال/لل/بال/و/ب is in the full library.
        self.assertEqual(normalize('للمذكرة'), 'للمذكره')


if __name__ == '__main__':
    unittest.main()
