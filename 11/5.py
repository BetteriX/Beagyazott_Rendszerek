#!/usr/bin/env python3

import pytesseract
import cv2


def main():
    image_path = "deik.jpg"
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(image)
    print(text)


if __name__ == "__main__":
    main()
