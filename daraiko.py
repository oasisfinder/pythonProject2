from selenium import webdriver
import datetime
import csv

driver = webdriver.Chrome()
url = "http://www.shouei-shouten.com/14537920252370"
driver.get(url)

table = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[4]/div/table")
tbody = table.find_element_by_tag_name("tbody")


rows = tbody.find_elements_by_tag_name("tr")
dlist = []
vlist = []

for i, rows in enumerate(rows):
    if i < 2:
        continue
    date = rows.find_elements_by_tag_name("td")[8]
    value = rows.find_elements_by_tag_name("td")[9]
    datek = date.text.replace("月","/")
    datek = datek.replace("日","")
    dlist.append(datek)
    vlist.append(value.text)


with open('daraiko.csv', 'w',newline='') as f:
    write = csv.writer(f)
    write.writerow(dlist)
    write.writerow(vlist)
f.close()