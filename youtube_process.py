import subprocess
import os
import sys
import argparse


parser = argparse.ArgumentParser(description="Get count of all characters!")
parser.add_argument(
    "-p", "--path", action="store", dest="path", default='./resources/data/ar/eg/map', type=str, help="Path to map file",
)
args = parser.parse_args()
path = args.path

output = '/'.join(path.split('/')[:-1])

if not os.path.exists(output+'/wav'): os.mkdir(output+'/wav')

f = open(path, "r")

for line in f:
    audioFile = output+'/wav/' + str(line.split()[0]) + '.wav'
    youtubeID = line.split()[1]
    if os.path.exists(audioFile):
        print("Exist: ", audioFile)
        continue
    print("Processing: ", audioFile, youtubeID)
    subprocess.run(['youtube-dl', '-f', '[ext=mp4]', '--output', 'tmp.mp4', "--", str(youtubeID)],
                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    subprocess.run(['ffmpeg', '-i', 'tmp.mp4', 'tmp.wav'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    subprocess.run(['sox', 'tmp.wav', '-c', '1', str(audioFile), 'trim', '0', '720'], stdout=subprocess.PIPE,
                   stderr=subprocess.STDOUT)
    if os.path.exists("tmp.mp4"): os.remove("tmp.mp4")
    if os.path.exists("tmp.wav"): os.remove("tmp.wav")