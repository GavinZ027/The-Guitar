# 导入 microbit 模块
from microbit import *

# 定义吉他音符的频率
F = 349
A = 440
C = 523

# 定义吉他弦的引脚
string1 = pin1
string2 = pin2
string3 = pin0

# 定义吉他弦的触摸感应
touch1 = pin1.is_touched()
touch2 = pin2.is_touched()
touch3 = pin0.is_touched()

# 定义吉他弦的音量
volume = 127

# 定义吉他弦的持续时间
duration = 500

# 定义吉他弦的播放函数
def play(string, note):
    # 如果触摸了弦，就播放对应的音符
    if string:
        # 用 PWM 信号生成音频输出
        speaker.write_analog(volume)
        # 设置音频输出的频率
        speaker.set_analog_period_microseconds(note)
        # 等待一定的时间
        sleep(duration)
        # 停止音频输出
        speaker.write_digital(0)

# 主循环
while True:
    # 播放第一根弦的音符 F
    play(touch1, F)
    # 播放第二根弦的音符 A
    play(touch2, A)
    # 播放第三根弦的音符 C
    play(touch3, C)
