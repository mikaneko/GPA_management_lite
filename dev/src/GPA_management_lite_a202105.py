# seu-gpa-calculator
# version a202105

# 平均学分绩点=（学生所属专业指导性教学计划中规定所学的必修课、限选课（成绩以百分制或五级记分制记载）的学分数*学分绩点之和）/规定时间内所学必修课、限选课的学分数之和

import os
import json
import time


def print_hi():
    print('GPA_management_lite')
    print('   atarashichiaki@hotmail.com')
    print('   chiaki@seu.edu.cn')
    time.sleep(1)

def gettimestr():
    return time.strftime('%Y%m%d%H%M%S')


def make_dir():
    if not os.path.exists('./seu_grade_data'):
        os.mkdir('./seu_grade_data')


def head_of_descriptor():
    print('Select "score list"')
    print('=' * 40)
    print('uid\tname\tnote\tmapto')


def bottom_of_descriptor():
    print('')
    print('=' * 40)
    print('0\tCreate a score list')
    print('-1\tDelete a score list')


def head_of_lesson(name):
    print('Score List: ' + name)
    print('=' * 40)
    print('uid\tname\ttype\tcredit\tscore')


def bottom_of_lesson():
    print('')
    print('=' * 40)
    print('0\tCreate a lesson')
    print('-1\tDelete a lesson')
    print('-2\tBACK TO LIST PAGE')


def load_descriptor():
    dat_list = []
    try:
        with open('./seu_grade_data/descriptor.json', 'r') as f:
            dat_list = json.loads(f.readline())
            f.close()
        return dat_list
    except:
        with open('./seu_grade_data/descriptor.json', 'w') as f:
            f.write('[]\n')
            f.close()
        with open('./seu_grade_data/descriptor.json', 'r') as f:
            dat_list = json.loads(f.readline())
            f.close()
        return dat_list


def load_lesson(filename):
    dat_list = []
    try:
        with open('./seu_grade_data/' + filename + '.json', 'r') as f:
            dat_list = json.loads(f.readline())
            f.close()
        return dat_list
    except:
        with open('./seu_grade_data/' + filename + '.json', 'w') as f:
            f.write('[]\n')
            f.close()
        return dat_list


def show_descriptor(a_list):
    for line in a_list:
        buffer = ''
        buffer += (str(line['uid']) + '\t')
        buffer += (line['name'] + '\t')
        buffer += (line['note'] + '\t')
        buffer += (line['mapto'] + '\t')
        print(buffer)


def show_lesson(a_list):
    for line in a_list:
        buffer = ''
        buffer += (str(line['uid']) + '\t')
        buffer += (line['name'] + '\t')
        buffer += (line['type'] + '\t')
        buffer += (str(line['credit']) + '\t')
        buffer += (str(line['score']) + '\t')
        print(buffer)


def descriptor_add():
    with open('./seu_grade_data/descriptor.json', 'r') as f:
        list_old = json.loads(f.readline())
        uid = int(len(list_old) + 1)
        name = input('>>>INPUT: name: ')
        note = input('>>>INPUT: note: ')
        mapto = gettimestr()
        dict_new = {'uid': uid,
                    'name': name,
                    'note': note,
                    "mapto": mapto}
        list_old.append(dict_new)
        list_new_format = json.dumps(list_old)
        f.close()
    with open('./seu_grade_data/descriptor.json', 'w') as f:
        f.write(list_new_format)
        f.close()
    with open('./seu_grade_data/' + mapto + '.json', 'w') as f:
        f.close()


def descriptor_del():
    uid_to_del = int(input('>>>INPUT: uid to be deleted:'))
    with open('./seu_grade_data/descriptor.json', 'r') as f:
        list_old = json.loads(f.readline())
        filename = list_old[uid_to_del - 1]['mapto']
        list_old.pop(uid_to_del - 1)
        while uid_to_del - 1 < len(list_old):
            list_old[uid_to_del - 1]['uid'] -= 1
            uid_to_del += 1
        list_new_format = json.dumps(list_old)
        f.close()
    with open('./seu_grade_data/descriptor.json', 'w') as f:
        f.write(list_new_format)
        f.close()
    try:
        os.remove('./seu_grade_data/' + filename + '.json')
    except:
        print('Warning! No file! ')


