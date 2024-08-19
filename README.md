# Read3D-Interface
## 環境配置
### 安裝所需依賴
進入 real3dportrait 環境後，安裝 requirements.txt 中的套件
```bash
conda activate /mnt/Nami/users/Jason0411202/anaconda3/envs/real3dportrait
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
