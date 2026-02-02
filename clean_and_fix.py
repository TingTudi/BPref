import os
import shutil

# 1. Define paths
current_dir = os.getcwd()
user_dir = os.path.expanduser("~")
mj_dir = os.path.join(user_dir, ".mujoco")
bin_dir = os.path.join(mj_dir, "mujoco200", "bin")

paths_to_check = [
    os.path.join(current_dir, "mjkey.txt"),
    os.path.join(mj_dir, "mjkey.txt"),
    os.path.join(bin_dir, "mjkey.txt")
]

# 2. The Clean Key Content (Strict Binary)
# We use byte strings (b"") to ensure Python does absolutely no formatting magic.
key_content = (
    b"LICENSE_ID: public\n"
    b"KEY:\n"
    b"8B446700000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000\n"
    b"00000000000000000000000000000000"
)

# 3. Execution
print("--- STARTING CLEANUP ---")

# Delete existing keys
for p in paths_to_check:
    if os.path.exists(p):
        try:
            os.remove(p)
            print(f"Deleted old key at: {p}")
        except Exception as e:
            print(f"Could not delete {p}: {e}")

# Create directories if needed
if not os.path.exists(mj_dir):
    os.makedirs(mj_dir)
if not os.path.exists(bin_dir):
    try:
        os.makedirs(bin_dir)
    except:
        print("Could not create bin dir (might not exist yet), skipping bin copy.")

# Write New Keys
# 1. To ~/.mujoco/mjkey.txt
with open(os.path.join(mj_dir, "mjkey.txt"), "wb") as f:
    f.write(key_content)
print(f"Written clean key to: {os.path.join(mj_dir, 'mjkey.txt')}")

# 2. To ~/.mujoco/mujoco200/bin/mjkey.txt (If bin exists)
if os.path.exists(bin_dir):
    bin_key_path = os.path.join(bin_dir, "mjkey.txt")
    with open(bin_key_path, "wb") as f:
        f.write(key_content)
    print(f"Written clean key to: {bin_key_path}")

print("--- DONE ---")
print("Please run the training command now.")