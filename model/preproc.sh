python preprocess.py \
-train_src data/src-train.txt \
-train_tgt data/tgt-train.txt \
-valid_src data/src-dev.txt \
-valid_tgt data/tgt-dev.txt \
-save_data data/preproc \
-src_vocab_size=45000 \
-tgt_vocab_size=28000 \
-src_seq_length=100

