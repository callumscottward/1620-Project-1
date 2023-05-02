from PyQt6.QtWidgets import *
from view import *


class Television(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 1
    MAX_CHANNEL = 9

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

        self.label_volume.setText('')
        self.label_channel.setText('')

        self.button_power.clicked.connect(lambda: self.power())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.button_1.clicked.connect(lambda: self.channel_num(1))
        self.button_2.clicked.connect(lambda: self.channel_num(2))
        self.button_3.clicked.connect(lambda: self.channel_num(3))
        self.button_4.clicked.connect(lambda: self.channel_num(4))
        self.button_5.clicked.connect(lambda: self.channel_num(5))
        self.button_6.clicked.connect(lambda: self.channel_num(6))
        self.button_7.clicked.connect(lambda: self.channel_num(7))
        self.button_8.clicked.connect(lambda: self.channel_num(8))
        self.button_9.clicked.connect(lambda: self.channel_num(9))
        self.button_volume_up.clicked.connect(lambda: self.volume_up())
        self.button_volume_down.clicked.connect(lambda: self.volume_down())
        self.button_channel_up.clicked.connect(lambda: self.channel_up())
        self.button_channel_down.clicked.connect(lambda: self.channel_down())

    def power(self):
        if self.__status:
            self.__status = False
            self.label_off.setText('OFF')
            self.label_volume.setText('')
            self.label_channel.setText('')

        else:
            self.__status = True
            self.label_off.setText('')

            if self.__muted:
                self.label_volume.setText(f'VOL\n⊘')
            else:
                self.label_volume.setText(f'VOL\n{self.__volume}')

            self.label_channel.setText(f'CH\n{self.__channel}')

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.label_volume.setText(f'VOL\n{self.__volume}')

            else:
                self.__muted = True
                self.label_volume.setText(f'VOL\n⊘')

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                self.label_channel.setText(f'CH\n{self.__channel}')
            else:
                self.__channel = Television.MIN_CHANNEL
                self.label_channel.setText(f'CH\n{self.__channel}')

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                self.label_channel.setText(f'CH\n{self.__channel}')
            else:
                self.__channel = Television.MAX_CHANNEL
                self.label_channel.setText(f'CH\n{self.__channel}')

    def channel_num(self, num):
        if self.__status:
            self.__channel = num
            self.label_channel.setText(f'CH\n{self.__channel}')

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.label_volume.setText(f'VOL\n{self.__volume}')

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.label_volume.setText(f'VOL\n{self.__volume}')

    def __str__(self):
        if self.__muted:
            return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
