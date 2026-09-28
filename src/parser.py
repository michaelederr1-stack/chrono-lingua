"""
Chrono-Lingua Core Parser & Analytics
"""

import re

class ChronoParser:
    def transform(self, text: str, mode: str = "standard") -> dict:
        if mode == "uppercase":
            transformed = text.upper()
        elif mode == "reverse":
            transformed = text[::-1]
        elif mode == "token_map":
            transformed = f"TOKENS[{len(text.split())} words]"
        elif mode == "stats":
            words = text.split()
            sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
            chars_no_spaces = len(text.replace(" ", ""))
            avg_word_len = sum(len(w) for w in words) / len(words) if words else 0.0
            read_time_sec = (len(words) / 200.0) * 60  # Assuming ~200 WPM reading speed
            
            transformed = {
                "character_count": len(text),
                "characters_no_spaces": chars_no_spaces,
                "word_count": len(words),
                "sentence_count": len(sentences),
                "average_word_length": round(avg_word_len, 2),
                "estimated_reading_time_seconds": round(read_time_sec, 1)
            }
        else:
            transformed = text
            
        return {
            "original": text,
            "mode": mode,
            "result": transformed
        }
