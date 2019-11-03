## Requirements

### Brew install
* crf++
* mecab
* mecab-ipadic
* xz
* cabocha
* wget

xz is needed for mecab-ipadic-meologd installation


### manual install
* mecab-ipadic-neologd
* cabocha-python

```bash
$ brew install crf++
$ brew install mecab mecab-ipadic
```

crf++ is needed for CaboCha


### Installation of mecab dictionary

```bash
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
$ cd mecab-ipadic-neologd
$ ./bin/install-mecab-ipadic-neologd -n -a
```

if you only need standard dictionary

```bash
./bin/install-mecab-ipadic-neologd -n
```

### Installation of cabocha-python

```bash
$ cd {path-to-this-project}
$ source wikiproj/bin/activate
(wikiproj) cd ../
(wikiproj) git clone https://github.com/taku910/cabocha.git cabocha-python
(wikiproj) cd cabocha
$ pip install python/
```

Note
1. git clone taku910/cabocha outside this project.
2. use your venv.
3. back to cloned taku910/cabocha directory
4. install cabocha-python under venv of this project


### Get all Wikipedia data

```bash
$ wget https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2
```
