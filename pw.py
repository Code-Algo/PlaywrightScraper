from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://finance.yahoo.com/u/yahoo-finance/watchlists/most-active-penny-stocks/')
    page.click('a[href="/quote/BBD"]')
    html = page.inner_html('#quote-summary')
    print(html)