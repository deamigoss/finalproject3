import streamlit as st
from sqlalchemy import text

list_montir = ['', 'Subagja', 'Andi', 'Karyono']
list_transmisi = ['', 'Matic', 'Cub']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://rizkiim198:5prbLmGT4qZk@ep-holy-snow-47509721.us-east-2.aws.neon.tech/finalproject3")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS SERVICES (id serial, nama_montir varchar, nama_motor varchar, transmisi char(25), \
                                                       yang_ditangani text, harga_service varchar, servis_ke text, tanggal_pengerjaan date);')
    session.execute(query)

st.header('SIMPLE RECORD PEKERJAAN')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM services ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO services (nama_montir, nama_motor, transmisi, yang_ditangani, harga_service, servis_ke, waktu_pengerjaan, tanggal_pengerjaan) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'[]', '5':'', '6':'', '7':'', '8':None})
            session.commit()

    data = conn.query('SELECT * FROM services ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        nama_montir_lama = result["nama_montir"]
        nama_motor_lama = result["nama_motor"]
        transmisi_lama = result["transmisi"]
        yang_ditangani_lama = result["yang_ditangani"]
        harga_servis_lama = result["harga_servis"]
        servis_ke_lama = result["servis_ke"]
        waktu_pengerjaan_lama = result["waktu_pengerjaan"]
        tanggal_pengerjaan_lama = result["tanggal_pengerjaan"]

        with st.expander(f'a.n. {nama_montir_lama}'):
            with st.form(f'data-{id}'):
                nama_montir_baru = st.selectbox("nama_montir", list_montir, list_montir.index(nama_montir_lama))
                nama_motor_baru = st.text_input("nama_motor", nama_motor_lama)
                transmisi_baru = st.selectbox("transmisi", list_transmisi, list_transmisi.index(transmisi_lama))
                yang_ditangani_baru = st.multiselect("yang_ditangani", ["Perawatan", "Ganti Ban", "Ganti Oli", "Ganti Aki"], eval(yang_ditangani_lama))
                harga_servis_baru = st.text_input("harga_servis", harga_servis_lama)
                servis_ke_baru = st.text_input("servis_ke", servis_ke_lama)
                waktu_pengerjaan_baru = st.text_input("waktu", waktu_pengerjaan_lama)
                tanggal_pengerjaan_baru = st.date_input("tanggal_pengerjaan", tanggal_pengerjaan_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE services \
                                          SET nama_montir=:1, nama_motor=:2, transmisi=:3, yang_ditangani=:4, \
                                          harga_servis=:5, servis_ke=:6, waktu_pengerjaan=:7, tanggal_pengerjaan=:8 \
                                          WHERE id=:9;')
                            session.execute(query, {'1':nama_montir_baru, '2':nama_motor_baru, '3':transmisi_baru, '4':str(yang_ditangani_baru), 
                                                    '5':harga_servis_baru, '6':servis_ke_baru, '7':waktu_pengerjaan_baru, '8':tanggal_pengerjaan_baru, '9':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM services WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()