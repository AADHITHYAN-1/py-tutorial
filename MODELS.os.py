import os
a=os.getcwd()
print(a)

'''pathh for the new direcory'''
new_dir=os.path.join(a,"os modules")
os.mkdir(new_dir)
print(f"directory{new_dir}created")

'''rename'''
os.rename(new_dir,os.path.Join(A,"os moduls file"))
print("directory rename")
