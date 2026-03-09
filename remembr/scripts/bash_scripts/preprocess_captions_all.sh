
for i in 0;
do

    python scripts/preprocess_captions.py --seq_id $i --seconds_per_caption 3 --captioner_name Llama-3-VILA1.5-8b --model-path Efficient-Large-Model/Llama-3-VILA1.5-8B --out_path data/captions/$i/captions

done




