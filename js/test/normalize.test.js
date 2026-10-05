'use strict';
const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');
const { normalize } = require('..');

const vectors = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '..', 'vectors', 'normalize.json'), 'utf8'));

test('shared vectors', () => {
  assert.ok(vectors.normalize.length >= 75);
  for (const c of vectors.normalize) assert.strictEqual(normalize(c.in), c.out, c.in);
});

test('examples', () => {
  assert.strictEqual(normalize('مُذَكِّرَةُ'), 'مذكره');
  assert.strictEqual(normalize('الإجابة'), 'الاجابه');
  assert.strictEqual(normalize('مستشفى'), 'مستشفي');
  assert.strictEqual(normalize('كتـــاب'), 'كتاب');
  assert.strictEqual(normalize(null), '');
  assert.strictEqual(normalize('للمذكرة'), 'للمذكره');
});

test('ESM entry exports the same function', async () => {
  const esm = await import('../index.mjs');
  assert.strictEqual(esm.normalize('أحمد'), 'احمد');
  assert.strictEqual(esm.default.normalize, normalize);
});
