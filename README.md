# Arabic SciPlot — الرسم العلمي بالعربية

حزمة صغيرة لتنسيق عناوين الرسوم البيانية ومحاورها وتدريجاتها بالعربية باستخدام **Matplotlib**، مع أدوات رقمية يمكن استعمالها في **Plotly**.

## التثبيت

يتطلب الإصدار `0.1.0` بايثون 3.11 أو أحدث وMatplotlib 3.11 أو أحدث.

بعد نشر الحزمة في PyPI:

```bash
pip install arabic-sciplot
```

للتجربة من المستودع قبل النشر:

```bash
pip install -e .
```

ولتشغيل أمثلة Plotly وB-spline الاختيارية: `pip install -e ".[examples]"`.

## الاستعمال

```python
import numpy as np
import matplotlib.pyplot as plt
from arabic_sciplot import arab, arabic_2d_axis_formatter

x = np.linspace(-5, 5, 200)
fig, ax = plt.subplots()
ax.plot(x, x**2)
ax.set_title(arab("تمثيل دالة تربيعية"))
arabic_2d_axis_formatter(ax)
plt.show()
```

التوابع المتاحة: `arab`، `custom_formatter`، `custom_log_formatter`، `pi_formatter`، `generate_tickvals_and_text`، `arabic_2d_axis_formatter`، `arabic_3d_axis_formatter`، و`arabic_3d_plot_formatter`.

يمكن تعطيل قلب المحور أو تعديل نمط التدريجات من غير تغيير الإعدادات الافتراضية القديمة:

```python
arabic_2d_axis_formatter(ax, invert_x=False, y_on_right=False,
                         tick_direction="out", tick_length=4, tick_labelsize=12)
```

## اتجاه الكتابة والخطوط

أضاف **Matplotlib 3.11** دعم تشكيل الحروف العربية وترتيب الكتابة من اليمين إلى اليسار. لذلك يعيد `arab(text)` النص نفسه دون تغييره، ولم نعد نستخدم `arabic-reshaper` أو `python-bidi`. **لا تُمرّر نصًا مُعاد تشكيله مسبقًا** إلى Matplotlib الجديد؛ فقد ينعكس ترتيبه مرتين.

يجب توفر خط يدعم المحارف المطلوبة، مثل **DejaVu Sans** للحروف الشائعة، أو **Amiri** أو **Noto Naskh Arabic** لبعض النصوص والتشكيل. لا تُضمّن الحزمة خطوطًا ولا تفرض خطًا على المستخدم. يمكن تعيين خط مثبت لديك عبر `plt.rcParams["font.family"] = "Amiri"`. يعتمد العرض النهائي على الخط ومحرك الرسم.

تُبقي الدوال الإعدادات القديمة للمحاور: قلب المحور السيني، ونقل تدريجات الصادات إلى اليمين في الرسم الثنائي، وقلب المحورين الأفقيين في الرسم الثلاثي.

## أمثلة

- `examples/basic_2d.py` — رسم علمي ثنائي الأبعاد.
- `examples/plot_3d.py` — رسم حلزوني ثلاثي الأبعاد.
- `examples/plotly_ticks.py` — تدريجات رياضية عربية في Plotly (إضافي).
- `examples/vector_field.py` — حقل متجهات مأخوذ من [الموسوعة العربية](https://github.com/Pontmousse/alalbab/blob/main/resources/calculus/vector_calculus/curl2d.py).
- `examples/spline_animation.py` — منحنى B-spline متحرك من [الموسوعة العربية](https://github.com/Pontmousse/alalbab/blob/main/resources/geometry/splines/bsplines/bspline.py)؛ ينشئ ملف GIF ويحتاج SciPy وPillow.

## الترخيص

MIT — انظر `LICENSE`.
