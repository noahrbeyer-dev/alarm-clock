import os

files = sorted(f for f in os.listdir("songs") if f.lower().endswith(".mp3"))
with open("songs/songs.txt", "w", newline="\n") as out:
    out.write("\n".join(files) + "\n")
print(f"{len(files)} songs written")