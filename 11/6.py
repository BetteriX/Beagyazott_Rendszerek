#!/usr/bin/env python3

import pytesseract
import cv2


def main():
    image_path = "licence.jpeg"
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    options = "outputbase digits"
    text = pytesseract.image_to_string(image, config=options)
    print(text)


if __name__ == "__main__":
    main()
