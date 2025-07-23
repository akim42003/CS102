from cs101audio import *

# sound = Audio()
# sound.open_audio_file("coin.wav")
# sound.play()

coin = Audio()
coin.open_audio_file("coin.wav")
# coin.play()


powerup = Audio()
powerup.open_audio_file("powerup.wav")
# powerup.play()

# coin *= 5
# volume

# new_sound = coin + powerup
# plays coin, then powerup

# coin += powerup
# plays coin, then powerup

# print(len(coin))
# prints milliseconds of time the coin plays

# coin.change_speed(3)
# speed of change between coin and powerup

# coin.fade(500, 500)
# how long the fade lasts

# coin = coin[200:]
# starts at 200

# coin = coin[:len(coin) // 2]
# the length of sound divided by 2

# coin.overlay(powerup)
# plays at the same time as coin

sound = Audio()
sound.open_audio_file("DireOnTheRocks.wav")

# sound.overlay(coin, 5000)

# sound.overlay(powerup, 10000)


# seconds = int(len(sound))//1000+1
# for second in range(0, seconds):
#     print(second)
#     
#     chunk = sound[second*1000:(second+1)*1000]
#     chunk.play()
    
# sound.play()

# powerup = powerup[10000:

# seconds = int(len(sound))//1000+1
# for second in range(0, seconds):
#     print(second)
#     
#     chunk = sound[second*1000:(second+1)*1000]
#     chunk.change_speed(second+1)
#     chunk.play()

# seconds = int(len(sound))//1000+1
# remix = Audio()
# for second in range(0, seconds):
#     chunk = sound[second*1000:(second+1)*1000]
#     chunk.change_speed(second/500+1)
#     chunk.apply_gain(-2second)
#     
#     remix += chunk
# seconds = int(len(sound))//1000+1
# remix = Audio()
# switch = 0
# for second in range(0, seconds):
#     switch+=1
#     chunk = sound[second*1000:(second+1)*1000]
#     if switch % 5 == 0:  
#         chunk.overlay(coin)
#     if switch %  10 == 0:
#         chunk.overlay(powerup)
#     
#     remix += chunk
#     
# # remix.play()
# seconds = int(len(sound))//1000+1
# remix = Audio()
# for second in range(1, seconds):
#     if (second) % 4 == 1:
#         chunk = sound[second*1000:(second+1)*1000] 
#         remix += chunk
#     
# remix.play()
    
b_flat = generate_music_note("Bb4", 20000, "Sine")
b_flat.play()

