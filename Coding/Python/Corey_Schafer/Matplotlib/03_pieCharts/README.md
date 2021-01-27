# Pie Chart

- Modify the pie colour
- Change the edge colour
- Explode the pie
- Add shadow
- Change the start angle
- Add the percentage method `autopct="%1.1f%%"`

```python
slices = [60, 40, 30, 20]

labels = ['After Effect', 'Maya', 'PhotoShop', 'Illustrator']
colors = ['#7F239B', '#4A4A4A', '#332CFF', '#E6B30E']
explode = [0, 0.2, 0, 0]
# 0 to 1 == centre to border

plt.pie(slices, # Object
        labels=labels,
        colors=colors,
        explode=explode, 
        shadow=True, 
        startangle=90, 
        autopct="%1.1f%%",
        wedgeprops={'edgecolor':'black'})
```
Unique pecentage format: __*`autopct="%1.1f%%"`*__

Suggestion: _*Apply pie chart if the items are less than five*_
