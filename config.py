from argparse import Namespace
from dataclasses import dataclass


@dataclass
class Config:
    input_file:str
    segment_length_seconds:int
    pause_length_seconds:float
    segment_step_seconds:int
    repeat_segment:int

    @staticmethod
    def from_args(args:Namespace):
        return Config(
            input_file=args.input,
            segment_length_seconds=args.segment_length,
            pause_length_seconds=args.pause_length,
            segment_step_seconds=args.segment_step,
            repeat_segment=args.segment_repeat,
        )