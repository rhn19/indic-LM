# indic-LM
State-Of-The-Art Language Models for Indian Languages

## Marathi
#### Datasets
- [IndicNLP mr Corpus](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/data/monolingual/indicnlp_v1/sentence/mr.txt.gz)
- [IndicNLP News Classification](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/evaluations/classification/indicnlp-news-articles.tgz)
- [iNLTK Headlines Classification (cleaned)](https://www.kaggle.com/rhn1903/marathi-news-dataset-cleaned)

Trained using IndicNLP-mr corpus (10% held out for evaluation)</br>
For generating the same splits :
```python
>>>from sklearn.model_selection import train_test_split
#lines (List(str)) - List of lines read from the corpus
>>>train, test = train_test_split(lines, shuffle=True, test_size=0.1, random_state=19)
```
#### Models

| Model Architecture | Perplexity | iNLTK Headlines (cleaned) | IndicNLP News | PyTorch model | Tensorboard Logs |
| :----------------: | :--------: | :-----------------------: | :-----------: | :-----------: | :--------------: |
|                    |            |<i>Accuracy/ Kappa</i>|<i>Accuracy/ Kappa</i>|               |                  |
| ALBERT-base-v2-550K | 37.06 | 0.94/ 0.89 | 0.96/ 0.93 | [Checkpoint](https://drive.google.com/drive/folders/103WoVxmQ_dZ2SHViEfQE23Ojlg5lvZvj?usp=sharing) | [Logs](https://tensorboard.dev/experiment/qLz6zcKoTQesQQAO33L9SA/) |


#### Tokenizers
Trained on the entire IndicNLP-mr Corpus

- <h5>SentencePiece</h5>
[Download](https://drive.google.com/drive/folders/1EhXX_ueS4VqZFkgJUq42tYO1BMzoNwZq?usp=sharing)</br>
File format : mr_ {character_coverage}_ {model_type}_ {vocab_size}_ spiece</br>
Added Tokens : [CLS], [SEP], [MASK]

- <h5>WordPiece</h5>
[Download](https://drive.google.com/drive/folders/1rW7brNHgECb8VViAtCZLwrrILtXk3UoT?usp=sharing)</br>
File format : mr_ {min_frequency}_ wordpiece_ {vocab_size}</br>
Added Tokens : [PAD], [UNK], [CLS], [SEP], [MASK]

- <h5>ByteLevelBPE</h5>
[Download](https://drive.google.com/drive/folders/10pAzvjBgOROYZKvf6dPpOqgE94rNG_bZ?usp=sharing)</br>
File format : mr_ {min_frequency}_ bpe_ {vocab_size}</br>
Added Tokens : &lt;s&gt;, &lt;pad&gt;, &lt;/s&gt;, &lt;unk&gt;, &lt;mask&gt;
