import os
path = "C:\\Python\\AtCoder"


def makefiles(name, times):
    times = str(times)
    if times is not None:
        makefolder_path = path + "\\" + name + "\\" + times
    else:
        makefolder_path = path + "\\" + name
    print(makefolder_path)
    try:
        os.mkdir(makefolder_path)
        if times is None:
            for i in range(6):
                # file A~F
                text = chr(i + 65)
                makefiles_path = makefolder_path + "\\" + text + ".py "
                print(makefiles_path)
                try:
                    with open(makefiles_path, mode='x') as f:
                        f.write("#" + text)
                except FileExistsError:
                    print('このファイルは作成することができません。')
        elif (name == "ABC" and int(times) < 125) or name == "ARC":
            # file A~D
            for i in range(4):
                text = chr(i + 65)
                makefiles_path = makefolder_path + "\\" + times + text + ".py"
                print(makefiles_path)
                try:
                    with open(makefiles_path, mode='x') as f:
                        f.write("#" + text)
                except FileExistsError:
                    print('このファイルは作成することができません。')
        else:
            for i in range(6):
                # file A~F
                text = chr(i + 65)
                makefiles_path = makefolder_path + "\\" + times + text + ".py"
                print(makefiles_path)
                try:
                    with open(makefiles_path, mode='x') as f:
                        f.write("#" + text)
                except FileExistsError:
                    print('このファイルは作成することができません。')
    except FileExistsError:
        print('このフォルダは作成することができません。')


contest = list(input('1:コンテスト名 (2:コンテスト数)').split())
contest[0] = contest[0].upper()
print(contest)
if contest[0] == 'ABC' or contest[0] == 'ARC' or contest[0] == 'AGC':
    print("1")
    # contest[1] = int(contest[1])
    # for i in range(n):
    makefiles(contest[0], int(contest[1]))
else:
    print("2")
    makefiles(contest[0], times=None)
print('Finish')
