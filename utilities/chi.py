def chi_squared(
        text, 
        expected_frequencies=[.082, .015, .028, .043, .127, .022, .020, .061, .070, .0015, .0077, .040, .024, .067, .075, .019, .00095, .060, .063, .091, .028, .0098, .024, .0015, .020, .00074], 
        letters="abcdefghijklmnopqrstuvwxyz"):
    
    chi_score = 0
    text_len = len(text)
    for i, l in enumerate(letters):
        expected_frequency = expected_frequencies[i]*text_len
        actual_frequency = text.count(l)
        chi_score += ((actual_frequency-expected_frequency)**2)/expected_frequency

    return chi_score