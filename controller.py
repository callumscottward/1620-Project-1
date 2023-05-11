from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from view import *


class Television(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 1
    MAX_CHANNEL = 9

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes GUI controller, adding backend-frontend integration for calculator
        based on view.py file.
        :param args: Essential for functionality of PyQt, based on Test 10 code
        :param kwargs: See above
        """
        # PyQt vars from Test 10
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Original Television class private values
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

        # Volume and channel start off blank because Television is off
        self.label_volume.setText('')
        self.label_channel.setText('')

        # Pixmap vars for imported channel logo image files
        self.icon_amc = QPixmap('assets/amc.jpg')
        self.icon_animal_planet = QPixmap('assets/animal_planet.jpg')
        self.icon_cn = QPixmap('assets/cn.jpg')
        self.icon_discovery = QPixmap('assets/discovery.jpg')
        self.icon_food = QPixmap('assets/food.jpg')
        self.icon_history = QPixmap('assets/history.jpg')
        self.icon_nat_geo = QPixmap('assets/nat_geo.jpg')
        self.icon_pbs = QPixmap('assets/pbs.jpg')
        self.icon_weather = QPixmap('assets/weather.jpg')

        # List arranging Pixmaps into order of channels
        self.channels = [self.icon_amc, self.icon_animal_planet, self.icon_cn, self.icon_discovery, self.icon_food,
                         self.icon_history, self.icon_nat_geo, self.icon_pbs, self.icon_weather]

        # Connecting buttons to methods
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

    def power(self) -> None:
        """
        Uses power button to turn TV off if on or on if off by changing value of
        self.__status and label values accordingly.
        """
        if self.__status:
            # Turns TV off if on
            self.__status = False
            self.label_main.setText('OFF')
            self.label_volume.setText('')
            self.label_channel.setText('')

        else:
            # Turns TV on if off and restores labels
            self.__status = True

            if self.__muted:
                self.label_volume.setText(f'VOL\n⊘')
            else:
                self.label_volume.setText(f'VOL\n{self.__volume}')

            self.label_channel.setText(f'CH\n{self.__channel}')
            self.label_main.setPixmap(self.channels[self.__channel - 1])
            self.label_main.setScaledContents(True)

    def mute(self) -> None:
        """
        If unmuted, mutes TV by temporarily disabling volume and setting its value to the
        character ⊘. Inherently different from setting volume to 0, because old volume
        can easily be restored by changing volume again or unmuting. Otherwise, unmutes
        muted TV.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.label_volume.setText(f'VOL\n{self.__volume}')

            else:
                self.__muted = True
                self.label_volume.setText(f'VOL\n⊘')

    def channel_up(self) -> None:
        """
        Increases channel number and associated screen display by one, wrapping back
        to 1 at end of channel list.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                self.label_channel.setText(f'CH\n{self.__channel}')
            else:
                # Loops back to MIN_CHANNEL instead of MAX_CHANNEL + 1
                self.__channel = Television.MIN_CHANNEL
                self.label_channel.setText(f'CH\n{self.__channel}')

            # Retrieves proper Pixmap index and scales to label
            self.label_main.setPixmap(self.channels[self.__channel - 1])
            self.label_main.setScaledContents(True)

    def channel_down(self) -> None:
        """
        Decreases channel number and associated screen display by one, wrapping back
        to 9 at beginning of channel list.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                self.label_channel.setText(f'CH\n{self.__channel}')
            else:
                # Loops back to MAX_CHANNEL instead of MIN_CHANNEL - 1
                self.__channel = Television.MAX_CHANNEL
                self.label_channel.setText(f'CH\n{self.__channel}')

            # Retrieves proper Pixmap index and scales to label
            self.label_main.setPixmap(self.channels[self.__channel - 1])
            self.label_main.setScaledContents(True)

    def channel_num(self, num: int) -> None:
        """
        Manually sets channel to specified single-digit number based on which keypad
        number is pressed on remote.
        :param num: Number on keypad that is pressed, passed in lambda connection
        """
        if self.__status:
            self.__channel = num
            self.label_channel.setText(f'CH\n{self.__channel}')

            # Retrieves proper Pixmap index and scales to label
            self.label_main.setPixmap(self.channels[self.__channel - 1])
            self.label_main.setScaledContents(True)

    def volume_up(self) -> None:
        """
        Increases volume and volume label by one, stopping at MAX_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.label_volume.setText(f'VOL\n{self.__volume}')

    def volume_down(self) -> None:
        """
        Decreases volume and volume label by one, stopping at MIN_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.label_volume.setText(f'VOL\n{self.__volume}')

    def __str__(self) -> str:
        """
        Prints string consisting of TV's characteristics when the TV's variable is
        printed. Brought in as carryover from original lab and not utilized in this
        project, but feasibly could be.
        :return: String of TV's values associated with variable name
        """
        if self.__muted:
            return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
