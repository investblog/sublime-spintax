# Spintax — Sublime Text syntax highlighting

[![CI](https://github.com/investblog/sublime-spintax/actions/workflows/ci.yml/badge.svg)](https://github.com/investblog/sublime-spintax/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

Syntax highlighting for [**spintax**](https://spintax.net) templates in Sublime Text —
engine-accurate against the [`@spintax/core`](https://www.npmjs.com/package/@spintax/core)
contract. Applies to `.spintax` and `.gtw` files.

| Construct | Example |
| --- | --- |
| Enumeration | `{a\|b\|c}` |
| Permutation | `[<minsize=2;maxsize=3;sep=", ">a\|b\|c]` |
| Variable | `%name%` |
| Local set | `#set %name% = value` |
| Include | `#include "slug-or-id"` |
| Conditional | `{?VAR?then\|else}` · `{?!VAR?…}` |
| Plural | `{plural %n%: one\|few\|many}` |
| Comment | `/# … #/` |

## Example

```spintax
/# hero block #/
#set %product% = Acme
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

The grammar's discriminators are checked in CI:

```sh
python tests/validate_syntax.py
```

The [VS Code sibling](https://github.com/investblog/vscode-spintax) additionally verifies the
mirrored TextMate grammar headlessly (`vscode-tmgrammar-test`) under the real Oniguruma engine.

## Related

- 📖 Syntax reference — <https://spintax.net/docs/syntax>
- 🧪 Live playground — <https://spintax.net/play/>
- 📦 Engine (`@spintax/core`) — <https://www.npmjs.com/package/@spintax/core>
- 🧩 VS Code extension — [investblog/vscode-spintax](https://github.com/investblog/vscode-spintax)

## License

[MIT](./LICENSE) — part of the [301.st](https://301.st) toolset.
