import asyncio
from playwright.async_api import async_playwright

async def take_screenshot(url, path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.screenshot(path=path)
        await browser.close()

# 例: スクリーンショットを取得
if __name__ == "__main__":
    asyncio.run(take_screenshot('https://qiita.com/KTakahiro1729/items/88f1da528b42f2740d14', 'screenshots/screenshot.png'))
