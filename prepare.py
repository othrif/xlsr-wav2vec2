import operator
import csv
import argparse
import re
from datasets import load_dataset

parser = argparse.ArgumentParser(description="Get count of all characters!")
parser.add_argument(
    "-p", "--path", action="store", dest="path", default='./resources/models', type=str, help="Destination path to save file",
)
args = parser.parse_args()
path = args.path

def remove_special_characters(batch):
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower() + " "
    return batch


count_char = {}
chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“]'

common_voice_train = load_dataset("common_voice", "ar", split="train+validation")
common_voice_test = load_dataset("common_voice", "ar", split="test")

for d in [common_voice_test, common_voice_train]:
    for x in d:
        for c in x['sentence'].lower():
            if c in count_char.keys():
                count_char[c] += 1
            else:
                count_char[c] = 1
sorted_char = sorted(count_char.items(), key=operator.itemgetter(1), reverse=True)
with open(path+'/letters.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for x in sorted_char:
        writer.writerow(x)


print('All characters and their count:')
for x in sorted_char:
    print(x)