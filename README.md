# Slimetime

Proof of concept - build the simplest possible python GUI executable. Support Windows and Mac. Automated builds via github actions.

Key libraries:

- [Gooey](https://pypi.org/project/Gooey/)
- [pyinstaller](http://www.pyinstaller.org/)

What is `slimetime`? A 2000s Nickelodeon [show](https://en.wikipedia.org/wiki/Slime_Time_Live); inspired by the Gooey name.

## Setup instructions

```python
# py38 or higher
python3 -m venv venv --prompt=slimetime

source venv/bin/activate
pip install -U pip
pip install -r requirements_dev.txt
```

To build (mac or windows):

```bash
make build
```

### Extras

To convert the PNG image to an ICO:

```python
from PIL import Image
Image.open("green-slime.png").save('green-slime.ico')
```

<div>green-slime.png icon made by <a href="https://www.flaticon.com/authors/good-ware" title="Good Ware">Good Ware</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
