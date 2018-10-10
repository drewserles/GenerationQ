python test.py \
-model trained/lowest_ppl_model.pt \
-src data/src-test.txt \
-output pred.txt \
-replace_unk \
-verbose \
-beam_size 3 \
-gpu 0 \
-batch_size 30
