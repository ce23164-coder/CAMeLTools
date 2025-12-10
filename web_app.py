#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
واجهة ويب لـ CAMeL Tools
Web Interface for CAMeL Tools
"""

import streamlit as st
import sys
import os

# إضافة المسار الحالي للمسار
sys.path.insert(0, os.path.dirname(__file__))

st.set_page_config(
    page_title="CAMeL Tools - أدوات معالجة اللغة العربية",
    page_icon="🐪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS مخصص للعربية
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        padding: 20px;
    }
    .arabic-text {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', 'Tahoma', sans-serif;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #ddd;
        margin: 10px 0;
        color: #000000;
    }
    .result-box p {
        color: #000000;
    }
    .result-box pre {
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# العنوان الرئيسي مع الشعار
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        # محاولة عرض الشعار إذا كان موجوداً
        logo_path = "logo.png"
        if os.path.exists(logo_path):
            st.image(logo_path, use_container_width=True)
        else:
            # إذا لم يوجد الشعار، عرض العنوان فقط
            st.title("🐪 CAMeL Tools - أدوات معالجة اللغة العربية")
    except Exception:
        st.title("🐪 CAMeL Tools - أدوات معالجة اللغة العربية")

st.markdown("---")

# شريط جانبي للاختيار
st.sidebar.title("🔧 الأدوات المتاحة")
tool_choice = st.sidebar.radio(
    "اختر الأداة:",
    [
        "🏠 الصفحة الرئيسية",
        "📝 التحليل الصرفي (Morphology)",
        "🔄 التحويل بين أنظمة الكتابة (Transliteration)",
        "🧹 تنظيف النص العربي (Arabic Cleaning)",
        "🔤 إزالة التشكيل (Dediacritization)",
        "✂️ تقسيم النص (Tokenization)",
        "ℹ️ معلومات المشروع"
    ]
)

# الصفحة الرئيسية
if tool_choice == "🏠 الصفحة الرئيسية":
    st.header("مرحباً بك في CAMeL Tools")
    st.markdown("""
    ### ما هو CAMeL Tools؟
    
    **CAMeL Tools** هي مجموعة شاملة من أدوات معالجة اللغة الطبيعية للعربية، 
    تم تطويرها من قبل **سجاد كاظم** و **زينب جاسم** في الجامعة التكنولوجية.
    
    ### الوظائف المتاحة:
    
    1. **التحليل الصرفي** - تحليل الكلمات العربية صرفياً
    2. **التحويل بين أنظمة الكتابة** - تحويل بين أنظمة الكتابة المختلفة (Buckwalter, XML, SafeBW, etc.)
    3. **تنظيف النص العربي** - تنظيف وتطبيع النص العربي
    4. **إزالة التشكيل** - إزالة علامات التشكيل من النص
    5. **تقسيم النص** - تقسيم النص العربي إلى كلمات
    
    ### كيفية الاستخدام:
    
    استخدم القائمة الجانبية لاختيار الأداة التي تريد استخدامها.
    """)

# التحليل الصرفي
elif tool_choice == "📝 التحليل الصرفي (Morphology)":
    st.header("التحليل الصرفي")
    st.markdown("تحليل الكلمات العربية صرفياً")
    
    try:
        from camel_tools.morphology.database import MorphologyDB
        from camel_tools.morphology.analyzer import Analyzer
        
        # اختيار قاعدة البيانات
        db_name = st.selectbox(
            "اختر قاعدة البيانات:",
            ["calima-msa-r13", "calima-egy-r13"],
            help="MSA = Modern Standard Arabic, EGY = Egyptian Arabic"
        )
        
        # إدخال النص
        text_input = st.text_area(
            "أدخل النص العربي:",
            height=100,
            placeholder="مثال: شارع"
        )
        
        if st.button("تحليل", type="primary"):
            if text_input.strip():
                try:
                    # تحميل قاعدة البيانات
                    with st.spinner("جاري تحميل قاعدة البيانات..."):
                        db = MorphologyDB.builtin_db(db_name)
                        analyzer = Analyzer(db)
                    
                    # تحليل النص
                    words = text_input.split()
                    results = []
                    
                    for word in words:
                        analyses = analyzer.analyze(word)
                        results.append({
                            'word': word,
                            'analyses': analyses
                        })
                    
                    # عرض النتائج
                    st.success("تم التحليل بنجاح!")
                    for result in results:
                        st.markdown(f"### الكلمة: **{result['word']}**")
                        if result['analyses']:
                            for i, analysis in enumerate(result['analyses'], 1):
                                st.markdown(f"""
                                <div class="result-box">
                                    <strong>التحليل {i}:</strong><br>
                                    <pre style="color: #000000;">{analysis}</pre>
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.warning("لم يتم العثور على تحليل لهذه الكلمة")
                except Exception as e:
                    st.error(f"حدث خطأ: {str(e)}")
            else:
                st.warning("الرجاء إدخال نص للتحليل")
    except ImportError as e:
        st.error(f"خطأ في استيراد المكتبات: {str(e)}")
        st.info("تأكد من تثبيت camel_tools بشكل صحيح")

