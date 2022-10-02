from sensi import read_log_likelihood, read_log_prior, read_stop_words, read_all_training

def test_read_likelihood():
    likelihood = read_log_likelihood()
    assert isinstance(likelihood, dict)

def test_read_prior():
    prior = read_log_prior()
    assert isinstance(prior, float)

def test_read_stop_words():
    prior = read_stop_words()
    assert isinstance(prior, set)

def test_read_training():
    prior = read_all_training()
    assert isinstance(prior, dict)
