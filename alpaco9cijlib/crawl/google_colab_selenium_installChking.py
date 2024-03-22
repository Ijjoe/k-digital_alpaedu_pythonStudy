def google_colab_selenium_installChking():
    pip_list = !pip list | grep 'google-colab-selenium '

    if len(pip_list) == 1:
        !pip list | grep 'google-colab-selenium'
        print("이미 설치 되어있음 ")
    else:
        import sys
        sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
        from selenium.webdriver.chrome.options import Options
        import google_colab_selenium as gs

		# setup chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless') # ensure GUI is off
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
       
        driver = gs.Chrome(options=chrome_options)
        driver.get('https://www.google.com/')
        print(driver.title)
        print("구글 타이틀 출력되면 설치 및 get테스트 완료")
        driver.quit()

    return '체킹완료'


