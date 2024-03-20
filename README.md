# Welcome to NewsDejaVu.github.io

## Overview of Methods 

To create News Déjà Vu we contrastively trained a custom large language model to represent each news article by a 768-dimensional vector (an “embedding”), where articles that are semantically similar are represented by similar embeddings. The similarity of two embeddings is measured using the cosine distance between them. 

We digitized a large number of historical U.S. newspaper articles, covering the period 1850-1989.  Each day, we take a sample of modern news articles and create embeddings of these. We then find the closest article within our corpus of historical news. For both the modern and historical articles we mask the names of people, locations, organizations, and other named entities, so the similarity comparison is not based on these. 

The language model captures similarities in the semantics of how things are described, which may or may not reflect similarities in the underlying events or situations being described. While the historical news articles are drawn from mainstream newswires, they reflect the norms and biases of their time and may be considered offensive or contain inaccurate information.

### Historical Newspaper Articles

We digitized front pages from off-copyright local U.S. newspapers spanning 1920-1989. We recognize layouts using Mask RCNN (He et al., 2017) and OCR the texts using Tesseract. Newspaper articles have complex and irregular layouts that can span multiple columns. We associate the (potentially multiple) headline bounding boxes with the (potentially multiple) article bounding boxes and byline boxes that comprise a single article using a combination of layout information and language understanding. More information about the dataset can be found in Silcock, Arora and Dell (2023). We also use the over 400 million newspaper articles from [American Stories](https://huggingface.co/datasets/dell-research-harvard/AmericanStories) (Dell et al., 2023). 

Local newspapers frequently reprint articles that were made available to them via newswires, such as the Associated Press. This means that our corpus can contain multiple copies of the same article (up to editing differences and OCR errors.) We follow the method in Silcock, D’Amico Wong, Yang and Dell (2023) to deduplicate these. We subset to articles that were printed in more than 5 newspapers, to ensure that we have historical articles that were of national, rather than local, interest, choosing the version of the article with the best OCR quality. 

### Modern Newspaper Articles 

We retrieve modern newspaper articles using the newsapi.org API. We remove social media handles and advertisements and reproduce a truncated portion of the text in our posts, including a link to the full article.

### Masking Named Entities

For both modern and historical content, we mask named entities (people, locations, organisations and miscellaneous) before embedding them. This ensures that the similarity model does not rely on similar names in different newspaper articles. To do this, we trained a custom Named Entity Recognition (NER) model to detect spans of text corresponding to these entity types. Custom training was necessary to achieve good performance with robustness to OCR noise. We finetune a Roberta-Large model (Liu et. al, 2020) at a learning rate of 4.7e-05 with a batch size of 128 for 184 epochs. We then replace all detected entities by "[MASK]". The ability to recognize named entities (Named Entity Recognition) also allows us to create "tags" for some of our posts.

### Finding Similar Stories  

To find historical articles that are semantically similar to modern articles, we learned a metric space, where the cosine distance between article embeddings captures semantic similarity. We contrastively trained a language model so that the embeddings of similar pairs of articles have similar embeddings and different articles do not. 

We created training data using articles from [AllSides.com](https://www.allsides.com/), a news aggregator that collates articles on the same story from multiple news sites. We extract pairs of articles from these groupings and use these as positive pairs in our training data. For negative pairs, we use pairs that have a small cosine distance when evaluated with the untrained model, but do not come from the same story, and do not share the same topic tags, according to All Sides. 

We finetuned the model from Silcock, D’Amico Wong, Yang and Dell (2023), which was trained on similar historical newspaper data, but with the purpose of detecting noisy duplication, rather than semantic similarity.  This model has an S-BERT MPNET backbone (Reimers & Gurevych, 2019; Song et al., 2020). We finetuned for 9 epochs, with a batch size of 32 and a warm-up rate of 0.39.  We use S-BERT’s online contrastive loss (Hadsell et al., 2006) implementation with a margin of 0.5. 

## More Information

News Déjà Vu is a product of Dr. Melissa Dell's research lab at Harvard University. You can find more information about our team at [dell-research-harvard](https://dell-research-harvard.github.io/) or see more of our work on [GitHub](https://github.com/dell-research-harvard).

*More Repos Coming Soon!*

## References 

* Dell, Melissa, Jacob Carlson, Tom Bryan, Emily Silcock, Abhishek Arora, Zejiang Shen, Luca D'Amico-Wong, Quan Le, Pablo Querubin and Leander Heldring (2023) “American Stories: A Large-Scale Structured Text Dataset of Historical U.S. Newspapers”, Conference on Neural Information Processing Systems (NeurIPS). 

* Hadsell, Raia, Sumit Chopra, and Yann LeCun (2006), “Dimensionality reduction by learning an invariant mapping”, Conference on Computer Vision and Pattern Recognition (CVPR).

* He, K., G. Gkioxari, P. Dollar and R. Girshick, (2017) R. Mask R-CNN. Proceedings of the IEEE international Conference on Computer Vision. 

* Liu, Yinhan, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer and Veselin Stoyanov (2020), “RoBERTa: A Robustly Optimized BERT Pretraining Approach”, Noise-Robust De-Duplication at Scale”, International Conference on Learning Representations (ICLR).

* Reimers, Nils and Iryna Gurevych (2019), “Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks”, Empirical Methods in Natural Language Processing (EMNLP). 

* Silcock, Emily, Abhishek Arora and Melissa Dell (2023), “A Massive Scale Semantic Similarity Dataset of Historical English”, Conference on Neural Information Processing Systems (NeurIPS).

* Silcock, Emily, Luca D'Amico Wong, Jinglin Yang and Melissa Dell (2023), “Noise-Robust De-Duplication at Scale”, International Conference on Learning Representations (ICLR).

## Disclaimer
*The language model captures similarities in the semantics of how things are described, which may or may not reflect similarities in the underlying events or situations being described. While the historical news articles are drawn from mainstream news wires, they reflect the norms and biases of their time and may be considered offensive or contain inaccurate information.*
