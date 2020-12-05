import numpy
from sklearn.base import BaseEstimator, TransformerMixin

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class CustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        print('Execution NotasFeatureTransformer')

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        
        data = data[data['koi_pdisposition'].notna()]
        data = data[data['koi_score'].values < 1.1]
        
        return data
        
