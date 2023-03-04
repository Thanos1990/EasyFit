from pathlib import Path

p1 = Path(r"C:\Users\thana\OneDrive\Documents\Udemy\Automation_Python\files_folders\ghi.txt")
#print(type(p1))

if not p1.exists():
    with open(p1,'w') as file:
        file.write("Content 3")

print(p1.name)

p2 = Path(r"C:\Users\thana\OneDrive\Documents\Udemy\Automation_Python\files_folders")
print(p2.iterdir())

for item in p2.iterdir():
    print(item)