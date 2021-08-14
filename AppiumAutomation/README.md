Automation Testing
----------------
We are doing automation for Android and iOS application. So below are the prerequisites. 

### Installation

For iOS:
- [Install Xcode](https://itunes.apple.com/in/app/xcode/id497799835?mt=12)

For Android:
- [Install Android Studio](https://developer.android.com/studio/install.html)

Other Dependencies:
- [Install Homebrew](http://brew.sh/)
- [Install JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html)


Install Node
```sh
$ brew install node
$ brew install npm
```

Install Appium and Appium-client
```sh
$ npm install -g appium
$ npm install wd
```

Install Python
```sh
$ brew install python3
```

Install Python Library which are used by automation script
```sh
$ pip3 install -r requirements.txt
```

How to run locally:

`behave --junit -f json.pretty --outfile results.json`
`./convert_to_cucumber`
`node index.js`
Note: Node should be install on machine and hit `npm install -g cucumber-html-reporter`
