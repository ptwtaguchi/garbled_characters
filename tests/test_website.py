import pytest
import asyncio
import sys
import os

# srcディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from take_screenshot import take_screenshot
from azure_ocr import ocr_image, check_for_garbled_text

@pytest.mark.asyncio
async def test_website_for_garbled_text():
    await take_screenshot('https://qiita.com/KTakahiro1729/items/88f1da528b42f2740d14', 'screenshots/screenshot.png')
    ocr_result = ocr_image('screenshots/screenshot.png')
    assert check_for_garbled_text(ocr_result) == False, "Garbled text found in the screenshot"
