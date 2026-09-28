"""
Command Line Interface for chrono-lingua.
"""

import sys
import argparse
import json
from src.parser import ChronoParser

def main():
    parser = argparse.ArgumentParser(description="Chrono-Lingua Text Parser & Transformation Utility")
    parser.add_argument("text", type=str, help="The input text to transform")
    parser.add_argument(
        "--mode", 
        type=str, 
        default="standard", 
        choices=["standard", "uppercase", "reverse", "token_map", "stats"],
        help="Transformation mode to apply"
    )
    parser.add_argument(
        "--format",
        type=str,
        default="text",
        choices=["text", "json"],
        help="Output format (human-readable text or raw JSON)"
    )

    args = parser.parse_args()
    
    chrono = ChronoParser()
    result = chrono.transform(args.text, mode=args.mode)
    
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print("\n--- Chrono-Lingua Result ---")
        for key, value in result.items():
            print(f"{key.capitalize()}: {value}")
        print("-" * 28)

if __name__ == "__main__":
    main()
