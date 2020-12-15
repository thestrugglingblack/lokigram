```bazaar
                               .__....._             _.....__,
                                        .": o :':         ;': o :".
                                        `. `-' .'.       .'. `-' .'
                                          `---'             `---'
                            
                                _...----...      ...   ...      ...----..._
                             .-'__..-""'----    `.  `"`  .'    ----'""-..__`-.
                            '.-'   _.--"""'       `-._.-'       '"""--._   `-.`
                            '  .-"'                  :                  `"-.  `
                              '   `.              _.'"'._              .'   `
                                    `.       ,.-'"       "'-.,       .'
                                      `.                           .'
                                        `-._                   _.-'
                                            `"'--...___...--'"`
                                    
                    ██       ██████  ██   ██ ██  ██████  ██████   █████  ███    ███ 
                    ██      ██    ██ ██  ██  ██ ██       ██   ██ ██   ██ ████  ████ 
                    ██      ██    ██ █████   ██ ██   ███ ██████  ███████ ██ ████ ██ 
                    ██      ██    ██ ██  ██  ██ ██    ██ ██   ██ ██   ██ ██  ██  ██ 
                    ███████  ██████  ██   ██ ██  ██████  ██   ██ ██   ██ ██      ██                 
```
# Overview
This project came from the love of my beautiful cat Loki! The world needs to know about him and what better way to do this than to post his cute cat pictures and videos on Instagram. I didn't want to manually upload these media files, so I thought what a better way to do this than to create a script that would do all of the work for me. Unfortunately Instagram, doesn't allow for computers to upload pictures to personal accounts (Booo Instagram! :ghost:) So I had to resort to creative ways.

Instagram removed the "Add Post" button from their website **but** they didn't remove their "Upload Video" button for Instagram videos. The script I created allows for me to use Selenium and Geckodriver to upload videos to Instagram. To tackle uploading pictures on Instagram I resorted to using [Apple Scripts](https://en.wikipedia.org/wiki/AppleScript). I have a blog post on creating an Apple Script through an iOS phone [here]().
![]()

# Requirements
* Python 3.6
* Selenium
* Geckodriver

# Getting Started
1. Install Selenium through [here](https://selenium-python.readthedocs.io/installation.html)
2. Install Geckodriver through Homebrew `brew install geckodriver`
3. Install project dependencies `pip install -r requirements.txt`
4. Setup virtualenv 
   ```
   python -m venv ./venv
   source venv/bin/activate
   ```   
4. Run script `python main.py`

# RoadMap
- [ ] Add pyUnit test
- [ ] Upload script to Azure Functions
