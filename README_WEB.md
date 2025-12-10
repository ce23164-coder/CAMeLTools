# واجهة ويب لـ CAMeL Tools

## التثبيت

1. تثبيت المتطلبات:
```bash
pip install -r requirements-web.txt
```

أو في بيئة venv:
```bash
.\venv\Scripts\pip.exe install streamlit
```

## التشغيل

لتشغيل الواجهة، استخدم الأمر التالي:

```bash
streamlit run web_app.py
```

أو في بيئة venv:
```bash
.\venv\Scripts\streamlit.exe run web_app.py
```

بعد التشغيل، ستفتح الواجهة في المتصفح تلقائياً على العنوان:
`http://localhost:8501`

## الميزات

- ✅ التحليل الصرفي للكلمات العربية
- ✅ التحويل بين أنظمة الكتابة المختلفة
- ✅ تنظيف النص العربي
- ✅ إزالة التشكيل
- ✅ تقسيم النص إلى كلمات
- ✅ واجهة عربية سهلة الاستخدام

## ملاحظات

- تأكد من تثبيت camel_tools بشكل صحيح
- قد تحتاج إلى تثبيت البيانات المطلوبة باستخدام `camel_data -i defaults`

