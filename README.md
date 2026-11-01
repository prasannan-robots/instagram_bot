# instagram_bot

Scheduled [InstaPy](https://github.com/InstaPy/InstaPy) session that likes posts from your feed
and a handful of hashtags, with InstaPy's quota supervisor to stay under daily limits.

> **Status:** InstaPy has been unmaintained since 2020 and often fails against today's
> Instagram (login flow and page layout changes). For a working approach see
> [Wamala](https://github.com/prasannan-robots/Wamala), which uses the private-API client
> `aiograpi`.

## Setup

1. Python 3.8–3.10 (InstaPy's dependencies don't support newer versions), Firefox and
   [geckodriver](https://github.com/mozilla/geckodriver/releases) on your `PATH`.
2. `pip install -r requirements.txt`
3. Set `INSTA_USERNAME` and `INSTA_PASSWORD` (and optionally `MAIL_ADDRESS`, `MAIL_PASSWORD`,
   `MAIL_TO` for a login email). Don't put credentials in the code.
4. `python bot.py` (runs at 12:35, 17:30 and 20:25 daily) or `python simple_bot.py` (once).

Automated activity can get an account rate-limited or banned — use your own account and keep
the limits low.
