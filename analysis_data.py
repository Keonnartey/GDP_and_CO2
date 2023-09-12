# %%
import pandas as pd
import matplotlib.pyplot as plt

Data_new = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
# %%
data_new_subset = Data_new[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]
data_new_subset
# %%
plt.scatter(
    data_new_subset["Mortality rate, infant (per 1,000 live births)"],
    data_new_subset["GDP per capita (constant 2010 US$)"],
)
plt.xlabel("Mortality rate")
plt.ylabel("GDP")
plt.title("Mortality rate vs GDP per Capita")
plt.show()
# %%
