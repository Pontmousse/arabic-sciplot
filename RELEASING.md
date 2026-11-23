# نشر إصدار على PyPI

يُنشر `arabic-sciplot` عبر **GitHub Actions + PyPI Trusted Publishing (OIDC)**. لا نحتاج إلى مفتاح API أو كلمة مرور داخل GitHub.

## ١. ربط المستودع بـ PyPI (مرة واحدة)

من صفحة [Pending Publishers](https://pypi.org/manage/account/publishing/) أدخل:

| الحقل | القيمة |
| --- | --- |
| PyPI Project Name | `arabic-sciplot` |
| Owner | `Pontmousse` |
| Repository name | `arabic-sciplot` |
| Workflow name | `publish.yml` |
| Environment name | `pypi` |

اضغط **Add** لإنشاء الناشر المعلّق. يمكن إضافة الناشر قبل إنشاء المشروع فعليًا على PyPI؛ تتكفّل أول عملية نشر ناجحة بإنشاء المشروع.

في GitHub، افتح **Settings → Environments**، وأنشئ بيئة باسم `pypi` إن لم تكن موجودة. يُفضّل ضبط قواعد الحماية المناسبة لتفويض النشر؛ يجب أن تسمح أي قيود للفروع والوسوم بوسم الإصدار الذي ستنشره.

## ٢. إصدار النسخة الأولى

1. ادمج طلب المراجعة الذي يضيف `.github/workflows/publish.yml` إلى `main`.
2. تأكد من نجاح اختبارات CI ومن أن `pyproject.toml` يتضمن `version = "0.1.0"`.
3. من **GitHub → Releases → Draft a new release** أنشئ الوسم `v0.1.0` من `main`، ثم انشر GitHub Release (ليس Pre-release).
4. ستبني GitHub Actions ملفَي wheel وsource distribution، ثم ترفعهما إلى PyPI بواسطة OIDC.
5. تحقق من الصفحة `https://pypi.org/project/arabic-sciplot/`، ثم جرّب `pip install arabic-sciplot`.

**مهم:** يجب أن يطابق الوسم رقم الإصدار في `pyproject.toml` مسبوقًا بالحرف `v`؛ وإلا تتوقف عملية النشر. لا تُنشر الإصدارات الموسومة في GitHub على أنها Pre-release بهذا المسار.

للإصدارات التالية، حدِّث `project.version` في طلب مراجعة ثم أنشئ وسمًا مطابقًا بعد الدمج. لا يمكن إعادة رفع رقم إصدار سبق نشره على PyPI.

**لا يؤدي دمج طلب المراجعة أو دفع commit عادي إلى نشر الحزمة**؛ يبدأ النشر حصريًا عند نشر GitHub Release.
