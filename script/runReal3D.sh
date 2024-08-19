source /mnt/Nami/users/Jason0411202/anaconda3/bin/activate /mnt/Nami/users/Jason0411202/anaconda3/envs/real3dportrait
echo "Current Conda environment: $(conda info --envs | grep '*' | awk '{print $1}')"

# 取得傳入的參數
param1=$1
param2=$2
param3=$3

# 使用參數
echo "Parameter 1: $param1"
echo "Parameter 2: $param2"
echo "Parameter 3: $param3"

cd ../Real3DPortrait

python_command="python ../Real3DPortrait/inference/real3d_infer.py --src_img \"$param1\" --drv_aud \"$param2\" --drv_pose \"Inputs/drv_pose/default.mp4\" --out_name \"$param3\" --out_mode \"final\""
echo "Executing command: $python_command"

# 執行 python 指令
eval $python_command