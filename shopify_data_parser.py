import numpy as np
import pandas as pd

FILE_NAME = 'data.csv'

data = pd.read_csv(FILE_NAME)

# filtering out identified outliers
data = data.loc[data["total_items"] != 2000]
data = data.loc[data["shop_id"] != 78]

# calculating and outputting new mean
order_amounts = data['order_amount'].to_numpy()
aov = np.mean(order_amounts)
print(aov)


