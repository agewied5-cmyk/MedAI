import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعدادات واجهة المستخدم الاحترافية
st.set_page_config(page_title="MedAI | مساعدك الصيدلي", page_icon="💊")

# إضافة لمسة جمالية للتطبيق
st.markdown("""
    <style>
    .stHeader { color: #2E7D32; }
    .reportview-container { background: #f0f2f6; }
    </style>
    """, unsafe_allow_html=True)

# تفعيل المحرك (استبدل الرمز بمفتاحك الخاص)
API_KEY = "AIzaSyDTfTUNgBEzzAajW63b9beryynnBGlaXFA"

if API_KEY != "ضغ_مفتاح_جوجل_هنا":
    genai.configure(api_key=API_KEY)
    # استخدام فلاش لسرعة الاستجابة ودقة قراءة النصوص
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.title("💊 تطبيق MedAI للتعرف على الأدوية")
    st.write("قم بتصوير شريط الدواء بوضوح للحصول على تحليل دقيق.")

    file = st.file_uploader("ارفع صورة الدواء هنا", type=['jpg', 'png', 'jpeg'])

    if file:
        img = Image.open(file)
        st.image(img, caption="الصورة المرفوعة", use_column_width=True)
        
        if st.button("🚀 بدء التحليل الذكي"):
            with st.spinner("جاري الاتصال بقاعدة البيانات الطبية وتحليل الصورة..."):
                # استدعاء الأمر القوي (The Gold Prompt)
                final_prompt = """
                تحرك كخبير صيدلي. حلل الصورة بدقة:
                1. استخرج اسم الدواء والتركيز.
                2. حدد المادة الفعالة.
                3. حدد الشكل الصيدلاني (كبسولة، قرص، إلخ) وكيفية التناول.
                4. اشرح الاستخدام بلغة عربية بسيطة جداً.
                في النهاية أضف تحذيراً طبياً.
                """
                
                try:
                    response = model.generate_content([final_prompt, img])
                    st.success("تم التحليل بنجاح!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"عذراً، حدث خطأ تقني: {e}")
else:
    st.warning("⚠️ الخطوة الأخيرة: يرجى وضع الـ API Key داخل الكود ليعمل التطبيق.")
