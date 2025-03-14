import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest

file_path = r"C:\Users\USER\Desktop\ab\ab_data.csv"  # указываем путь
df = pd.read_csv(file_path)


mismatch = df[
    (df["group"] == "control") & (df["landing_page"] == "new_page")
    | (df["group"] == "treatment") & (df["landing_page"] == "old_page")
]
print("Несоответствия групп и страниц:", len(mismatch))


if len(mismatch) > 0:
    df.loc[
        (df["group"] == "control") & (df["landing_page"] == "new_page"), "landing_page"
    ] = "old_page"
    df.loc[
        (df["group"] == "treatment") & (df["landing_page"] == "old_page"),
        "landing_page",
    ] = "new_page"


new_mismatch = len(
    df[
        (df["group"] == "control") & (df["landing_page"] == "new_page")
        | (df["group"] == "treatment") & (df["landing_page"] == "old_page")
    ]
)

print("Количество несоответствий после исправления:", new_mismatch)

# A/B тестирование с использованием z-теста


control = df[df["group"] == "control"]
treatment = df[df["group"] == "treatment"]

conversion_control = control["converted"].mean()
conversion_treatment = treatment["converted"].mean()

n_control = len(control)
n_treatment = len(treatment)

success_control = control["converted"].sum()
success_treatment = treatment["converted"].sum()

# Проведение Z-теста
successes = np.array([success_treatment, success_control])  # treatment first!
nobs = np.array([n_treatment, n_control])  # treatment first!
z_stat, p_value = proportions_ztest(successes, nobs)

# Визуализация результатов
plt.figure(figsize=(10, 6))
sns.barplot(
    x=["Control (old_page)", "Treatment (new_page)"],
    y=[conversion_control, conversion_treatment],
)
plt.title("Конверсия в контрольной и тестовой группах")
plt.ylabel("Доля конверсий")
plt.ylim(0, max([conversion_control, conversion_treatment]) + 0.05)
plt.grid(True)
plt.show()


print(f"Конверсия в контрольной группе: {conversion_control:.4f}")
print(f"Конверсия в тестовой группе: {conversion_treatment:.4f}")
print(f"Z-статистика: {z_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Вывод:
# Различие статистически незначимо (p-value > 0.05)
# Конверсия новой страницы незначительно ниже (z-test = -1.24)
# Введение новой страницы не влияет на конверсию, лишь незначительно её уменьшает
