
import gradio as gr
import numpy as np
import joblib

scaler = joblib.load("/content/scaler.pkl")
feature_cols = joblib.load("/content/feature_cols.pkl")
model_rf = joblib.load("/content/model_rf.pkl")

CLASS_LABELS = {0:"Normal", 1:"LG Fault", 2:"LL Fault",
                3:"LLG Fault", 4:"LLL Fault", 5:"LLLG Fault"}

FAULT_DESC = {
    0: "Sistem beroperasi normal, tidak ada gangguan terdeteksi.",
    1: "Line-to-Ground Fault: Gangguan satu fasa ke tanah.",
    2: "Line-to-Line Fault: Gangguan antar dua fasa.",
    3: "Double Line-to-Ground Fault: Gangguan dua fasa ke tanah.",
    4: "Three-Phase Fault: Gangguan tiga fasa serentak.",
    5: "Three-Phase-to-Ground Fault: Gangguan tiga fasa ke tanah."
}

def predict(*args):
    x = np.array(args).reshape(1,-1)
    x_scaled = scaler.transform(x)
    pred = model_rf.predict(x_scaled)[0]
    proba = model_rf.predict_proba(x_scaled)[0]

    classes = model_rf.classes_
    prob_table = "\n\n**Probabilitas per Kelas:**\n"
    for i, cls in enumerate(classes):
        bar = "█" * int(proba[i] * 20)
        prob_table += f"- {CLASS_LABELS[cls]}: {bar} {proba[i]*100:.1f}%\n"

    status = "🟢" if pred == 0 else "🔴"
    result  = f"## {status} Prediksi: {CLASS_LABELS[pred]}\n\n"
    result += f"**Konfidiensi:** {proba[list(classes).index(pred)]*100:.1f}%\n\n"
    result += f"**Deskripsi:** {FAULT_DESC[pred]}"
    result += prob_table
    return result

inputs = [gr.Number(label=c, value=0) for c in feature_cols]
demo = gr.Interface(
    fn=predict,
    inputs=inputs,
    outputs=gr.Markdown(),
    title="⚡ Electrical Fault Detection & Classification",
    description="Masukkan nilai arus (Ia, Ib, Ic) dan tegangan (Va, Vb, Vc) untuk mendeteksi jenis gangguan jaringan listrik.",
    examples=[
        [0, 0, 0, 0.4, -0.2, -0.2],
        [-151.29, -9.68, 85.80, 0.40, -0.13, -0.27],
        [-300, -300, 100, 0.1, 0.1, -0.2],
    ],
    theme=gr.themes.Soft()
)
demo.launch(share=True)
