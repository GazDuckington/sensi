from sensi import prediksi_nbc, per_kata, per_kalimat

input_baik: str = "bagus"
input_buruk: str = "jelek"
input_kalimat: str = "in adalah string untuk pengujian fungsi."

def test_prediksi_nbc():
    hasil_prediksi = prediksi_nbc(input_baik)
    assert isinstance(hasil_prediksi, float)

def test_prediksi_nbc_pos():
    hasil_prediksi = prediksi_nbc(input_baik)
    assert hasil_prediksi > 0

def test_prediksi_nbc_neg():
    hasil_prediksi = prediksi_nbc(input_buruk)
    assert hasil_prediksi < 0

def test_per_kata():
    hasil_prediksi = per_kata(input_kalimat)
    assert isinstance(hasil_prediksi, list)

def test_per_kalimat():
    hasil_prediksi = per_kalimat(input_kalimat)
    assert isinstance(hasil_prediksi, list)
