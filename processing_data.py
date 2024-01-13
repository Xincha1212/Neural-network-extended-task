train_path = 'NewsData/train.txt'
dev_path = 'NewsData/dev.txt'

i = 0
label_dict = {}

with open(train_path, 'r', encoding='utf-8') as f:
    train_lines = f.readlines()
    f.close()

for line in train_lines:
    label = line.split('\t')[1].replace('\n', '')
    if label not in label_dict:
        label_dict[label] = i
        i += 1

with open('NewsData/train.txt', 'w', encoding='utf-8') as f:
    for line in train_lines[0:int(len(train_lines)*0.8)]:
        title = line.split('\t')[0]
        label = line.split('\t')[1].replace('\n', '')
        f.write(title + '\t' + str(label_dict[label]) + '\n')
    f.close()

with open('NewsData/test.txt', 'w', encoding='utf-8') as f:
    for line in train_lines[int(len(train_lines)*0.8):]:
        title = line.split('\t')[0]
        label = line.split('\t')[1].replace('\n', '')
        f.write(title + '\t' + str(label_dict[label]) + '\n')
    f.close()

with open(dev_path, 'r', encoding='utf-8') as f:
    dev_lines = f.readlines()
    f.close()

with open('NewsData/dev.txt', 'w', encoding='utf-8') as f:
    for line in dev_lines:
        title = line.split('\t')[0]
        label = line.split('\t')[1].replace('\n', '')
        f.write(title + '\t' + str(label_dict[label]) + '\n')
    f.close()

label_list = list(label_dict)
with open('NewsData/class.txt', 'w', encoding='utf-8') as f:
    for label in label_list:
        f.write(label + '\n')
    f.close()
