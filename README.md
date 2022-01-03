# To Install and use the Best Buy Bot V 1.1

These instructions are for Mac users only.

---

## Clone this Repo to your machine.

- [BestBuyBot version 1.1](https://github.com/rest2437/BestBuyBot_V1.1.git)
- Open in VScode.

---

## Is Python installed?

### No:

- Please reference the [Python documentation](https://www.python.org/downloads/) for installing Python.

### Yes:

- Move onto the next step.

---

### Install Selenium.

- 1. Open the VScode built in terminal.
- 2. install selenium using "pip3 install selenium" or if you are using an older
     version of python use "pip install selenium".

---

### Download web driver for Chrome. If using Firefox, please see next step

- 1. Find out which version of chrome you are using by typing "chrome://version" in your chrome search bar.
- 2. If you are using Chrome version 97, please download [ChromeDriver 97.0.4692.36](https://chromedriver.storage.googleapis.com/index.html?path=97.0.4692.36/)
- 3. If you are using Chrome version 96, please download [ChromeDriver 96.0.4664.45](https://chromedriver.storage.googleapis.com/index.html?path=96.0.4664.45/)
- 4. If you are using Chrome version 95, please download [ChromeDriver 95.0.4638.69](https://chromedriver.storage.googleapis.com/index.html?path=95.0.4638.69/)
- 5. Once it appears in your downloads folder, extract the zip file and move the "chromedriver" file from the downloads
     folder to the "/usr/local/bin" PATH.

---

### If you are using Firefox

- 1. Download Geckodriver which can be found [here](https://github.com/mozilla/geckodriver/releases)
- 2. Based on your CPU model, the file will either be [geckodriver-v0.30.0-macos-aarch64.tar.gz](https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-macos-aarch64.tar.gz) or [geckodriver-v0.30.0-macos.tar.gz](https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-macos.tar.gz)
- 3. Once it appears in your downloads folder, extract the zip file and move the "geckodriver" file from the downloads
     folder to the "/usr/local/bin" PATH.
- 4. In BestBuyBot_v1.1.py, locate and comment out the CHROME section
- 5. In BestBuyBot_v1.1.py, locate and uncomment the FIREFOX section

---

### Input your personal information for guest sign in and shipping

- 1. In BestBuyBot_v1.1.py, locate the section LOG IN AS GUEST. This is where you will see notes to help assist you in inputting your information that will be used to log you in as a guest user.

---

### Create a free Twilio Account

- 1. [Twilio website](https://www.twilio.com/)
- 2. In BestBuyBot_v1.1.py, locate the section TEXT MESSAGE ALERT OPTION and follow the notes to input your Twilio account credentials.

---

### Test program

- 1. Locate an item on best buys webpage that is in stock and copy the items link.
- 2. In BestBuyBot_v1.1.py, locate the TEST section. In that section you will see "driver.get('PASTE_TEST_LINK_HERE')". please paste the copied link where it says PASTE_TEST_LINK_HERE.
- 3. Uncomment the TEST section.
- 4. Save the file
- 5. Run the scrypt by pressing the play button on the upper right corner of the window if using VScode.
- 6. If everything works fine, comment out the TEST section and uncomment the SCALP section that is preset to scalp for the PS5
- 7. Save the file
- 8. Run the program and watch it work!

---

### Notes

- If you wish to buy a different item on Best Buys Website, you can locate the item and paste the link in.
- If you do not know how to Uncomment or Comment out items, click on the line number and press "command and /"

---

### Stretch Goals

- I want this bot to eventually have a GUI to allow the user to input their information, the website to scalp, CC info, and checkout without having to sourt through code.
