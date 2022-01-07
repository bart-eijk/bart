 ____   ____ ____  ______
|    \ /    |    \|      |
|  o  )  o  |  D  )      |
|     |     |    /|_|  |_|
|  O  |  _  |    \  |  |
|     |  |  |  .  \ |  |
|_____|__|__|__|\_| |__|

"Are you transcribing a conversation? BART can help!"

BART (Beyond Audio Replay Technology) aids transcribe tasks by taking a source audio file
and creating automatic repeated loops, allowing transcribers to listen to fragments multiple
times (with possible overlap between segments).

# Installation
Make sure to clone this repository and install Python dependencies using:
```bash
pip install -r requirements.txt
```

BART relies on [Pydub](https://github.com/jiaaro/pydub/) for processing audio.
Pydub needs ffmepg or libav to be available on your system.
Read [this](https://github.com/jiaaro/pydub/#dependencies) carefully.

## Installing ffmpeg on MacOS
On my macOS system, I did the following.

1. Download `ffmpeg` and `ffprobe` binaries from: https://evermeet.cx/ffmpeg/
2. Unarchive downloaded files and move them to your $PATH, e.g.:
```bash
sudo cp ffmpeg /usr/local/bin
sudo cp ffprobe /usr/local/bin
```
3. Double check they are in your $PATH:
```bash
which ffmpeg || echo "ffmpeg not found"
which ffprobe || echo "ffprobe not found"
```

# Usage
BART is very simple and expects all input files in the `input/` directory.

Overmore, BART is very naive. It always writes output files to the `output/` directory with exactly the same name as the input file. If the file exists, it will overwrite *without warning*.

BART is very chatty and will tell you when he adds a segment and when he adds a pause.

## Example
```bash
python main.py --input test.mp3 --segment-length 10 --pause-length 1.0 --segment-step 5 --segment-repeat 2
```

Usage:
```bash
python main.py -h
```