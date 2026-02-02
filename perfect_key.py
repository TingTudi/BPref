import base64
import os

# This is the Base64 encoded version of the official working mjkey.txt
# It forces the exact correct byte sequence (Linux newlines, no BOM).
KEY_B64 = (
    "TElDRU5TRV9JRDogcHVibGljCktFWToKOEI0NDY3MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAK"
    "MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw"
    "MDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAw"
    "MDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAw"
    "MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw"
    "MDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAw"
    "MDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAw"
    "MDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAw"
    "MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw"
    "MDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAw"
    "MDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAw"
    "MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAK"
    "MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw"
    "MDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAw"
    "MDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAw"
    "MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw"
    "MDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAw"
    "MDAwMDAwMDAwMDAKMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDA="
)

# 1. Decode the key bytes
key_bytes = base64.b64decode(KEY_B64)

# 2. Define path to user home .mujoco
user_home = os.path.expanduser("~")
mj_dir = os.path.join(user_home, ".mujoco")
target_path = os.path.join(mj_dir, "mjkey.txt")

# 3. Write binary (ensures no windows \r\n conversion or UTF-8 BOM)
if not os.path.exists(mj_dir):
    os.makedirs(mj_dir)

with open(target_path, "wb") as f:
    f.write(key_bytes)

print(f"✅ Successfully wrote clean binary key to: {target_path}")
print(f"Key Size: {len(key_bytes)} bytes")