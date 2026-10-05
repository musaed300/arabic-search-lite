# arabic-search-lite

Normalize Arabic text for search. Free (MIT), no dependencies, for Python and JavaScript.

توحيد النص العربي للبحث. مجانية (MIT)، بدون أي اعتماديات، لـ Python وJavaScript.

| Before · قبل | After · بعد |
|---|---|
| مُذَكِّرَةُ | مذكره |
| الإجابة | الاجابه |
| مستشفى | مستشفي |
| سؤال | سوال |
| كتـــاب | كتاب |
| أحمد · إحمد · آحمد | احمد |

What it does: removes diacritics (tashkeel) and tatweel, turns أ إ آ ٱ into ا, ى ئ into ي, ة into ه and ؤ into و, and lowercases Latin letters. Arabic-Indic digits (٠١٢٣) stay as they are.

وش تسوي: تشيل التشكيل والتطويل، وتحوّل «أ إ آ ٱ» إلى «ا»، و«ى ئ» إلى «ي»، و«ة» إلى «ه»، و«ؤ» إلى «و»، وتصغّر الحروف اللاتينية. والأرقام الهندية (٠١٢٣) تبقى زي ما هي.

## Install · التثبيت

From the GitHub release (PyPI and npm packages are coming soon):

من إصدار GitHub (حزم PyPI وnpm قريبًا):

```sh
pip install https://github.com/musaed300/arabic-search-lite/releases/download/v1.0.0/arabic_search_lite-1.0.0-py3-none-any.whl
npm install https://github.com/musaed300/arabic-search-lite/releases/download/v1.0.0/arabic-search-lite-1.0.0.tgz
```

Or copy a single file into your project: `python/arabic_search_lite/__init__.py` or `js/index.js`.

أو انسخ ملف واحد لمشروعك: `python/arabic_search_lite/__init__.py` أو `js/index.js`.

## Use · الاستخدام

Python (3.8+):

```python
from arabic_search_lite import normalize

normalize("مُذَكِّرَةُ الإجابة")   # "مذكره الاجابه"
```

JavaScript / TypeScript (Node 14+ and browsers, ESM or CommonJS):

```js
import { normalize } from "arabic-search-lite";   // or: const { normalize } = require("arabic-search-lite")

normalize("مُذَكِّرَةُ الإجابة");   // "مذكره الاجابه"
```

Normalize both sides the same way: the text you store and the text the user searches for.

وحّد الطرفين بنفس الطريقة: النص اللي تحفظه، والكلمة اللي يبحث عنها المستخدم.

```python
rows = [r for r in rows if normalize(query) in normalize(r.text)]
```

## What it does not do · وش ما تسويه

This package only normalizes letters. It does not understand words, so:

- A word behind an attached prefix is a different word: «مذكرة» does not equal «للمذكرة», «بالمذكرة» or «والمذكرة».
- There is no search index. Substring checks and `LIKE '%…%'` scan every row, and they also match inside unrelated words («علم» inside «معلم»).

هذي الحزمة توحّد الحروف بس، وما تفهم الكلمات:

- الكلمة اللي قبلها سابقة ملتصقة تعتبرها كلمة ثانية: «مذكرة» غير «للمذكرة» و«بالمذكرة» و«والمذكرة».
- ما فيها فهرس بحث. البحث بجزء من النص أو `LIKE '%…%'` يمر على كل الصفوف، ويطابق داخل كلمات ما لها علاقة («علم» داخل «معلم»).

## The full version · النسخة الكاملة

[Arabic Search](https://dovmem.com/arabic-search) adds what this package leaves out:

- finds words behind attached prefixes: ال، لل، بال، وال، و، ب، ف، ك، ل
- a ready SQLite FTS5 index and query builder, with a fallback when FTS5 is missing
- result snippets with the matched word highlighted
- the same results in Swift, Python and JavaScript, with an in-memory index for the browser

Try it live on the product page, with any Arabic word: https://dovmem.com/arabic-search#try

Why plain `LIKE` and FTS5 miss Arabic words, with real SQLite results: https://dovmem.com/blog/arabic-search-sqlite

[«بحث عربي ذكي»](https://dovmem.com/arabic-search) يضيف اللي ما في هالحزمة: يلقى الكلمة ورا السوابق الملتصقة، وفيه فهرس SQLite FTS5 جاهز، ومقتطفات تلوّن الكلمة اللي طابقت، وبنفس النتيجة في Swift وPython وJavaScript. جرّبه بأي كلمة عربية في صفحته.

`normalize` here gives exactly the same output as `normalize` in the full library. Both are checked against the same 75 test cases.

`normalize` هنا يطلّع نفس مخرج `normalize` في النسخة الكاملة بالضبط، والاثنين يتفحصون على نفس الـ75 حالة اختبار.

## License · الرخصة

MIT. Made by [dovmem](https://dovmem.com).
