#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import cv2

app = Flask(__name__)


@app.route('/verifypic', methods=['GET'])
def verifypic():
    path = request.args['path']
    print('path:', path)
    img = cv2.imread(path)
    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(GrayImage, (5, 5), 0)  # 高斯滤波
    ret, thresh3 = cv2.threshold(blurred, 165, 255, cv2.THRESH_BINARY)
    cv2.imwrite('E:\\jxfilterpic\\test.jpg', thresh3)
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
