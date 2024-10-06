import pandas as pd
import pickle

model_path = 'models/train-2023-08-01.pkl'
data_path = 'data/predict-2023-08-03.parquet'

def main(event, context):
    # Carregar o modelo salvo
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Carregar os dados para previsão
    df = pd.read_parquet(data_path)

    # Definir as variáveis independentes (X) para as previsões
    X = df[['store_id', 'year', 'month', 'day', 'weekday']]

    # Fazer previsões
    df['predicted_sales'] = model.predict(X)

    # print("=========== Predict ===========")
    return df['predicted_sales'].tolist()