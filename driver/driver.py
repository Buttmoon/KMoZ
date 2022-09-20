import glob
import os
from  seleniumwire.undetected_chromedriver import webdriver
from appium import webdriver as AppiumWebdriver
from auto import Device
import subprocess
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from driver.colors import bcolors
# from selenium.webdriver.chromium import *
# from selenium.webdriver.common import *
# from selenium.webdriver.chrome import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from user_agents import Agents
from viewport import Viewport
import chromedriver_binary
WEBRTC = os.path.join('extension', 'webrtc_control.zip')
ACTIVE = os.path.join('extension', 'always_active.zip')
FINGERPRINT = os.path.join('extension', 'fingerprint_defender.zip')
TIMEZONE = os.path.join('extension', 'spoof_timezone.zip')
CUSTOM_EXTENSIONS = glob.glob(os.path.join('extension', 'custom_extension', '*.zip')) + \
    glob.glob(os.path.join('extension', 'custom_extension', '*.crx'))
class Driver:
    def __init__(self) -> None:
        pass
    def get_chromium_driver(self, headless:bool=False, proxy = "guooydry-rotate:nu81yobbdo6q@p.webshare.io:80"):
        print(bcolors.OKBLUE + """
╔═╗┌─┐┌─┐┌─┐┬  ┌─┐  ╔═╗┌─┐┌─┐┌─┐┬ ┬┌┐┌┌┬┐┌─┐  ┌─┐┬─┐┌─┐┌─┐┌┬┐┌─┐┬─┐
║ ╦│ ││ ││ ┬│  ├┤   ╠═╣│  │  │ ││ ││││ │ └─┐  │  ├┬┘├┤ ├─┤ │ │ │├┬┘
╚═╝└─┘└─┘└─┘┴─┘└─┘  ╩ ╩└─┘└─┘└─┘└─┘┘└┘ ┴ └─┘  └─┘┴└─└─┘┴ ┴ ┴ └─┘┴└─
        """ + bcolors.ENDC)
        options = webdriver.ChromeOptions()
        options.binary_location = "./binary/Chromium.app/Contents/MacOS/Chromium"
        options.headless = headless
        wire_options = {
            'disable_capture': True,
            # 'ca_cert': './ca.crt',
            # 'ca_cert': './localhost.crt',
            # 'ca_key':'localhost.decrypted.key',
            'verify_ssl': True,  # Verify SSL certificates but beware of errors with self-signed certificates,
           'proxy': {
               'http': f'socks5h://{proxy}',
               'https': f'socks5h://{proxy}',
               'no_proxy': 'localhost,127.0.0.1'
               }
           }
        view_size =  Viewport().get_random_mobile()
        if view_size:
            options.add_argument(f"--app-window-size={view_size.landscapeWidth},{view_size.portraitWidth}")
        options.add_argument("--log-level=3")
        # options.add_experimental_option(
        #     "excludeSwitches", ["enable-automation", "enable-logging"])
        # options.add_experimental_option('useAutomationExtension', False)
        prefs = {"intl.accept_languages": 'en_US,en',
                 "credentials_enable_service": False,
                 "profile.password_manager_enabled": False,
                 "profile.default_content_setting_values.notifications": 2,
                 "download_restrictions": 3}
        options.add_experimental_option("prefs", prefs)
        # options.add_experimental_option('extensionLoadTimeout', 120000)
        agent = Agents().get_random_mobile()
        options.add_argument(f"--user-agent={agent}")
        options.add_argument("--mute-audio")
        # options.add_argument('--no-sandbox')
        # --app-window-size=600,600  --app=http://accounts.google.com
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--app=http://accounts.google.com')
        options.add_argument('--disable-features=UserAgentClientHint')
        # options.add_argument("--disable-web-security")
        webdriver.DesiredCapabilities.CHROME['loggingPrefs'] = {
            'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}

        if not headless:
            options.add_extension(WEBRTC)
            options.add_extension(FINGERPRINT)
            options.add_extension(TIMEZONE)
            options.add_extension(ACTIVE)
            if CUSTOM_EXTENSIONS:
                for extension in CUSTOM_EXTENSIONS:
                    options.add_extension(extension)

        # if auth_required:
        #     create_proxy_folder(proxy, proxy_folder)
        #     options.add_argument(f"--load-extension={proxy_folder}")
        else:
            options.add_argument(f'--proxy-server=socks5h://{proxy}')
        service = Service(executable_path=chromedriver_binary.chromedriver_filename)
        driver = webdriver.Chrome(service=service, options=options, seleniumwire_options=wire_options)
        return driver

    def get_appium_driver(self):
        return Device("emulator-5556")