# التحويل بين أنظمة الكتابة
elif tool_choice == "🔄 التحويل بين أنظمة الكتابة (Transliteration)":
    st.header("التحويل بين أنظمة الكتابة")
    st.markdown("تحويل النص العربي بين أنظمة الكتابة المختلفة")
    
    try:
        from camel_tools.utils.charmap import CharMapper
        
        # اختيار نوع التحويل
        conversion_type = st.selectbox(
            "نوع التحويل:",
            [
                "ar2bw", "bw2ar",
                "ar2safebw", "safebw2ar",
                "ar2xmlbw", "xmlbw2ar",
                "ar2hsb", "hsb2ar"
            ]
        )
        
        text_input = st.text_area(
            "أدخل النص:",
            height=100,
            placeholder="مثال: مرحبا"
        )
        
        if st.button("تحويل", type="primary"):
            if text_input.strip():
                try:
                    mapper = CharMapper.builtin_mapper(conversion_type)
                    result = mapper(text_input)
                    st.success("تم التحويل بنجاح!")
                    st.markdown(f"""
                    <div class="result-box">
                        <strong>النتيجة:</strong><br>
                        <p style="font-size: 20px; direction: ltr; text-align: center; color: #000000;">{result}</p>
                    </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"حدث خطأ: {str(e)}")
            else:
                st.warning("الرجاء إدخال نص للتحويل")
    except ImportError as e:
        st.error(f"خطأ في استيراد المكتبات: {str(e)}")

# تنظيف النص العربي
elif tool_choice == "🧹 تنظيف النص العربي (Arabic Cleaning)":
    st.header("تنظيف النص العربي")
    st.markdown("تنظيف وتطبيع النص العربي")
    
    try:
        from camel_tools.utils.charmap import CharMapper
        
        text_input = st.text_area(
            "أدخل النص العربي:",
            height=100,
            placeholder="مثال: النص الذي تريد تنظيفه"
        )
        
        if st.button("تنظيف", type="primary"):
            if text_input.strip():
                try:
                    mapper = CharMapper.builtin_mapper('arclean')
                    result = mapper(text_input)
                    st.success("تم التنظيف بنجاح!")
                    st.markdown(f"""
                    <div class="result-box">
                        <strong>النص الأصلي:</strong><br>
                        <p style="color: #000000;">{text_input}</p>
                        <strong>النص المنظف:</strong><br>
                        <p style="color: #000000;">{result}</p>
                    </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"حدث خطأ: {str(e)}")
            else:
                st.warning("الرجاء إدخال نص للتنظيف")
    except ImportError as e:
        st.error(f"خطأ في استيراد المكتبات: {str(e)}")

# إزالة التشكيل
elif tool_choice == "🔤 إزالة التشكيل (Dediacritization)":
    st.header("إزالة التشكيل")
    st.markdown("إزالة علامات التشكيل من النص العربي")
    
    try:
        from camel_tools.utils.dediac import dediac_ar
        
        text_input = st.text_area(
            "أدخل النص المشكل:",
            height=100,
            placeholder="مثال: مَرْحَباً"
        )
        
        if st.button("إزالة التشكيل", type="primary"):
            if text_input.strip():
                try:
                    result = dediac_ar(text_input)
                    st.success("تمت إزالة التشكيل بنجاح!")
                    st.markdown(f"""
                    <div class="result-box">
                        <strong>النص الأصلي:</strong><br>
                        <p style="color: #000000;">{text_input}</p>
                        <strong>النص بدون تشكيل:</strong><br>
                        <p style="color: #000000;">{result}</p>
                    </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"حدث خطأ: {str(e)}")
            else:
                st.warning("الرجاء إدخال نص لإزالة التشكيل")
    except ImportError as e:
        st.error(f"خطأ في استيراد المكتبات: {str(e)}")

# تقسيم النص
elif tool_choice == "✂️ تقسيم النص (Tokenization)":
    st.header("تقسيم النص")
    st.markdown("تقسيم النص العربي إلى كلمات")
    
    try:
        from camel_tools.tokenizers.word import simple_word_tokenize
        
        text_input = st.text_area(
            "أدخل النص العربي:",
            height=100,
            placeholder="مثال: مرحبا بك في CAMeL Tools"
        )
        
        if st.button("تقسيم", type="primary"):
            if text_input.strip():
                try:
                    tokens = simple_word_tokenize(text_input)
                    st.success("تم التقسيم بنجاح!")
                    st.markdown(f"""
                    <div class="result-box">
                        <strong>عدد الكلمات:</strong> {len(tokens)}<br>
                        <strong>الكلمات:</strong><br>
                        <p style="color: #000000;">{' | '.join(tokens)}</p>
                    </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"حدث خطأ: {str(e)}")
            else:
                st.warning("الرجاء إدخال نص للتقسيم")
    except ImportError as e:
        st.error(f"خطأ في استيراد المكتبات: {str(e)}")

# معلومات المشروع
elif tool_choice == "ℹ️ معلومات المشروع":
    st.header("معلومات المشروع")
    st.markdown("""
    ### CAMeL Tools
    
    **CAMeL Tools** هي مجموعة شاملة من أدوات معالجة اللغة الطبيعية للعربية.
    
    ### المطورون:
    - **سجاد كاظم** - الجامعة التكنولوجية
    - **زينب جاسم** - الجامعة التكنولوجية
    
    ### الروابط:
    - [GitHub](https://github.com/CAMeL-Lab/CAMeL_Tools)
    - [التوثيق](https://camel-tools.readthedocs.io/)
    
    ### الرخصة:
    MIT License
    
    ### الإصدار:
    """)
    
    try:
        import camel_tools
        st.info(f"الإصدار المثبت: {camel_tools.__version__}")
    except:
        st.warning("لا يمكن تحديد الإصدار")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "تم التطوير باستخدام CAMeL Tools و Streamlit | "
    "Developed with CAMeL Tools and Streamlit"
    "</div>",
    unsafe_allow_html=True
)

