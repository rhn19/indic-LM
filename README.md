# indic-LM
State-Of-The-Art Language Models for Indian Languages

## Models
<table style="width:100%">
  <tr>
    <th>Language</th>
    <th>Model Architecture</th>
    <th>Perplexity</th>
    <th>IndicNLP News (Accuracy/ Kappa)</th>
    <th>Public Classification Datasets (Accuracy/Kappa)</th>
    <th>PyTorch model</th>
    <th>Tensorboard Logs</th>
  </tr>
  <tr>
    <td rowspan="2" align="center" valign="center">Marathi (mr)</td>
    <td align="center" valign="center">ALBERT-base-v2-550K</td>
    <td align="center" valign="center">37.06</td>
    <td align="center" valign="center">0.96/ 0.93</td>
    <td align="center" valign="center">iNLTK Headlines<br>0.94/ 0.89</td>
    <td align="center" valign="center"><a href="https://drive.google.com/drive/folders/1KBJfA5ffsHbar4pIfVKGWLThOD_NHmuz?usp=sharing">Checkpoint</a></td>
    <td align="center" valign="center"><a href="https://tensorboard.dev/experiment/qLz6zcKoTQesQQAO33L9SA/">Logs</a></td>
  </tr>
  <tr>
    <td align="center" valign="center">BERT-base</td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
  </tr>
  
  <tr>
    <td rowspan="2" align="center" valign="center">Hindi (hi)</td>
    <td align="center" valign="center">ALBERT-base-v2</td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
  </tr>
  <tr>
    <td align="center" valign="center">BERT-base</td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
    <td align="center" valign="center"></td>
  </tr>
</table>

## Tokenizers
Trained on the IndicNLP Corpus (Max Samples=10M)

[Download](https://drive.google.com/drive/folders/1pMS4Y1mwCo4VZXzoEjq0_9VfXaexqfL7?usp=sharing)<br>
Contains Tokenizers for the following languages : Marathi, Hindi, Punjabi, Bengali, Oria, Gujurati, Kannada, Telegu, Malayalam, Tamil

**SentencePiece**<br>
File format : {lang}_ {character_coverage}_ {model_type}_ {vocab_size}_ spiece</br>
Added Tokens : [CLS], [SEP], [MASK]

**WordPiece**<br>
File format : {lang}_ {min_frequency}_ wordpiece_ {vocab_size}</br>
Added Tokens : [PAD], [UNK], [CLS], [SEP], [MASK]

**ByteLevelBPE**<br>
File format : {lang}_ {min_frequency}_ bpe_ {vocab_size}</br>
Added Tokens : &lt;s&gt;, &lt;pad&gt;, &lt;/s&gt;, &lt;unk&gt;, &lt;mask&gt;

## Datasets
LMs trained using IndicNLP corpus (10% held out for evaluation)</br>
For generating the same splits :
```python
>>>from sklearn.model_selection import train_test_split
#lines (List(str)) - List of lines read from the corpus
>>>train, test = train_test_split(lines, shuffle=True, test_size=0.1, random_state=19)
```

Links -
- [IndicNLP Corpus](https://github.com/ai4bharat-indicnlp/indicnlp_corpus)
- [IndicNLP News Classification](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/evaluations/classification/indicnlp-news-articles.tgz)
- [iNLTK Marathi Headlines Classification (cleaned)](https://www.kaggle.com/rhn1903/marathi-news-dataset-cleaned)
