# Really awful scrip because i can't import multiple images
import os

IMGS_DIR =  "./src/imgs"
RELATIVE_DIR = "../imgs"
OUTPUT_FILE = "./src/pages/Main.js"

lines = []
img_vals = sorted(["img_" + img[:-4] for img in os.listdir(IMGS_DIR)])
print("[" + ", ".join(img_vals) + "]")
# img_paths = sorted(["import img_" + file[:-4] + " from \"" + os.path.join(RELATIVE_DIR, file) + "\";\n" for file in os.listdir(IMGS_DIR)])
# for i in img_paths:
#     if ".png" in i:
#         lines.append(i)
#         print(i)


# with open(OUTPUT_FILE, "r") as f:
#     file_lines = f.readlines()

# with open(OUTPUT_FILE,  "w") as f:
#     f.write(file_lines[0])

#     for line in lines:
#         f.write(line)

#     for file_line in file_lines[1:]:
#         f.write(file_line)