from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="C:\\Users\\NLSDE\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get("http://www.baidu.com")
data = driver.title
print(data)
