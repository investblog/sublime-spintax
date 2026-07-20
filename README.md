# Spintax — Sublime Text syntax highlighting

[![CI](https://github.com/investblog/sublime-spintax/actions/workflows/ci.yml/badge.svg)](https://github.com/investblog/sublime-spintax/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

Syntax highlighting for [**spintax**](https://spintax.net) templates in Sublime Text —
engine-accurate against the Modern Spintax Engine
([`@spintax/core`](https://www.npmjs.com/package/@spintax/core)) contract.
Applies to `.spintax` files.

- **Enumeration** — `{a|b|c}`, empty option allowed: `{|a|b}`
- **Permutation** — `[a|b|c]`, with config `[<minsize=2;maxsize=3;sep=", ">a|b|c]`
- **Variable** — `%name%`
- **Local set** — `#set %name% = value` — macro, re-rolled at every reference
- **Local def** — `#def %name% = value` — resolved once per render, held everywhere
- **Include** — `#include "slug-or-id"`
- **Conditional** — `{?VAR?then|else}`, `{?!VAR?…}`
- **Plural** — `{plural %n%: one|few|many}`
- **Comment** — `/# … #/`

## Example

```
/# hero block #/
#set %product% = Acme
#def %tone% = {friendly|warm}
{Welcome to|Meet} %product% — %tagline%, trusted since {2019|2020}.
Ships with [<minsize=2;maxsize=3;sep=", ";lastsep=" and ">SSO|audit logs|alerts]{?free? — free tier available|}.
You have %n% {plural %n%: message|messages}.
```

## Install

### Package Control (recommended)

1. Open the Command Palette → **Package Control: Install Package**.
2. Search for **Spintax** and install.

### Manual

Clone or download this repo into your Sublime Text `Packages/` directory
(**Preferences → Browse Packages…**) as a folder named `Spintax`.

## What you get

- Full, engine-accurate tokenization of every spintax construct, including nested spintax
  inside conditional branches and enumerations.
- **Correct permutation config vs HTML:** `<minsize=…;sep=…>` is config, while HTML inside
  items (`[<li>a</li>|b]`, `[<a href="/x">…</a>|b]`) stays content; genuine separators like
  `[<and>a|b]` and per-element `[a<, >|b]` are highlighted.
- Strict conditional / plural openers — `{??x}` and `{plural noun}` are *not* mis-highlighted.
- Toggle Comment (<kbd>Ctrl/Cmd</kbd>+<kbd>/</kbd>) wraps selections in `/# … #/`.

## Development

Tokenization is verified with Sublime Text's own syntax test runner. The assertions live in
[`tests/syntax_test_spintax.spintax`](./tests/syntax_test_spintax.spintax) and cover every
construct plus the tricky discriminators (permutation config vs. HTML, leading/trailing
separators, strict conditional/plural openers). CI runs them against Sublime Text `latest`,
`stable`, and an ST3 build via [`SublimeText/syntax-test-action`](https://github.com/SublimeText/syntax-test-action).

Run them locally from Sublime Text with **Build With: Syntax Tests** (<kbd>Ctrl/Cmd</kbd>+<kbd>B</kbd>)
while the test file is open.

Releases are published from tags: tag a commit `X.Y.Z` and push it, and the release workflow
creates the GitHub Release using the matching `## X.Y.Z` section of
[`CHANGELOG.md`](./CHANGELOG.md) as its notes — so that section has to exist first. Package
Control installs from tags, so a tag is the release; the GitHub Release entry is the shop window.

The [VS Code sibling](https://github.com/investblog/vscode-spintax) additionally verifies the
mirrored TextMate grammar headlessly (`vscode-tmgrammar-test`) under the real Oniguruma engine.

## Related

- 📖 Syntax reference — <https://spintax.net/docs/syntax>
- 🧪 Live playground — <https://spintax.net/play/>
- 📦 Engine (`@spintax/core`) — <https://www.npmjs.com/package/@spintax/core>
- 🧩 VS Code extension — [investblog/vscode-spintax](https://github.com/investblog/vscode-spintax)

## License

[MIT](./LICENSE) — part of the [301.st](https://301.st) toolset.
