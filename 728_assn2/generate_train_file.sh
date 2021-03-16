output_file_path=/Users/amankansal/Desktop/data/728_assn2/train.csv
mkdir -p $(dirname $output_file_path)
python3 generate_train_file.py \
    --input_file_path /Users/amankansal/Desktop/datasets/ncc/labeled.csv\
    --output_file_path $output_file_path \
    --test_ratio 0.15