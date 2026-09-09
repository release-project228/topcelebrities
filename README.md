# topcelebrities

Celebrity news and biographies: bloggers, influencers and public figures.

**Website: [https://topcelebrities.ru](https://topcelebrities.ru)**

## What's inside

- `mentions.py` — counts how often given names appear in a text; handy to
  see which celebrity an article is really about.

```bash
cat article.txt | python mentions.py "Taylor Swift" "Elon Musk"
```

Matching is case-insensitive on whole-name phrases.

## Why this repo

`mentions.py` is a small, dependency-free example of the text tooling
topcelebrities could offer around its articles. The full site lives at
[https://topcelebrities.ru](https://topcelebrities.ru).

## License

MIT
