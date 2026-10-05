"""arabic_search_lite: normalize Arabic text for search (free, MIT).

Removes diacritics and tatweel, unifies alef, yaa, taa marbuta and waw-hamza forms, and lowercases.
Same rules, same output as ``normalize`` in the full Arabic Search library (https://dovmem.com/arabic-search).
Standard library only. No I/O, no network.
"""

__version__ = '1.0.0'
__all__ = ['normalize', '__version__']

# Diacritics U+064B..U+065F, superscript alef U+0670, tatweel U+0640: removed.
# Arabic-Indic digits (U+0660..U+0669) are kept.
_MARKS = {c: None for c in list(range(0x064B, 0x0660)) + [0x0670, 0x0640]}
# أ إ آ ٱ -> ا · ى ئ -> ي · ة -> ه · ؤ -> و
_FOLD = {0x0623: 'ا', 0x0625: 'ا', 0x0622: 'ا', 0x0671: 'ا',
         0x0649: 'ي', 0x0626: 'ي', 0x0629: 'ه', 0x0624: 'و'}
_TABLE = {**_MARKS, **_FOLD}


def normalize(text: str) -> str:
    """Return ``text`` ready for comparison or indexing.

    >>> normalize('مُذَكِّرَةُ الإجابة')
    'مذكره الاجابه'
    """
    s = (text or '').translate(_TABLE)
    # str.lower() turns a final capital sigma into ς; lowering one character at a time keeps σ,
    # which matches the Swift and JavaScript versions.
    return ''.join(c.lower() for c in s) if 'Σ' in s else s.lower()
