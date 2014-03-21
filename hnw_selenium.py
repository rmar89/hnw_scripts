import json
import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://purewellness.linkedinfitness.com/dt/v2/linkedinindex.asp')

# login
browser.find_element_by_id('userbox').send_keys("rmar@linkedin.com")
browser.find_element_by_id('passbox').send_keys("selenium")
browser.find_element_by_class_name('loginText').submit()

# navigate to daily activities
browser.find_element_by_partial_link_text('Incentives').click()

# time.sleep(5)

# browser.get('https://www.linkedin.com/pulse-fe/follows')

# x = json.loads(browser.find_element_by_tag_name('body').text)

# print repr(x)

# for ix, i in enumerate(x['follows']):
# print "%s %s %s" % (ix+1, i['url'], i['urn'])

# browser.close()

