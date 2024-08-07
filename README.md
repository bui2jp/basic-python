# basic-python (2024)

## vscode の設定

### 前提

wsl ubuntu or Mac で作業
python のインストールは pyenv
python の仮想環境について

### pyenv

```
$ pyenv version
3.10.14 (set by /home/user01/.pyenv/version)

$ python --version
Python 3.10.14


# インストール可能な一覧
$ pyenv install --list
:
3.11.9
:

# インストール *最新
$ pyenv install 3.11.9

# インストール済みの確認
$ pyenv versions
  system
* 3.10.14 (set by /home/user01/.pyenv/version)
  3.11.9

# バージョンの切り替え
pyenv global 3.11.9
pyenv local 3.11.9

$ python --version
Python 3.11.9
```

### 対話型シェルの利用例

```
$ python
Python 3.11.9 (main, Aug  6 2024, 15:43:59) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> message='hi, this is python.'
>>> print(message)
hi, this is python.
>>> exit()
```

# Mac /w anaconda
Anaconda3 2024.06-1をインストール
