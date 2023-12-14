import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

data = {
    'yil': [2023, 2023, 2022, 2022, 2021, 2020],
    'net_tl': [11402.32, 8506.80, 5500.35, 4253.40, 2825.90, 2324.00],
    'dolar': [23.71, 18.67, 16.76, 17.10, 7.43, 5.95]
}

df = pd.DataFrame(data)
reg = LinearRegression()
reg.fit(df[['yil', 'net_tl']], df['dolar'])

while 1:
    print(f"\033[96m")
    yil_input = int(input("Lütfen yıl bilgisini girin: "))
    net_tl_input = float(input("Lütfen net TL bilgisini girin: "))

    tahmin_dolar = reg.predict([[yil_input, net_tl_input]])

    print(f"\033[91mTahmini Dolar Kuru: {tahmin_dolar[0]:.2f}")

    print("\n")
