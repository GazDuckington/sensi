<div align=center><b>Framework analisis sentiment teks Bahasa Indonesia, menggunakan Klasifikasi Naive-Bayes</b></div>

# Dependensi
- sastrawi 
- nltk
- numpy
- pandas
- sqlalchemy

# Instalasai
Belum ada setup.py, install secara manual.
1. _copy/clone_ _repository_ kedalam directory proyek anda
```bash
git clone https://github.com/GazDuckington/nbc-sentimen.git
```
1. Ikuti contoh-contoh penggunaan.

# Penggunaan
- Contoh penerapan dapat dilihat pada directory 'apis' pada repository [flask-sk](https://github.com/GazDuckington/flask-sk)

- Contoh sederhana:
  ```python
  from database.query import readLoglikelihood, readLogprior
  from resources.sentiment import predict_nbc
  
  logprior = readLogprior()
  loglikelihood = readLoglikelihood()
  text = "contoh text yang ingin di analisis."
  
  print(predict_nbc(text, logprior, loglikelihood))
  ```
- Baca ```resources/predictor.py``` untuk berbagai contoh lainnya.

# LICENSE
[MIT](LICENSE)
