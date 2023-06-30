# Method to label texts using time series.

This repository contains code and resources for performing weak supervision using function labeling to generate text from time series features. The approach utilizes intraday oscillation time series data to label text data.

## Introduction

In many applications, obtaining labeled text data for training machine learning models can be a challenging and time-consuming task. Weak supervision techniques provide an alternative approach to generating labeled data by leveraging auxiliary information. In this project, we focus on generating text labels from time series features using intraday oscillation data.

## Requirements

To run the code in this repository, you will need the following:

- Python (version 3.7 or above)
- NumPy
- Pandas

## Getting Started

Clone the repository:

```python
!pip install git+https://github.com/ivanfilhoreis/ts_label.git -q
!pip install pandas --upgrade

```

## Usage

This step will read the data for labeling.

```python
from tslabel_weak import tslabel_weak as ts
import pandas as pd

# time series data
ts = pd.read_excel('dataset\Cepea_milho.xls')
ts.set_index('date', inplace=True)

# textual data
df_tx = pd.read_excel('dataset\Scraping_Cepea_En_Noticias.xlsx', index_col='Date')
df_tx.index = pd.to_datetime(df_tx.index)
```

This step will generate text labels for the given time series data using the trained model.

```python
txt_lb = ts (txt=df_tx, col_txt='text', serie=ts, col='real', pct= 0.03, )

```

The parameters are:

- txt     = dataset with texts.
- col_txt = column of dataset with texts.
- serie   = prices series
- col     = column with prices series
- pct     = Threshold in percentage to define the label


## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
