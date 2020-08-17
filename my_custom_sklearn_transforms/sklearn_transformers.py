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

class NotasFeatureTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        print('Execution NotasFeatureTransformer')

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()

        # Removendo outliers
        data["NOTA_MF"] = numpy.where(data["NOTA_MF"] > 10, 10, data["NOTA_MF"])

        data["TAN_SQRT_NOTA_MF"] = numpy.tan(sqrt(data['NOTA_MF']))
        data["SQRT_NOTA_MF"] = numpy.sqrt(data['NOTA_MF'])
        data["SQRT_NOTA_DE"] = numpy.sqrt(data['NOTA_DE'])
        data["SQRT_NOTA_EM"] = numpy.sqrt(data['NOTA_MF'])
        data["SQRT_NOTA_GO"] = numpy.sqrt(data['NOTA_GO'])

        data["D_NOTA_DE"] = numpy.where(data["NOTA_DE"] <= 6, 0, 1)
        data["D_NOTA_EM"] = numpy.where(data["NOTA_EM"] <= 6, 0, 1)
        data["D_NOTA_MF"] = numpy.where(data["NOTA_MF"] <= 6, 0, 1)
        data["D_NOTA_GO"] = numpy.where(data["NOTA_GO"] <= 6, 0, 1)

        data["REPROVACOES_DE"] = numpy.where(data["REPROVACOES_DE"] > 1, 1, data["REPROVACOES_DE"])
        data["REPROVACOES_EM"] = numpy.where(data["REPROVACOES_EM"] > 1, 1, data["REPROVACOES_EM"])
        data["REPROVACOES_MF"] = numpy.where(data["REPROVACOES_MF"] > 1, 1, data["REPROVACOES_MF"])
        data["REPROVACOES_GO"] = numpy.where(data["REPROVACOES_GO"] > 1, 1, data["REPROVACOES_GO"])

        return data
        
