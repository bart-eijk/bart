import datetime
import argparse
from time import sleep

from pydub import AudioSegment

from config import Config

MILLIS = 1000

def pretty_print(millis_timestamp:int):
    return str(datetime.timedelta(milliseconds=millis_timestamp))

def process(config: Config):
    input = AudioSegment.from_file("input/" + config.input_file)
    input_duration_sec = input.duration_seconds
    print(f"Loaded input file [{config.input_file}] with a duration of [{input_duration_sec}] seconds")

    output = AudioSegment.empty()

    for s in range(0, int(input_duration_sec), config.segment_step_seconds):
        start_ts = s * MILLIS
        end_ts = MILLIS * (s + config.segment_length_seconds)

        for _ in range(config.repeat_segment):
            print(f"Adding segment: [{pretty_print(start_ts)}] - [{pretty_print(end_ts)}]")
            output += input[start_ts:end_ts]

            if config.pause_length_seconds != 0:
                pause = AudioSegment.silent(duration=MILLIS * config.pause_length_seconds)
                print(f"Adding pause of length [{pretty_print(pause.duration_seconds * MILLIS)}]")
                output += AudioSegment.silent(duration=MILLIS * config.pause_length_seconds)

    print("Exporting to output file, this can take some time for big audio files...")
    output.export("output/" + config.input_file, format="mp3")

    print(f"All done! Wrote output file [output/{config.input_file}] with length of [{pretty_print(output.duration_seconds * 1000)}]")



if __name__ == "__main__":
    doc = """
 ____   ____ ____  ______ 
|    \ /    |    \|      |
|  o  )  o  |  D  )      |
|     |     |    /|_|  |_|
|  O  |  _  |    \  |  |  
|     |  |  |  .  \ |  |  
|_____|__|__|__|\_| |__|  
                      

BART (Beyond Audio Replay Technology) aids transcribe tasks by taking a source audio file
and creating automatic repeated loops, allowing transcribers to listen to fragments twice 
with possible overlap.
    """

    parser = argparse.ArgumentParser(description=doc)
    parser.add_argument('--input', dest='input', type=str, required=True,
                        help='location of input file relative to directory `input/`')
    parser.add_argument('--segment-length', dest='segment_length', type=int, default=10,
                        help='length of segments in seconds')
    parser.add_argument('--segment-step', dest='segment_step', type=int, default=5,
                        help='step size in seconds (interval between two segments)')
    parser.add_argument('--pause-length', dest='pause_length', type=float, default=0.0,
                        help='pause (silence) between segments')
    parser.add_argument('--segment-repeat', dest='segment_repeat', type=int, default=1,
                        help='repeat count of each segment')

    args = parser.parse_args()

    config = Config.from_args(args)

    print(doc)
    sleep(5)
    process(config)