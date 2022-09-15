<div align="center">Sensi, analisis sentimen bahasa Indonesia menggunakan klasifikasi Naive-Bayes.</div>

# Instalasai
Belum ada setup.py, install secara manual.
1. _Install_ paket
```bash
pip install sensi
```
1. Ikuti contoh-contoh penggunaan.

# Penggunaan
- Contoh penerapan dapat dilihat pada directory 'apis' pada repository [flask-sk](https://github.com/GazDuckington/flask-sk)

- Contoh sederhana:
  ```python
  from sensi.database.query import readLoglikelihood, readLogprior
  from sensi.resources.sentiment import predict_nbc
  
  logprior = readLogprior()
  loglikelihood = readLoglikelihood()
  text = "contoh text yang ingin di analisis."
  
  print(predict_nbc(text, logprior, loglikelihood))
  ```
  
- Baca ```resources/predictor.py``` untuk berbagai contoh lainnya.

# LICENSE
[MIT](LICENSE)
