# Changelog

All notable changes to the Spintax syntax highlighting package are documented here.
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Changed

- Tests are now Sublime Text syntax test files (`tests/syntax_test_spintax.spintax`) run by the
  official [`SublimeText/syntax-test-action`](https://github.com/SublimeText/syntax-test-action),
  replacing the previous Python validation script. CI exercises the grammar on Sublime Text
  `latest`, `stable`, and an ST3 build, confirming ST3092+ compatibility.

## 1.0.0 — 2026-07-08

First release. Engine-accurate highlighting for the full spintax surface, matching the
[`@spintax/core`](https://www.npmjs.com/package/@spintax/core) contract.

### Added

- Enumerations `{a|b|c}`, permutations `[<config>a|b]`, variables `%name%`,
  `#set` / `#include` directives, comments `/# … #/`.
- **Conditionals** `{?VAR?then|else}` / `{?!VAR?…}` — strict opener (ASCII identifier +
  mandatory `?`), so `{??x}` / `{?1bad?x}` are not mistaken for conditionals.
- **Plurals** `{plural N: form|…}` — requires the `{plural ` prefix and a mandatory `:`,
  so `{plural noun}` / `{plural: x}` are not mistaken for plurals.
- **Engine-accurate permutation separators**: leading `<config>` is recognised only as a
  known-key block or a single-separator, and HTML (`[<li>a</li>|b]`, `[<a href="/x">…</a>|b]`)
  is left as content. Leading `<and>` (no matching close tag) and per-element trailing
  separators (`[a<, >|b]`, `[a<and>|b]`) are highlighted as separators — mirroring the engine's
  `looksLikeHtmlStartTag` / `extractTrailingSep` asymmetry.
- Block-comment toggle (`/# … #/`) via `Comments.tmPreferences`.
