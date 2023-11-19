from datetime import datetime
import streamlit as st
from streamlit_extras.grid import grid
import pandas as pd

st.set_page_config(layout='wide',initial_sidebar_state='collapsed') 
def main():
    my_grid = grid([10,1,1], vertical_align="top")
    my_grid.title("6661 AGİ DESTEK KONTROL ROBOTU")
    aylar = {"01": "Ocak", "02": "Şubat", "03": "Mart", "04": "Nisan", "05": "Mayıs", "06": "Haziran",
            "07": "Temmuz", "08": "Ağustos", "09": "Eylül", "10": "Ekim", "11": "Kasım", "12": "Aralık"}
    selected_month = my_grid.selectbox("Ay Seç", aylar.values())
    selected_year = my_grid.number_input("Yıl Seç", min_value=2000, max_value=datetime.now().year, step=1, value=datetime.now().year)
    selected_month_key = [key for key, value in aylar.items() if value == selected_month][0]
    st.success("Seçilen Dönem: " + str(selected_month_key) + "/" + str(selected_year))
    df = pd.DataFrame([
        {"SAP Kodu": "", "İŞ YERİ ADI": "", "KULLANICI ADI": "", "KULLANICI KODU": "", "SİSTEM ŞİFRESİ": "","İŞYERİ ŞİFRESİ": "",str(selected_month) + "-" + str(selected_year)+ " 6661 AGİ Destek Tutarları": "", }])
    
    edit_df = st.data_editor(df,use_container_width=True, num_rows="dynamic",)
    if st.button("Robot Başlat",key="start",):
        pass
    if st.button("Raporu İndir",key="download"):
        edit_df.to_excel(str(selected_month) + "-" + str(selected_year)+ " 6661 AGİ Destek Tutarları Raporu.xlsx", index=False)
        st.toast(body="Excel dosyası indirildi!",)

if __name__ == "__main__":
    main()
