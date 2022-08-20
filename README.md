## Dependensi

```python
sastrawi nltk numpy pandas sqlalchemy
```

## Instalasai
Belum ada setup.py, install secara manual.
1. copy isi repository kedalam directory proyek anda
1. gunakan fungsi-fungsi yang diinginkan dengan meng-impor fungsi-2 tsb.

## Contoh
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
baca **resources/predictor.py** untuk berbagai contoh lainnya.