def lesson_add(filename):
    with open('./seu_grade_data/' + filename + '.json', 'r') as f:
        list_old = json.loads(f.readline())
        uid = int(len(list_old) + 1)
        name = input('>>>INPUT: name: ')
        print('TIP: only can type "BiXiu","XuanXiu","XianXuan,"NO". ')
        type = input('>>>INPUT: type: ')
        credit = float(input('>>>INPUT: credit: '))
        score = float(input('>>>INPUT: score: '))
        dict_new = {'uid': uid,
                    'name': name,
                    'type': type,
                    'credit': credit,
                    'score': score}
        list_old.append(dict_new)
        list_new_format = json.dumps(list_old)
        f.close()
    with open('./seu_grade_data/' + filename + '.json', 'w') as f:
        f.write(list_new_format)
        f.close()


def lesson_del(filename):
    uid_to_del = int(input('>>>INPUT: uid to be deleted:'))
    with open('./seu_grade_data/' + filename + '.json', 'r') as f:
        list_old = json.loads(f.readline())
        list_old.pop(uid_to_del - 1)
        while uid_to_del - 1 < len(list_old):
            list_old[uid_to_del - 1]['uid'] -= 1
            uid_to_del += 1
        list_new_format = json.dumps(list_old)
        f.close()
    with open('./seu_grade_data/' + filename + '.json', 'w') as f:
        f.write(list_new_format)
        f.close()


def loop_lesson(filename, name):
    while True:
        os.system("cls")
        time.sleep(0.2)
        head_of_lesson(name)
        lesson = load_lesson(filename)
        show_lesson(lesson)
        show_gpa_info(lesson)
        bottom_of_lesson()
        op2_code = input('>>>INPUT: select: ')
        if op2_code == '0':
            lesson_add(filename)
            continue
        if op2_code == '-1':
            lesson_del(filename)
            continue
        if op2_code == '-2':
            break
        print('Wrong operation code! (2)')


def loop_descriptor():
    while True:
        os.system("cls")
        time.sleep(0.2)
        head_of_descriptor()
        descriptor = load_descriptor()
        show_descriptor(descriptor)
        bottom_of_descriptor()
        op1_code = input('>>>INPUT: select: ')
        if op1_code == '0':
            descriptor_add()
            continue
        if op1_code == '-1':
            descriptor_del()
            continue
        try:
            loop_lesson(descriptor[int(op1_code) - 1]['mapto'], descriptor[int(op1_code) - 1]['name'])
        except Exception as e:
            print(e)
            print('Wrong operation code! (1)')


def cal_credit(a_list):
    credit = 0
    for line in a_list:
        if line['type'] == 'BiXiu':
            credit += line['credit']
    return credit

def cal_all_credit(a_list):
    credit = 0
    for line in a_list:
        credit += line['credit']
    return credit


def cal_gpa(a_list):
    sum_credit = cal_credit(a_list)
    upper_credit = 0
    for line in a_list:
        if line['type'] == 'BiXiu':
            if line['score'] >= 96:
                level = 4.8
            elif line['score'] >= 93:
                level = 4.5
            elif line['score'] >= 90:
                level = 4.0
            elif line['score'] >= 86:
                level = 3.8
            elif line['score'] >= 83:
                level = 3.5
            elif line['score'] >= 80:
                level = 3.0
            elif line['score'] >= 76:
                level = 2.8
            elif line['score'] >= 73:
                level = 2.5
            elif line['score'] >= 70:
                level = 2.0
            elif line['score'] >= 66:
                level = 1.8
            elif line['score'] >= 63:
                level = 1.5
            elif line['score'] >= 60:
                level = 1.0
            else:
                level = 0.0
            upper_credit += (line['credit'] * level)
    if sum_credit == 0:
        return 0
    return upper_credit / sum_credit


def show_gpa_info(alist):
    print('')
    print('Credit sum: '+str(cal_all_credit(alist)))
    print('Credit counted in "BiXiu"：' + str(cal_credit(alist)))
    print('4.8 GPA: ' + str(cal_gpa(alist)))


if __name__ == '__main__':
    print_hi()
    make_dir()
    loop_descriptor()
