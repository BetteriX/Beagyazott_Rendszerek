#!/usr/bin/env python3


from imutils.video import VideoStream
import imutils
import argparse
import time
from pyzbar import pyzbar
import cv2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-w", "--width", type=int, default=400, help="Width of the window")
    args = vars(ap.parse_args())

    vs = VideoStream().start()
    time.sleep(2.0)

    while True:
        # acquire a frame from the video stream and resize it
        # according to the window size
        frame = vs.read()
        frame = imutils.resize(frame, width=args["width"])

        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            # draw bounding box around the detected object
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # the barcode data is a bytes object so if we want to draw it on
            # our output image we need to convert it to a string first
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type

            # draw the barcode description and type on the image
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(
                frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2
            )

        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # cleanup – close window(s) and stop video stream
    cv2.destroyAllWindows()
    vs.stop()


if __name__ == "__main__":
    main()
