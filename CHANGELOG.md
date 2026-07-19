# Changelog

All notable changes to the Spintax syntax highlighting package are documented here.
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.1.1 — 2026-07-19

### Fixed

- `.gitattributes` now marks development files `export-ignore`, so the installed
  package contains only what Sublime loads: the syntax, the comment preferences,
  README, CHANGELOG and LICENSE. Tests and CI config previously shipped to users.

## 1.1.0 — 2026-07-19

### Added

- Highlighting for the `#def` directive, shipped in Spintax engine 3.0.0 /
  `@spintax/core` 0.3.0. Same line-anchored shape as `#set`
  (`#def %name% = value`), opposite semantics: `#set` is a macro whose value is
  re-substituted and re-rolled at every reference, while `#def` resolves once per
  render and holds that result everywhere.
- `#def` gets its own scope, `keyword.other.directive.def.spintax`, rather than
  sharing `#set`'s. The directives mean genuinely different things, so a colour
  scheme must be able to tell them apart.

### Fixed

- Directives on their own line inside a multi-line `{ … }` or `[ … ]` are now
  highlighted. The engine extracts `#set`/`#def` from the whole source
  line-by-line, independent of bracket nesting, so such a line really does define
  a variable — it was previously rendered as plain enumeration text. Pre-existing
  for `#set`; fixed for both.

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
