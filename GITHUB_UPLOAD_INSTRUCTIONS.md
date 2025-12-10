# تعليمات رفع المشروع على GitHub

## الخطوات:

### 1. إنشاء Repository جديد على GitHub:
   - اذهب إلى https://github.com/new
   - اختر اسم للمشروع (مثلاً: `camel-tools` أو `camel-tools-ut`)
   - اختر Public أو Private حسب رغبتك
   - **لا** تضع علامة على "Initialize this repository with a README"
   - اضغط على "Create repository"

### 2. ربط المشروع المحلي بـ GitHub:
   بعد إنشاء الـ repository، سيعرض GitHub أوامر. استخدم الأوامر التالية:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

**ملاحظة:** استبدل `YOUR_USERNAME` و `YOUR_REPO_NAME` باسم المستخدم واسم الـ repository الذي أنشأته.

### 3. إذا كنت تستخدم SSH بدلاً من HTTPS:
```bash
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### 4. إذا كان لديك بالفعل repository على GitHub:
   - استخدم الأمر التالي لإضافة الـ remote:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   ```
   - ثم ارفع المشروع:
   ```bash
   git branch -M main
   git push -u origin main
   ```

## ملاحظات مهمة:
- تم إعداد Git config محلياً فقط لهذا المشروع
- تم إضافة `venv/` إلى `.gitignore` حتى لا يتم رفع البيئة الافتراضية
- جميع الملفات المهمة تم إضافتها إلى Git
- إذا واجهت مشكلة في المصادقة، قد تحتاج إلى إعداد GitHub Personal Access Token

## للمساعدة:
إذا واجهت أي مشكلة، أخبرني وسأساعدك في حلها.

