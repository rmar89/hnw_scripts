import json
import time
from selenium import webdriver

browser = None

def init():
  global browser
  browser = webdriver.Firefox()
  browser.get('https://purewellness.linkedinfitness.com/dt/v2/linkedinindex.asp')

# login
def login(user="rmar@linkedin.com", pw="selenium"):
  browser.find_element_by_id('userbox').send_keys(user)
  browser.find_element_by_id('passbox').send_keys(pw)
  browser.find_element_by_class_name('loginText').submit()

# navigate to daily activities
def gotoActivities():
  browser.find_element_by_partial_link_text('Incentives').click()
  browser.find_element_by_partial_link_text('Healthy Habits').click()

# open the datepicker
def setStartDate(day=16, month='Feb', year=2014):
  browser.find_element_by_class_name('ui-datepicker-trigger').click()
  month_element = browser.find_element_by_class_name('ui-datepicker-month')
  for option in month_element.find_elements_by_tag_name('option'):
    if option.text == month:
      option.click()
      break
  day_elements = browser.find_elements_by_class_name('ui-state-default')
  for d in day_elements:
    if d.text == str(day):
      d.click()
      break

# month needs to be all caps
def isEndDate(day=20, month='MAR', year=2014):
  partialDateString = "%s %d, %d" % (month, day, year)
  return partialDateString in browser.find_element_by_class_name('dtDateText').text

# tick the checkboxes and score some points
def submitHabits():
    browser.find_element_by_id('verifyBox559').click() # stairs
    browser.find_element_by_id('verifyBox560').click() # mental break
    browser.find_element_by_id('verifyBox561').click() # eating healthy
    browser.find_element_by_id('HHSubmitBut').click()

# returns true if going to the next day is successful
def incrementDay():
  dateHeader = browser.find_element_by_class_name('dtColoumHeaderFont')
  dateNudgers = dateHeader.find_elements_by_tag_name('a')
  if (len(dateNudgers) == 2):
    dateNudgers[1].click()
    return True
  return False

def runRange():
  while not isEndDate():
    submitHabits()
    if not incrementDay():
      return
  submitHabits()

# time.sleep(5)

# browser.get('https://www.linkedin.com/pulse-fe/follows')

# x = json.loads(browser.find_element_by_tag_name('body').text)

# print repr(x)

# for ix, i in enumerate(x['follows']):
# print "%s %s %s" % (ix+1, i['url'], i['urn'])

# browser.close()

def main():
  init()
  login() #todo: take script args for login
  gotoActivities()
  setStartDate() #todo: take args for specifying start date
  runRange()

if __name__ == "__main__":
    main()

