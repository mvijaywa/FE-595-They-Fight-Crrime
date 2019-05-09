
# coding: utf-8

# ### Importing the Libraries

# In[1]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob


# #### Script to download all the files from the discussions folder using Selenium

# In[11]:


chromedriver = 'C:\\chromedriver.exe'
chromeOptions = webdriver.ChromeOptions()

###Specifying the download location for the files
prefs = {"download.default_directory" : "C:/Users/monic/Google Drive/Spring-19/FE-595/All_files"}
chromeOptions.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

browser.get('https://sit.instructure.com/courses/30002/discussion_topics/126409')

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys("Enter username")
password.send_keys("Enter Password")

driver_login=browser.find_element_by_css_selector("button").click()
alt_com=browser.find_elements_by_class_name('comment_attachments')
for i in alt_com:
    i.find_element_by_css_selector("a").click()



# ### Script to merge all the files

# In[12]:


os.chdir("C:/Users/monic/Google Drive/Spring-19/FE-595/All_files")
read_files = glob.glob("*.txt")
read_files.extend(glob.glob("*.csv"))
#print(read_files)
with open("merge.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

