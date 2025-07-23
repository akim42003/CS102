from cs101audio import *

coin = Audio()
coin.open_audio_file("coin.wav")

def get_sample_rate():
    samples = coin.get_sample_list()
    total_samples = len(samples)
    time = int(len(coin))
    rate = (total_samples/time)
    print(f"The sample rate is {rate} kHz")
    
def main():
    get_sample_rate()
    
main()

