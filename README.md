# Egyptian Arabic Wikipedia Scanner: Automatic Detection of Template-translated Articles in the Egyptian Wikipedia

- [Application Description](#application-description)
- [Application Features](#application-features)
- [Application Datasets](#application-datasets)
- [Application Local Run](#application-local-run)
- [Application Citations](#application-citations)


## Application Description:
We release the source code of this web-based detection system, **Egyptian Arabic Wikipedia Scanner**, to automatically identify the template-translated articles on the Egyptian Arabic Wikipedia edition. We publically host this application on Streamlit Community Cloud, here: [https://egyptian-wikipedia-scanner.streamlit.app](https://egyptian-wikipedia-scanner.streamlit.app/), and for better accessibility, we also host it on Hugging Face Spaces, here: [https://huggingface.co/spaces/SaiedAlshahrani/Egyptian-Wikipedia-Scanner](https://huggingface.co/spaces/SaiedAlshahrani/Egyptian-Wikipedia-Scanner).

This web-based application is introduced in a research paper titled "[***Leveraging Corpus Metadata to Detect Template-based Translation: An Exploratory Case Study of the Egyptian Arabic Wikipedia Edition***](https://arxiv.org/abs/2404.00565)", which is **accepted** at [LREC-COLING 2024](https://lrec-coling-2024.org/): [The 6th Workshop on Open-Source Arabic Corpora and Processing Tools (OSACT6)](https://osact-lrec.github.io/), and is currently released under an MIT license.

## Application Features:
This web-based application, **Egyptian Wikipedia Scanner**, allows users to search for an article directly or select a suggested article retrieved using fuzzy search from the Egyptian Arabic Wikipedia edition. The application automatically fetches the article’s metadata (using the Wikimedia [XTools API](https://www.mediawiki.org/wiki/XTools)), displays the fetched metadata in a table, and automatically classifies the article as `human-generated` or `template-translated`. The application also dynamically displays the full summary of the article and provides the URL to the article to read the full text, as shown in the screenshots below.

<details><summary>Screenshot-1</summary><p align="center"><img src="https://github.com/SaiedAlshahrani/Egyptian-Wikipedia-Scanner/blob/main/Screenshot-1.png?raw=true"></p></details>

<details><summary>Screenshot-2</summary>![](https://github.com/SaiedAlshahrani/Egyptian-Wikipedia-Scanner/blob/main/Screenshot-2.png?raw=true)</details>

## Application Datasets:
We also release the heuristically filtered, manually processed, and automatically classified Egyptian Arabic Wikipedia articles dataset (balanced subset) that has been used to train and test this web-based application, **Egyptian Arabic Wikipedia Scanner**, on Hugging Face Hub, here: [https://huggingface.co/datasets/SaiedAlshahrani/Detect-Egyptian-Wikipedia-Articles](https://huggingface.co/datasets/SaiedAlshahrani/Detect-Egyptian-Wikipedia-Articles), and is also currently released under an MIT license.

## Application Local Run:
This web-based application is publicly hosted online on Streamlit Community Cloud and Hugging Face Spaces, yet if you desire to run the application locally on your machine, follow these steps.

1- Clone the application's GitHub repository to your machine. Use this command in your terminal:

```bash
git clone https://github.com/SaiedAlshahrani/Egyptian-Wikipedia-Scanner.git
cd Egyptian-Wikipedia-Scanner 
```

2- Download the required Python packages. Use this command in your terminal:

```bash
pip install -r requirements.txt
```

3- Run Streamlit local server. Use this command in your terminal:

```bash
streamlit run scanner.py
```

## Application Citations: 
Saied Alshahrani, Hesham Haroon, Ali Elfilali, Mariama Njie, and Jeanna Matthews. 2024. [Leveraging Corpus Metadata to Detect Template-based Translation: An Exploratory Case Study of the Egyptian Arabic Wikipedia Edition](https://arxiv.org/abs/2404.00565). *arXiv preprint arXiv:2404.00565*.

```
@article{alshahrani2024leveraging,
      title={Leveraging Corpus Metadata to Detect Template-based Translation: An Exploratory Case Study of the Egyptian Arabic Wikipedia Edition}, 
      author={Saied Alshahrani and Hesham Haroon and Ali Elfilali and Mariama Njie and Jeanna Matthews},
      year={2024},
      eprint={2404.00565},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
      journal={arXiv preprint arXiv:2404.00565},
      url={https://arxiv.org/abs/2404.00565}
}
```
```
