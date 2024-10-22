# zhconvPrj

## 用途說明
`convertTool.py` 是一個將指定目錄中的 `.mp4` 檔案名稱從簡體中文轉換為繁體中文的工具。使用此工具可以自動批量處理檔案名稱，適合需要統一檔案命名格式的工作流程。

## Python 虛擬環境的建立

1. 先確認系統已安裝 [Python 3](https://www.python.org/downloads/)。
2. 在專案根目錄下建立虛擬環境：

   ```bash
   python3 -m venv .venv

3. 啟動虛擬環境：

若使用 macOS/Linux：

    source .venv/bin/activate


若使用 Windows：

    .venv\Scripts\activate


4.	安裝所需套件：

    pip install zhconv



使用方式

1.	在 convertTool.py 中，指定要處理的目錄路徑：

    directory_path = "/your/directory/path"


2.	啟動腳本進行檔案名稱的轉換：

    python convertTool.py


3.	執行後，所有目錄中的 .mp4 檔案名稱會從簡體中文轉換為繁體中文，並顯示轉換結果：

已將 example.mp4 轉換為 示例.mp4



其他

•	請確保安裝 Python 版本 3.6 以上。
•	若有任何問題或建議，歡迎提交 issue。

