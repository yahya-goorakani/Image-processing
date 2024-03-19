import cv2
import numpy as np
import utils

curveList = []
avgVal = 10


def get_lane_curve(img, display=2):
    img_copy = img.copy()
    img_result = img.copy()

    # Step 1: Thresholding
    img_thres = utils.thresholding(img)

    # Step 2: Perspective Transformation
    hT, wT, c = img.shape
    points = utils.val_trackbars()
    img_warp = utils.warp_img(img_thres, points, wT, hT)
    img_warp_points = utils.draw_points(img_copy, points)

    # Step 3: Histogram Analysis
    middle_point, img_hist = utils.get_histogram(img_warp, display=True, minPer=0.5, region=4)
    curve_average_point, img_hist = utils.get_histogram(img_warp, display=True, minPer=0.9)
    curve_raw = curve_average_point - middle_point

    # Step 4: Smoothing the Curve
    curveList.append(curve_raw)
    if len(curveList) > avgVal:
        curveList.pop(0)
    curve = int(sum(curveList) / len(curveList))

    # Step 5: Display Lane Detection
    if display != 0:
        img_inv_warp = utils.warp_img(img_warp, points, wT, hT, inv=True)
        img_inv_warp = cv2.cvtColor(img_inv_warp, cv2.COLOR_GRAY2BGR)
        img_inv_warp[0:hT // 3, 0:wT] = 0, 0, 0
        img_lane_color = np.zeros_like(img)
        img_lane_color[:] = 0, 255, 0
        img_lane_color = cv2.bitwise_and(img_inv_warp, img_lane_color)
        img_result = cv2.addWeighted(img_result, 1, img_lane_color, 1, 0)
        midY = 450
        cv2.putText(img_result, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
        cv2.line(img_result, (wT // 2, midY), (wT // 2 + (curve * 3), midY), (255, 0, 255), 5)
        cv2.line(img_result, ((wT // 2 + (curve * 3)), midY - 25), (wT // 2 + (curve * 3), midY + 25), (0, 255, 0),
                 5)
        for x in range(-30, 30):
            w = wT // 20
            cv2.line(img_result, (w * x + int(curve // 50), midY - 10),
                     (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)

    # Displaying the Results
    if display == 2:
        img_stacked = utils.stack_images(0.7, ([img, img_warp_points, img_warp],
                                                [img_hist, img_lane_color, img_result]))
        cv2.imshow('ImageStack', img_stacked)
    elif display == 1:
        cv2.imshow('Result', img_result)

    # Normalizing the Curve
    curve = curve / 100
    if curve > 1:
        curve == 1
    if curve < -1:
        curve == -1

    return curve


if __name__ == '__main__':
    cap = cv2.VideoCapture('lane2.mp4')
    initial_trackbar_vals = [102, 80, 20, 214]
    utils.initialize_trackbars(initial_trackbar_vals)
    frame_counter = 0

    while True:
        frame_counter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frame_counter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frame_counter = 0

        success, img = cap.read()
        img = cv2.resize(img, (480, 240))
        curve = get_lane_curve(img, display=2)
        print(curve)
        cv2.waitKey(1)


