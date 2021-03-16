out_folder_path=/Users/amankansal/Desktop/code/728_assn1/logs/test_out
mkdir -p $out_folder_path
python3 make_test_files.py \
    --xml_folder_path /Users/amankansal/Desktop/datasets/TPP/TPPCorpora/SemEval/Test/Source\
    --key_folder_path /Users/amankansal/Desktop/datasets/TPP/TPPCorpora/SemEval/Test/Key \
    --out_folder_path $out_folder_path \
    --mode without_key