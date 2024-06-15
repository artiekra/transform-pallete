# Transform pallete

Takes input images, and changes the colors, so that the image only uses given pallete.

Tries to match the pallete as close as possible

(just used it for one random task, not tested at all lmao)

## Usage

Clone from git, activate virtual env, install requirements:

```bash
git clone https://github.com/artiekra/transform-pallete
cd transform-pallete
py -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the script:

```bash
py main.py image.png pool
```

`pool` is a file, containing a pallete, for example:

```
130 0 127
154 0 0
207 109 228
228 0 1
255 84 178
255 101 101
255 167 209
0 0 234
25 25 115
```
