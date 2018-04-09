# qiandao
各种自动签到脚本

安装Chrome
```
$ wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
$ echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
$ sudo apt update
$ sudo apt install google-chrome-stable
```

安装Selenium
```
$ sudo apt install python-pip
$ sudo pip install selenium
```

安装Chrome driver
```
$ wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
$ sudo apt install unzip
$ unzip chromedriver_linux64.zip
$ sudo cp chromedriver /usr/bin/
```

配置cron
```
$ crontab -e
```
```
10 */8 * * * /usr/bin/python $HOME/zhongye_net.py
```