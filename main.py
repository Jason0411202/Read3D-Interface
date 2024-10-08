import json
import subprocess
import sys
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

load_dotenv()

SRC_IMG_DIR=os.getenv("SRC_IMG_DIR")
JSON_FILE_PATH=os.getenv("JSON_FILE_PATH")

def ExecuteReal3dCommend(sentence, emotion, audio_path):
    src_img = SRC_IMG_DIR + "/" + emotion + ".jpg" # sourse img 的路徑
    drv_aud = audio_path # 音檔的路徑，從 JSON 檔案中取得
    out_name = "../Read3D-Interface/output/temp/" + sentence + ".mp4" # 因為 script 已經 cd 至 Read3D 的專案中了，故要從那個位置出發

    command = f"bash script.sh '{src_img}' '{audio_path}' '{out_name}'"

    command = [
        "bash",
        "script/runReal3D.sh",
        src_img,
        drv_aud,
        out_name
    ]

    print(" ".join(command)) # 印出指令
    subprocess.run(command, check=True) # 執行指令

def ConnectVideo(videoPathArr):
    clips = [VideoFileClip(file) for file in videoPathArr] # 讀取所有影片
    final_clip = concatenate_videoclips(clips, method="compose") # 合併影片
    final_clip.write_videofile("output/final.mp4", codec="libx264") # 輸出合併後的影片

if __name__ == "__main__":
    with open(JSON_FILE_PATH, 'r', encoding='utf-8') as file: #  讀取紀錄音檔與情緒等的 JSON 檔案
        data = json.load(file)
    
    videoPathArr = []
    for item in data["content"]:
        sentence = item["sentence"]
        emotion = item["emotion"]
        audio_path = item["audio_file_path"]
        videoPathArr.append("output/temp/" + item["sentence"] + ".mp4") # 將影片路徑加入 videoPathArr 陣列，用來合併影片
        
        ExecuteReal3dCommend(sentence, emotion, audio_path) # 執行 Real3d 的指令
    
    ConnectVideo(videoPathArr) # 連接影片