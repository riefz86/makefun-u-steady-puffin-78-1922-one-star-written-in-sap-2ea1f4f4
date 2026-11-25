"""One Star, Written in Sap.

Writes a single one-line 1-star review from a houseplant about its
human owner to /output/entry.txt: a real review with a grievance and a
reason for the single star, in the plant's own voice.
"""

import os

LINE = "One star. I spent three years turning his sunlight into oxygen and he thanked me by watering me with leftover iced coffee and naming me Planty. Would not photosynthesize here again — signed, in sap."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
