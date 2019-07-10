
# coding: utf-8

# 예제 내용
# * PaintEvent를 사용하여 실시간으로 값 변경하기
# * MouseEvent를 사용하여 마우스 값 가져오기

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QGraphicsOpacityEffect

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        # 마우스 좌표 저장용 변수
        self.mouse_x = 0
        self.mouse_y = 0

        self.lb = QLabel(self)

        self.properties_list = (
            "width", "height", "x", "y", "geometry",
            "maximumHeight", "maximumWidth", "maximumSize", "minimumSize", "minimumWidth",
            "size", "windowFilePath", "windowTitle",
            "underMouse"
        )  # 출력할 property 이름

        #add widget
        self.w1 = QWidget(parent=self, flags=Qt.Widget)
        self.w3 = QWidget(parent=self, flags=Qt.Widget)
        self.w2 = QWidget(parent=self, flags=Qt.Widget)

        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Hello World")
        self.setGeometry(100, 100, 640, 480)  # 창 위치, 크기 설정
        self.setMouseTracking(True)  # 마우스 움직임을 캐치

        # QLabel 인스턴스 생성
        # 인자값으로 parent인 self 지정
        # QLabel(str, parent), QLabel(parent) 등으로 줄 수 있음
        self.lb.setStyleSheet("background-color: yellow")  # 라벨위젯과의 구분을 위한 색
        self.lb.setMouseTracking(True)  # False 값일 경우 Label 위젯에서는 mouse 이벤트가 발생하지 않는다.
        msg = self.get_properties_value(self.properties_list)  # property 이름과 값을 돌려주는 함수 호출
        self.lb.setText(msg)  # Label에 텍스트 설정

        # 맨 아래 놓이게 될 위젯
        # 투명도를 설정하지 않음
        self.w1.setGeometry(10, 10, 100, 100)
        self.w1.setStyleSheet("background-color: yellow")

        # 중간에 놓이게 될 위젯
        # 투명도를 설정하지 않음
        self.w3.setGeometry(40, 40, 100, 100)
        self.w3.setStyleSheet("background-color: pink")

        # 가장 위에 놓이게 될 위젯
        self.w2.setGeometry(70, 70, 100, 100)
        opacity_effect = QGraphicsOpacityEffect(self.w2)
        opacity_effect.setOpacity(0.3)
        self.w2.setGraphicsEffect(opacity_effect)
        self.w2.setStyleSheet("background-color: red")

    def get_properties_value(self, properties):
        """
        인자 값으로 property의 이름을 담은 시퀀스 자료형
        property를 차례로 호출하며 이름과 값의 문자열 생성
        :param properties list or tuple
        :return str
        """
        msg = []
        for p in properties:
            if not hasattr(self, p):
                continue
            value = getattr(self, p)()  # == self.width(), self.x()
            msg.append("{:>20s} : {:<30s}".format(p, str(value)))
        msg.append("{:>20s} : {:<30s}".format("mouse_x", str(self.mouse_x)))
        msg.append("{:>20s} : {:<30s}".format("mouse_y", str(self.mouse_y)))
        msg = "\n".join(msg)
        return msg

    def mouseMoveEvent(self, QMouseEvent):
        """
        위젯 안에서의 마우스 움직임이 일어날 때 호출
        :param QMouseEvent:
        :return:
        """        
        self.mouse_x = QMouseEvent.x()
        self.mouse_y = QMouseEvent.y()
        self.update()

    def moveEvent(self, QMoveEvent):
        """
        창이 이동했을 경우(이동 중 아님.) 호출
        :param QMoveEvent:
        :return:
        """
        self.update()

    def paintEvent(self, QPaintEvent):
        """
        창을 다시 그려야 할 때 호출
        """
        msg = self.get_properties_value(self.properties_list)
        self.lb.setText(msg)  # Label에 텍스트 설정


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())



# # 털과 날개가 있는지 없는지에 따라, 포유류인지 조류인지 분류하는 신경망 모델을 만들어봅니다.
# import tensorflow as tf
# import numpy as np

