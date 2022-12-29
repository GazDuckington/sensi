from sensi import rem_stop, normalisasi, freqs

kata_tidak_baku: str = "berjalan terpengaruh"
list_kata_mentah: list = ["tahu", "waduh", "jelek", "supaya", "bagus"]
expected_list: list = ["jelek", "bagus"]


def test_rem_stop():
    hasil_rem_stop: list = rem_stop(list_kata_mentah)
    assert hasil_rem_stop == expected_list


def test_normalisasi():
    hasil_normalisasi = normalisasi(kata_tidak_baku)
    assert hasil_normalisasi == ["jalan", "pengaruh"]


def test_freqs():
    hasil_freqs = freqs(kata_tidak_baku)
    assert isinstance(hasil_freqs, list)
