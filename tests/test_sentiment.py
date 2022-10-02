import pandas as pd
from sensi import hitung_likelihood, hitung_prior, kamus_freq, predict_nbc, uji_akurasi, read_log_prior, read_log_likelihood 

data_unit_test = [['text1', 0], ['text2', 0], ['text3', 1]]
df_unit_test = pd.DataFrame(data_unit_test, columns=['text', 'label'])
test_kata = df_unit_test['text'].tolist()
test_label = df_unit_test['label'].tolist()
kata = "baik"

frek = kamus_freq(test_kata, test_label)
prior = hitung_prior(frek, df_unit_test['label'])
likelihood = hitung_likelihood(frek)
hasil_test = uji_akurasi(test_kata, test_label, prior, likelihood)

def test_kamus_freq():
    assert isinstance(frek, dict)

def test_likelihood():
    assert isinstance(likelihood, dict)

def test_prior():
    assert isinstance(prior, float)

def test_akurasi():
    assert isinstance(hasil_test, str)

def test_predict_nbc():
    hasil = predict_nbc(kata, prior, likelihood)
    assert isinstance(hasil, float)
