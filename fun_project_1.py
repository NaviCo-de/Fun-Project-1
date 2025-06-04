import streamlit as st

def next_step():
    if st.session_state.p_index < len(data) - 1:
        st.session_state.p_index += 1

def back_step():
    if st.session_state.p_index > 0:
        st.session_state.p_index -= 1

st.title("🧐WHAT IS YOUR PASSION🧐")

st.header("Mini quizzz")
data = [
   {
       "pertanyaan" : "Saat nongkrong, lu lebih suka...",
       "pilihan": [
                "Duduk sambil ngerjain side project (iya, bawa laptop😎)",
                "Nge-review desain cafe: 'Ini kok norak bgt desainnya😐'",
                "Ngobrolin tren crypto, data Tiktok"
            ]
   },
   {
       "pertanyaan" : "Kalo disuruh ikut lomba, lu paling semangat kalau...",
       "pilihan": [
                "Hackathon bikin web/aplikasi",
                "Bikin desain buat aplikasi",
                "Suruh ngolah data buanyak banget biar rapih"
            ]
   },
   {
       "pertanyaan" : "Waktu kerja kelompok, lu biasanya...",
       "pilihan": [
                "Paling gercep ngambil coding-an pokoknya biar cepet kelar",
                "Maunya yang gambar gambar mulu",
                "Selalu nanya, 'INI DATA DAPET DARIMANA'"
            ]
   }
]

if "p_index" not in st.session_state:
    st.session_state.p_index = 0
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = [None] * len(data)

if "submitted" not in st.session_state:
    st.session_state.submitted = False

index_sekarang = st.session_state.p_index
pertanyaan_sekarang = data[index_sekarang]

st.subheader(f"Pertanyaan ke-{index_sekarang+1} dari {len(data)}")
jawaban = st.radio(
    pertanyaan_sekarang["pertanyaan"],
    pertanyaan_sekarang["pilihan"],
    index = pertanyaan_sekarang["pilihan"].index(st.session_state.jawaban_user[index_sekarang])
    if st.session_state.jawaban_user[index_sekarang] in pertanyaan_sekarang["pilihan"] else 0,
    key = f"radio_{index_sekarang}"
)

st.session_state.jawaban_user[index_sekarang] = jawaban

col1, col2  = st.columns([1,1])
with col1:
    st.button("Back", on_click=back_step)

with col2:
    if index_sekarang == len(data) - 1:
        if st.button("Submit"):
            st.session_state.submitted = True
    else:
        st.button("Next", on_click=next_step)

if st.session_state.submitted:
    jawaban_user = st.session_state.jawaban_user
    programmer = 0
    uiux = 0
    data_scientist = 0

    for i in range (len(jawaban_user)):
        for pilihan in data[i]["pilihan"]:
            if jawaban_user[i] == pilihan and data[i]["pilihan"].index(pilihan) == 0:
                programmer += 1
            elif jawaban_user[i] == pilihan and data[i]["pilihan"].index(pilihan) == 1:
                uiux += 1
            elif jawaban_user[i] == pilihan and data[i]["pilihan"].index(pilihan) == 2:
                data_scientist += 1

    if programmer > uiux and programmer > data_scientist:
        st.subheader("SELAMAT KAMU OTW TIDUR 1 JAM PER HARI SEBAGAI PROGRAMMER")
    elif uiux > programmer and uiux > data_scientist:
        st.subheader("SELAMAT KAMU BISA BEDAIN WARNA #FFFFFF SAMA #FEFEFE. COCOK JADI UIUX DESIGNER")
    elif data_scientist > programmer and data_scientist > uiux:
        st.subheader("SELAMAT KAMU BISA NGELIHAT 1000 LINE EXCEL SEKALIGUS. SEPUH DATSCI")
    else:
        st.subheader("SELAMAT KAMU ALL ROLE, COCOK JADI PROGRAMMER, UIUX, SAMA DATSCI")

    st.session_state.submitted = False
