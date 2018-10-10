# Generation Q
A tool to help teachers generate quiz questions about their reading assignments. Try it out here: www.generationq.online

The core question generation model is a Python implementation of the paper [Learning to Ask: Neural Question Generation for Reading Comprehension](https://arxiv.org/abs/1705.00106).

The model is built with the [OpenNMT](http://opennmt.net) framework.

# Train a Model

## Preprocess
<ol>
  <li>Run preproc.sh to generate vocabulary and break training corpus up into smaller chunks.</li>
  <li>Download [GloVe](https://nlp.stanford.edu/projects/glove/) pretrained word vectors (840B.300d). Extract to model               directory.</li>
  <li>Run emb_to_torch.sh to generate and save embedding files for the vocabulary.</li>
</ol>
  
