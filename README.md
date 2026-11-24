# Fortune in a Pot

[![Bounty](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/cervus-snoopy/quiet-window-confidant-q7w2/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/cervus-snoopy/quiet-window-confidant-q7w2/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)

A tiny Python program that writes one kind, funny fortune for the houseplant in the window to `entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

The program reads `MAKEFUN_OUTPUT_DIR` (default `/output`), validates the
fortune — one line, 1–120 characters, valid UTF-8, not only whitespace —
writes it to `entry.txt` with no trailing newline and mode `0644`, then
reads the file back to verify it byte-for-byte.

## Verify

```sh
REPO=/path/to/quiet-window-confidant-q7w2   # checkout of this repository
cd /tmp
rm -rf /tmp/out-a /tmp/out-b
MAKEFUN_OUTPUT_DIR=/tmp/out-a python3 "$REPO/main.py"
MAKEFUN_OUTPUT_DIR=/tmp/out-b python3 "$REPO/main.py"
sha256sum /tmp/out-a/entry.txt /tmp/out-b/entry.txt
python3 -c "print(len(open('/tmp/out-a/entry.txt', encoding='utf-8').read()))"
```

Both runs must exit 0 and produce byte-identical `entry.txt` files.

## License

MIT — see [LICENSE](LICENSE).
