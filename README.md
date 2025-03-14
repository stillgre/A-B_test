# A-B_test
Стек:

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Statsmodels

Репозиторий содержит:

- Исходный csv файл, взятый с ресурса https://www.kaggle.com/datasets/zhangluyuan/ab-testing
- Код на Python, который направлен на анализ эффективности введния новой страницы, оценка влияния на конверсию. Задачи, которые решались в процессе написания кода:

1. Выявление не соответствий между группами и страницами (group: control, treatment; landing_page: old_page, new_page)
2. Исправление несоответствий
3. A/B тестирование
4. Z-тестирование
5. Визуализация

Итог:

- Несоответствия групп и страниц: 3893
- Количество несоответствий после исправления: 0
- Конверсия в контрольной группе: 0.1204
- Конверсия в тестовой группе: 0.1189
- Z-статистика: -1.2369
- P-value: 0.2161

Выводы:
# Различие статистически незначимо (p-value > 0.05)
# Конверсия новой страницы незначительно ниже (z-test = -1.24)
# Введение новой страницы не влияет на конверсию, лишь незначительно её уменьшает
