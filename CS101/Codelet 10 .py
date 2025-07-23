from cs101audio import *

coin = Audio()
coin.open_audio_file("coin.wav")

sample_len = coin.get_sample_rate()

print("sample_len")