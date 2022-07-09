import pandas as pd
import numpy as np

class tslabel_weak():
    """
        O módulo recebe como parâmetros:
            txt = dataset com dados textuais
            col_txt = coluna do dataset textual, contendo os textos
            serie = dataset com dados numericos
            pct = porcentagem para cálculo da diferença de um dia para o outro
            col = coluna com dados númericos (preços)
    """
    def __init__(self,
                txt,
                col_txt,
                serie,
                pct,
                col) -> None:

        self.txt = txt
        self.col_txt = col_txt
        self.serie = serie
        self.pct = pct
        self.col = col   

        self.df_price = self.serie
        self.df_price['diff'] = self.get_diff(self.df_price, self.col)
        self.df_price['per_diff'] = self.get_per(self.df_price, self.col)

        self.df_tx = self.txt
        self.df_tx = self.df_tx[[self.col_txt]]
        self.df_tx.sort_index(ascending=True, inplace=True)       

        if self.pct > 0:
            df = self.add_target_texts(self.df_tx, self.df_price, [self.pct], 0)
            
        elif self.pct < 0:
            df = self.add_target_texts(self.df_tx, self.df_price, [self.pct], 0)
        
        print(df.head(-1))


    
    def get_diff(self, df, column):
        df = df[column].diff().round(decimals=2)
        return df

    def get_per(self, df, column):
        per = df[column].pct_change().round(decimals=4)
        return per

    def add_target_texts(self, df_t, df_p, per, stp):
        
        if stp != 0:
            df_p['per_diff'] = df_p.per_diff.shift(periods=stp, fill_value=0)

        df = pd.merge(df_t, df_p['per_diff'], left_index=True, right_index=True)
        df['per_diff'] = df['per_diff'] * 100
        df['class'] = ''
        
        for p in per:
            if p >= 0:
                df.loc[df['per_diff'] > p, 'class'] = 'pos'
            elif p <= 0:
                df.loc[df['per_diff'] < p, 'class'] = 'neg'
        
        print("Number of Class:\n",df['class'].value_counts())
        
        return df

