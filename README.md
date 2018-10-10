# Generation Q
A tool to help teachers generate quiz questions about their reading assignments. Try it out here: www.generationq.online

The core question generation model is a Python implementation of the paper [Learning to Ask: Neural Question Generation for Reading Comprehension](https://arxiv.org/abs/1705.00106).

The model is built with the [OpenNMT](http://opennmt.net) framework.

# Create a Model

## Requirements
[OpenNMT](https://github.com/OpenNMT/OpenNMT-py)  
[Spacy and English model](https://spacy.io/usage/)

## Preprocess
<ol>
  <li>Navigate to model folder, GenerationQ / model.</li>
  <li>Run preproc.sh to generate vocabulary and break training corpus up into smaller chunks.</li>
  <li>Download the GloVe 840B.300d pretrained word vectors: https://nlp.stanford.edu/projects/glove/. Extract to model               directory.</li>
  <li>Run emb_to_torch.sh to generate and save embedding files for the vocabulary.</li>
</ol>

## Train

    sh train.sh
Training hyperparamters can be modified by changing the contents of train.sh. With a batch size of 64, 1 epoch is about 1100 training steps.  
Trained models are saved in the "trained" folder. To get the best results in testing, use the iteration that achieve the lowest perplexity.

## Test
Modify the "-model trained/lowest_ppl_model.pt" line in test.sh to point to the trained model with the lowest perplexity.
    
    sh test.sh
Generated questions and their perplexity scores are saved in pred.txt.

## Forward Pass
Run test.sh with the "-src" argument pointing to whatever text file you want to generate questions from. It must be tokenized with one sentence per line.
