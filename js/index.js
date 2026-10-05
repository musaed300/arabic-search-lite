'use strict';
// arabic-search-lite: normalize Arabic text for search (free, MIT).
// Same rules, same output as normalize() in the full Arabic Search library: https://dovmem.com/arabic-search

// Diacritics U+064B..U+065F, superscript alef U+0670, tatweel U+0640: removed. Arabic-Indic digits are kept.
const MARKS = /[ً-ٰٟـ]/g;
// أ إ آ ٱ -> ا · ى ئ -> ي · ة -> ه · ؤ -> و
const FOLD = { 'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا',
  'ى': 'ي', 'ئ': 'ي', 'ة': 'ه', 'ؤ': 'و' };
const FOLD_RE = /[أإآٱىئةؤ]/g;

function normalize(text) {
  const s = String(text == null ? '' : text).replace(MARKS, '').replace(FOLD_RE, (c) => FOLD[c]);
  if (!s.includes('Σ')) return s.toLowerCase();
  // toLowerCase() turns a final capital sigma into ς; lowering one character at a time keeps σ (same as Python and Swift).
  let out = '';
  for (const c of s) out += c.toLowerCase();
  return out;
}

module.exports = { normalize, version: '1.0.0' };
