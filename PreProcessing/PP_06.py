import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


#!#########################################
#!Kategorik Değişkenlerde Eksik Değer Atama
#!#########################################

V1 = np.array([1, 3, 6, np.NaN, 7, 1, np.NaN, 9, 15])
V4 = np.array(["IT", np.NaN, "IK", "IK", "IK", "IK", "IK", "IT", "IT"], dtype=object)

df = pd.DataFrame({
    "maas" : V1,
    "departman" : V4
})

print("\n-> Veri Seti :\n", df)

#! 1-Mod işlemi ile en sık gözlenen veri neyse ona göre eksiklik giderilmeye çalışılır.
# mod = df["departman"].mode()[0]
# df.iloc[df["departman"].isnull(), df.columns.get_loc("departman")] = mod

# print("\n-> Mod alınarak eksikliğin giderilmesi :\n",
#     df["departman"]
# )

#! 2-Öncesinde veya sonrasındaki değer ile doldurma
print("\n-> Sonrasındaki değer ile doldur :\n",
    df["departman"].bfill()
)
print("\n-> Önceki değer ile doldur :\n",
    df["departman"].ffill()
)
















