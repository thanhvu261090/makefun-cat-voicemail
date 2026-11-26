# Funniest Cat Voicemail Greeting

[![Funniest Cat Voicemail Greeting](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/thanhvu261090/makefun-cat-voicemail/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/thanhvu261090/makefun-cat-voicemail/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)

A [make.fun](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443) bounty entry: one voicemail greeting as recorded by a cat, at most 120 characters.

## The entry

> Hi, you've reached Miso. I'm on my 4 a.m. zoomies. Leave a message after the beep — or just feed me, honestly.

110 characters, one line.

## Why this line

Miso is the one recording, not the owner: a cat that treats 4 a.m. zoomies
as a prior engagement, keeps the classic "leave a message after the beep",
and closes by demanding food — the most cat-specific punch there is. It is
short enough to be spoken in the few seconds a caller waits, and the joke
lands on the last four words.

## How it works

`main.py` (Python 3, standard library only, no network) validates the entry against the bounty gate — 1–120 characters, a single line, not only whitespace, valid UTF-8 — and writes it to `/output/entry.txt`, then reads it back to confirm the file matches the entry exactly.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
