# global_context
Improving Word Meaning Representations using Wikipedia Categories

# Improving Word Meaning Representations using Wikipedia Categories

We extend Skip-Gram and Continuous Bag-of-Words models via global context information. We use Wikipedia corpus where articles are organized in a hierarchy of categories. These categories provide useful topical information about each article. We present several approaches how to enrich word meaning representation with such kind of information.

We experiment with English Wikipedia and evaluate our models on standard word similarity and word analogy datasets. Proposed models significantly outperform other word representation methods when similar size training data are used and provide similar performance compared with methods trained on much larger datasets.

## Getting Started

see our publication at 

## Download corpus

Categories mapping here:
```
https://uloz.to/!jqKCLASD6MmL/categories-filtmin10-prefixed-txt-zip
```
Wikipedia articles: 
```
https://uloz.to/!nZLUURC15rkv/wiki-filteredmin10-txt-zip
```

another format with one sentence per line: 
```
https://uloz.to/tam/_065GP5uM4VOj
```

alternative download: 
```
https://drive.google.com/drive/folders/1uv18K8ZGaLzMuzfgSRQERJqZdsn51o9B?usp=sharing
```

## Models

Trained models can be downloaded at following links: 
CBOW
```
https://uloz.to/!usCgCpNUbMEZ/trained-cbow-vec-zip
```
Skip-gram
```
https://uloz.to/!EJ8rDhVkMKoV/vectors-skip-cat-bin-zip
```

Or here: 
```
https://drive.google.com/drive/folders/1uv18K8ZGaLzMuzfgSRQERJqZdsn51o9B?usp=sharing
```
CZ corpus: 
```
https://drive.google.com/drive/folders/1rraa5-FGW-AfLeU3StVbsjN0YjDbUWe6?usp=sharing
```

## Use with 

Word2Vec, LexVec or fastText tools, clean implementation has to be done.

## Authors

* **Lukáš Svoboda** 
* **Tomáš Brychcín** 

## License

This corpus and models are free for research purposes. 

## Acknowledgments
This work has been partly supported from ERDF "Research and Development of Intelligent Components of Advanced Technologies for the Pilsen Metropolitan Area (InteCom)" (no.: CZ.02.1.01/0.0/0.0/17\_048/0007267) and by Grant No. SGS-2016-018 Data and Software Engineering for Advanced Applications. Computational resources were provided by the CESNET LM2015042 and the CERIT Scientific Cloud LM2015085, provided under the programme "Projects of Large Research, Development, and Innovations Infrastructures".
