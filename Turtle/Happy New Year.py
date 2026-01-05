import time
import sys
import random

# 🎉 Messages to show
msgs = [
    "✨🎊 H A P P Y  N E W  Y E A R  2 0 2 6 🎊✨",
    "🥂 May your 2026 be full of joy & success! ✨",
    "🌟 New Year, New Beginnings, New Wins! 💫",
    "🎆 Cheers to an awesome 2026 ahead! 🥳"
]

def animate_message(text, delay=0.07):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# 🎇 Animate all messages with random delay
for msg in msgs:
    animate_message(msg, random.uniform(0.04, 0.1))
    time.sleep(0.5)

print("\n🥳🎉 Wishing you all a Fantastic Year 2026! 🎉🥳")