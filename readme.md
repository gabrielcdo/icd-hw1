# Zap House Pricing



## Table of Contents

- [Description](#description)
- [Folder Structure](#folder-structure)
- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [License](#license)

## Description

This project aims to predict house prices in Brazil using data scraped from the Zap real estate website. The project is divided into the following steps:

1. **Web Scraping:** Data is scraped from the Zap real estate website using the `requests` and `BeautifulSoup` libraries.
2. **Data Exploration:** The dataset is explored and visualizations are created to gain a better understanding of the data.
3. **Data Preprocessing:** The data is preprocessed and prepared for training.
4. **Modeling:** Regression and classification models are trained and validated using the prepared data.

## Folder Structure

The project folder is structured as follows:

```
- /data: Contains the raw_data and processed_data folders, which store the data to be used.
- /images: Holds the images used in the notebooks.
- /notebooks: Contains the Jupyter notebooks for various applications, including:
  - 00_web_scraping.ipynb: Notebook used for scraping data from the Zap real estate website.
  - 01_data_understand.ipynb: Notebook for exploring and visualizing the dataset.
  - 02_prepare_data.ipynb: Notebook used to process data for training.
  - 03_modeling_regression.ipynb: Notebook for training and validating regression models.
  - 04_modeling_classification.ipynb: Notebook for training and validating classification models.
- /scripts: Contains additional scripts used in the project.
- columns.txt: A text file listing all the columns in the dataset.
- columns_described.txt: A text file describing the columns in the dataset.
- requiriments.txt: A file listing the project dependencies.
```

## Notebooks

In the `/notebooks` directory, you will find Jupyter notebooks that serve different purposes within the project. Here's a brief overview:

- **00_web_scraping.ipynb:** This notebook is used to scrape data from the Zap real estate website.

- **01_data_understand.ipynb:** In this notebook, the dataset is explored and visualizations are created to gain a better understanding of the data.

- **02_prepare_data.ipynb:** This notebook focuses on data preprocessing and preparing the data for training.

- **03_modeling_regression.ipynb:** Here, regression models are trained and validated using the prepared data.

- **04_modeling_classification.ipynb:** This notebook involves training and validating classification models.

## Scripts

The `/scripts` directory contains additional scripts that are used in the project. You can find more details about each script within their respective files.

## Dependencies

The project has dependencies listed in the `requiriments.txt` file. Make sure to install these dependencies before running the code. You can install them by running the following command:

```shell
pip install -r requiriments.txt
```
