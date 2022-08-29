# ts_labels
Uso de dados de séries temporais para rotular documentos de textos.

Essa implementação faz a união de dados textuais e séries temporais por meio de suas datas. Calcula a diferença intra-dia da série temporal e atribui o rótulo conforme a variação.

# 1. Instalação
A instalação é feita da seguinte forma:

```
!pip install git+https://github.com/ivanfilhoreis/ts_labels.git -q
!pip install pandas --upgrade

```

# 2. Uso
Primeiro passo é a formatação das datas para um padrão igual:

```
from tslabel_weak import tslabel_weak as ts
import pandas as pd

#dados da série temporal
df = pd.read_excel('test_dataset\Cepea_milho.xls')
df.set_index('date', inplace=True)

#dados textuais
df_tx = pd.read_excel('test_dataset\Scraping_Cepea_En_Noticias.xlsx', index_col='Date')
df_tx.index = pd.to_datetime(df_tx.index)
```

Os parêmetros do tslabel_weak são:

    txt = dataset com dados textuais
    col_txt = coluna do dataset contendo os textos
    serie = dataset com dados numericos
    pct = porcentagem para cálculo da diferença intra-dia
    col = coluna com dados númericos
    
Assim, para realizar a rotulagem chama a função da seguinte forma:

```
teste = ts(txt= df_tx, col_txt='Text_Headline', serie= df, pct= 0.03, col='real')
```




