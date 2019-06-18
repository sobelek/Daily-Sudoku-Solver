import cv2

template1 = cv2.imread('./digits/1.png', cv2.IMREAD_GRAYSCALE)
template2 = cv2.imread('./digits/2.png', cv2.IMREAD_GRAYSCALE)
template3 = cv2.imread('./digits/3.png', cv2.IMREAD_GRAYSCALE)
template4 = cv2.imread('./digits/4.png', cv2.IMREAD_GRAYSCALE)
template5 = cv2.imread('./digits/5.png', cv2.IMREAD_GRAYSCALE)
template6 = cv2.imread('./digits/6.png', cv2.IMREAD_GRAYSCALE)
template7 = cv2.imread('./digits/7.png', cv2.IMREAD_GRAYSCALE)
template8 = cv2.imread('./digits/8.png', cv2.IMREAD_GRAYSCALE)
template9 = cv2.imread('./digits/9.png', cv2.IMREAD_GRAYSCALE)
template1 = cv2.resize(template1, (90, 90))
template2 = cv2.resize(template2, (90, 90))
template3 = cv2.resize(template3, (90, 90))
template4 = cv2.resize(template4, (90, 90))
template5 = cv2.resize(template5, (90, 90))
template6 = cv2.resize(template6, (90, 90))
template7 = cv2.resize(template7, (90, 90))
template8 = cv2.resize(template8, (90, 90))
template9 = cv2.resize(template9, (90, 90))
templates = ['template1', 'template2', 'template3', 'template4', 'template5', 'template6', 'template7', 'template8', 'template9', ]


for i in range(81):
    temp = cv2.imread('./training_data/data' + str(i) + '.png')
    temp = cv2.resize(temp, (90, 90))
    cv2.imwrite('./training_data/data' + str(i) + '.png', temp)