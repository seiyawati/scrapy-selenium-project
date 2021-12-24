# Selenium Scraping

## System
![system image](https://camo.qiitausercontent.com/58372cbbe2ab2498c9fbe5502cc9e923ef706c7a/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f34333639392f64313562313763322d383132612d363465352d346437362d6261623962653730376565372e706e67)

## 環境構築

### DockerによるChromeとWebDriverのインストール

```
$ docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:3.141.59-xenon
```

### Pythonの仮想環境を構築

```
$ cd [project dir]
```

- 仮想環境作成
```
$ python3 -m venv .venv
```

- 仮想環境に入る
```
$ . .venv/bin/activate
```

- 仮想環境を抜ける
```
$ deactivate
```

### Seleniumのインストール

```
$ pip install selenium
```

## 実行手順

```
python sample.py
```
