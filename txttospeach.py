from gtts import gTTS

text = gTTS("hello world")
text.save("hello.mp3")