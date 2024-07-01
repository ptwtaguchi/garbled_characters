from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import re
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# Azureのキーとエンドポイント
subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY")
endpoint = os.getenv("AZURE_ENDPOINT")

# Computer Visionクライアントのセットアップ
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def ocr_image(file_path):
    with open(file_path, "rb") as image_stream:
        ocr_result = computervision_client.recognize_printed_text_in_stream(image_stream)
    return ocr_result

def is_valid_text(text):
    """
    文字化けを検出するロジックを実装します。
    日本語の範囲および半角英数字が含まれるかどうかをチェックします。
    """
    valid_char_pattern = re.compile(r'^[\u0020-\u007E\u3000-\u30FF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]+$')
    
    # 文字が有効な範囲に含まれているかを確認
    return bool(valid_char_pattern.match(text))

def check_for_garbled_text(ocr_result):
    """
    OCRの結果から文字化けを検出します。
    文字化けが見つかった場合にはその文字を表示し、Trueを返します。
    文字化けがない場合はFalseを返します。
    """
    garbled_found = False
    for region in ocr_result.regions:
        for line in region.lines:
            for word in line.words:
                text = word.text
                if not is_valid_text(text):
                    print(f"Garbled text found: {text}")
                    garbled_found = True
    return garbled_found

# 例: OCRの実行と文字化けチェック
if __name__ == "__main__":
    ocr_result = ocr_image("screenshots/screenshot.png")
    if check_for_garbled_text(ocr_result):
        print("Garbled text found in the screenshot")
    else:
        print("No garbled text found in the screenshot")
