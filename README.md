# Read3D-Interface
## 環境配置
### 安裝所需依賴
```bash
conda create -n Read3D-Interface python=3.11
conda activate Read3D-Interface
pip install -r requirements.txt
```

### 配置環境變數
在本專案根目錄下建立 `.env` 檔案，並填入以下內容
```
SRC_IMG_DIR=<不同情緒圖片的存放目錄>
JSON_FILE_PATH=<紀錄音檔與情緒等的 JSON 檔案之目錄>
```

## 執行
```bash
python main.py
```
