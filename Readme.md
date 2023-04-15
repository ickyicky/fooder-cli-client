# Fooder cli client
[![](https://github.com/ickyicky/fooder-cli-client/blob/main/doc/diary.png?raw=true)](https://github.com/ickyicky/fooder-cli-client)

# About

_Fooder_ is simple TUI client for [FooderAPI](https://github.com/ickyicky/fooder-api) and basic program for tracking calories from terminal.

# Installation

_Fooder_ is currently maintained on [PyPi](https://pypi.org/) Python Package Index. To install package simpply use:

`python3 -m pip install fooder`

# Usage

With installation of fooder you should have new executable - `fooder`.

```bash
fooder
```

from command line. There are some available options:

```
usage: __main__.py [-h] [--access-token ACCESS_TOKEN] [--refresh-token REFRESH_TOKEN] [--url URL]

options:
  -h, --help            show this help message and exit
  --access-token ACCESS_TOKEN
  --refresh-token REFRESH_TOKEN
  --url URL
```

By default `access_token` is stored in `~/.cache/fooder/.token` and `refresh_token` is stored in `~/.cache/fooder/.refresh_token`.
You can use different locations of those files as well as different URL for the API, which you can self-host for personalized
products database.

[![](https://github.com/ickyicky/fooder-cli-client/blob/main/doc/menu.png?raw=true)](https://github.com/ickyicky/fooder-cli-client)

Whole program is very simple TUI where in each view you can select action from available options, such as switching to diary from
another day, adding meals, adding entries etc. It's just intuitive and since project is in alpha stage I'm not writting whole
usage instruction just yet, before the finalized product is complete.
