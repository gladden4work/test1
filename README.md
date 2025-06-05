# test1

This repository contains a random password generator that can be used from the
command line or in the browser.

## Command line usage

Run the `password_generator.py` script and follow the prompts to choose the
password length (6–128) and which character types to include.

```bash
python3 password_generator.py
```

## Web usage

Open `index.html` in your browser to use the web interface. It lets you pick the
length, character types and copy the result to your clipboard. If you prefer to
serve it locally run:

```bash
python3 -m http.server
```

Then visit <http://localhost:8000/index.html> in your browser.