# # [털, 날개]
# x_data = np.array(
#     [[0, 0], [1, 0], [1, 1], [0, 0], [0, 0], [0, 1]])

# # [기타, 포유류, 조류]
# # 다음과 같은 형식을 one-hot 형식의 데이터라고 합니다.
# y_data = np.array([
#     [1, 0, 0],  # 기타
#     [0, 1, 0],  # 포유류
#     [0, 0, 1],  # 조류
#     [1, 0, 0],  # 기타
#     [1, 0, 0],  # 기타
#     [0, 0, 1]   # 조류
# ])

# #########
# # 신경망 모델 구성
# ######
# X = tf.placeholder(tf.float32)
# Y = tf.placeholder(tf.float32)

# # 신경망은 2차원으로 [입력층(특성), 출력층(레이블)] -> [2, 3] 으로 정합니다.
# W = tf.Variable(tf.random_uniform([2, 3], -1., 1.))

# # 편향을 각각 각 레이어의 아웃풋 갯수로 설정합니다.
# # 편향은 아웃풋의 갯수, 즉 최종 결과값의 분류 갯수인 3으로 설정합니다.
# b = tf.Variable(tf.zeros([3]))

# # 신경망에 가중치 W과 편향 b을 적용합니다
# L = tf.add(tf.matmul(X, W), b)
# # 가중치와 편향을 이용해 계산한 결과 값에
# # 텐서플로우에서 기본적으로 제공하는 활성화 함수인 ReLU 함수를 적용합니다.
# L = tf.nn.relu(L)

# # 마지막으로 softmax 함수를 이용하여 출력값을 사용하기 쉽게 만듭니다
# # softmax 함수는 다음처럼 결과값을 전체합이 1인 확률로 만들어주는 함수입니다.
# # 예) [8.04, 2.76, -6.52] -> [0.53 0.24 0.23]
# model = tf.nn.softmax(L)

# # 신경망을 최적화하기 위한 비용 함수를 작성합니다.
# # 각 개별 결과에 대한 합을 구한 뒤 평균을 내는 방식을 사용합니다.
# # 전체 합이 아닌, 개별 결과를 구한 뒤 평균을 내는 방식을 사용하기 위해 axis 옵션을 사용합니다.
# # axis 옵션이 없으면 -1.09 처럼 총합인 스칼라값으로 출력됩니다.
# #        Y         model         Y * tf.log(model)   reduce_sum(axis=1)
# # 예) [[1 0 0]  [[0.1 0.7 0.2]  -> [[-1.0  0    0]  -> [-1.0, -0.09]
# #     [0 1 0]]  [0.2 0.8 0.0]]     [ 0   -0.09 0]]
# # 즉, 이것은 예측값과 실제값 사이의 확률 분포의 차이를 비용으로 계산한 것이며,
# # 이것을 Cross-Entropy 라고 합니다.
# cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(model), axis=1))

# optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
# train_op = optimizer.minimize(cost)


# #########
# # 신경망 모델 학습
# ######
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init)

# for step in range(100):
#     sess.run(train_op, feed_dict={X: x_data, Y: y_data})

#     if (step + 1) % 10 == 0:
#         print(step + 1, sess.run(cost, feed_dict={X: x_data, Y: y_data}))


# #########
# # 결과 확인
# # 0: 기타 1: 포유류, 2: 조류
# ######
# # tf.argmax: 예측값과 실제값의 행렬에서 tf.argmax 를 이용해 가장 큰 값을 가져옵니다.
# # 예) [[0 1 0] [1 0 0]] -> [1 0]
# #    [[0.2 0.7 0.1] [0.9 0.1 0.]] -> [1 0]
# prediction = tf.argmax(model, 1)
# target = tf.argmax(Y, 1)
# print('예측값:', sess.run(prediction, feed_dict={X: x_data}))
# print('실제값:', sess.run(target, feed_dict={Y: y_data}))

# is_correct = tf.equal(prediction, target)
# accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
# print('정확도: %.2f' % sess.run(accuracy * 100, feed_dict={X: x_data, Y: y_data}))