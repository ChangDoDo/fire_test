import requests

# 目標網址
URL = "https://119.hcfd.gov.tw/DTS/caselist/html"

def test_fetch_fire_cases():
    """測試是否能成功抓取消防局的資料"""
    headers = {"User-Agent": "Mozilla/5.0"}  # 偽裝成瀏覽器
    try:
        response = requests.get(URL, headers=headers)
        response.encoding = "utf-8"

        if response.status_code == 200:
            print("✅ 成功抓取資料！")
            print(response.text[:500])  # 顯示前 500 個字元來驗證內容
        else:
            print(f"❌ 無法存取網站，HTTP 狀態碼: {response.status_code}")
    except Exception as e:
        print(f"⚠️ 錯誤發生: {e}")

if __name__ == "__main__":
    test_fetch_fire_cases()
