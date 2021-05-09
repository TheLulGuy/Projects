from selenium import webdriver

driver = webdriver.Chrome('/Users/tapasi/Downloads/chromedriver87')
driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_2Ujuu').click()
