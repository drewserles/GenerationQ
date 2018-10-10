python translate.py \
-model data/lowest_ppl_model.pt \
-src fwd-tok.txt \
-output fwd-pred.txt \
-replace_unk \
-verbose \
-beam_size 3 \
-batch_size 30
# -gpu 0 \
