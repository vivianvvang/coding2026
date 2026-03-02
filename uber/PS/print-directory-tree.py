def directory_tree(input):
    lines = input.split('\n')
    for line in lines:
        if not line.strip():
            continue
        file = line.lstrip('\t')
        level = len(line) - len(file)

        print("  " * level + file)

print("test case")
directory_tree("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
print("test case")
directory_tree("root\n\tfolder1\n\t\tfile1\n\t\tfile2\n\tfolder2\n")
print("test case")
directory_tree("home\n\tuser\n\t\tproject\n\t\t\tdoc.txt\n\t\timages\n")
print("test case")
directory_tree("app\n\tbin\n\t\tcmd.exe")
print("test case")
directory_tree("main\n\tsrc\n\t\tmodule.cpp\n\tinclude\n\t\tmodule.h")


