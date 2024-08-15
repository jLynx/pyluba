from enum import Enum


class DeviceType(Enum):
    UNKNOWN = (-1, "UNKNOWN", "Unknown")
    RTK = (0, "RTK", "RTK")
    LUBA = (1, "Luba", "Luba 1")
    LUBA_2 = (2, "Luba-VS", "Luba 2")
    LUBA_YUKA = (3, "Yuka-", "Yuka")
    YUKA_MINI = (4, "Yuka-MN", "Yuka Mini")
    YUKA_MINI2 = (5, "Yuka-YM", "Yuka Mini 2")
    LUBA_VP = (6, "Luba-VP", "Luba VP")

    def __init__(self, value: int, name: str, model: str):
        self._value = value
        self._name = name
        self._model = model

    def get_name(self):
        return self._name

    def get_model(self):
        return self._model

    def get_value(self):
        return self._value

    def get_value_str(self):
        return str(self._value)

    def set_value(self, value):
        self._value = value

    @staticmethod
    def valueof(value):
        """Return the corresponding DeviceType based on the input value.

        This function takes an integer value as input and returns the
        corresponding DeviceType enum value.

        Args:
            value (int): An integer representing the device type.

        Returns:
            DeviceType: The corresponding DeviceType enum value based on the input value.

        """

        if value == 0:
            return DeviceType.RTK
        if value == 1:
            return DeviceType.LUBA
        if value == 2:
            return DeviceType.LUBA_2
        if value == 3:
            return DeviceType.LUBA_YUKA
        return DeviceType.UNKNOWN

    @staticmethod
    def value_of_str(device_name, product_key=""):
        """Determine the type of device based on the provided device name and product key.

        Args:
            device_name (str): The name of the device.
            product_key (str?): The product key associated with the device. Defaults to "".

        Returns:
            DeviceType: The type of device based on the provided information.

        """

        if not device_name and not product_key:
            return DeviceType.UNKNOWN

        try:
            substring = device_name[:3]
            substring2 = device_name[:7]

            if DeviceType.RTK.name in substring or DeviceType.contain_rtk_product_key(product_key):
                return DeviceType.RTK
            elif DeviceType.LUBA_2.name in substring2 or DeviceType.contain_luba_2_product_key(product_key):
                return DeviceType.LUBA_2
            elif DeviceType.LUBA_YUKA.name in substring2:
                return DeviceType.LUBA_YUKA
            elif DeviceType.LUBA.name in substring2 or DeviceType.contain_luba_product_key(product_key):
                return DeviceType.LUBA
            else:
                return DeviceType.UNKNOWN
        except Exception:
            return DeviceType.UNKNOWN

    @staticmethod
    def has_4g(device_name, product_key=""):
        """Check if the device has 4G capability based on the device name and optional product key.

        This function determines the device type based on the device name and
        product key (if provided). It then checks if the device type has a value
        greater than or equal to the 4G threshold.

        Args:
            device_name (str): The name of the device.
            product_key (str?): The product key associated with the device. Defaults to "".

        Returns:
            bool: True if the device has 4G capability, False otherwise.

        """

        if not product_key:
            device_type = DeviceType.value_of_str(device_name)
        else:
            device_type = DeviceType.value_of_str(device_name, product_key)

        return device_type.get_value() >= DeviceType.LUBA_2.get_value()

    @staticmethod
    def is_luba1(device_name, product_key=""):
        """Check if the given device is of type LUBA.

        This function determines if the device specified by 'device_name' is of
        type LUBA. If 'product_key' is provided, it is used to further identify
        the device type.

        Args:
            device_name (str): The name of the device.
            product_key (str?): The product key associated with the device. Defaults to "".

        Returns:
            bool: True if the device is of type LUBA, False otherwise.

        """

        if not product_key:
            device_type = DeviceType.value_of_str(device_name)
        else:
            device_type = DeviceType.value_of_str(device_name, product_key)

        return device_type.get_value() == DeviceType.LUBA.get_value()

    @staticmethod
    def is_luba_2(device_name, product_key=""):
        """Check if the device type is LUBA 2 or higher based on the device name and optional product key.

        Args:
            device_name (str): The name of the device.
            product_key (str?): The product key associated with the device. Defaults to "".

        Returns:
            bool: True if the device type is LUBA 2 or higher, False otherwise.

        """

        if not product_key:
            device_type = DeviceType.value_of_str(device_name)
        else:
            device_type = DeviceType.value_of_str(device_name, product_key)

        return device_type.get_value() >= DeviceType.LUBA_2.get_value()

    @staticmethod
    def is_yuka(device_name):
        """Check if the given device name corresponds to a LUBA_YUKA device type.

        Args:
            device_name (str): The name of the device to be checked.

        Returns:
            bool: True if the device type is LUBA_YUKA, False otherwise.

        """

        return DeviceType.value_of_str(device_name).get_value() == DeviceType.LUBA_YUKA.get_value()

    @staticmethod
    def is_rtk(device_name, product_key=""):
        """Check if the device type is within the range of RTK devices.

        This function determines if the device type corresponding to the given
        device name and optional product key falls within the range of RTK
        (Real-Time Kinematic) devices.

        Args:
            device_name (str): The name of the device.
            product_key (str?): The product key associated with the device. Defaults to "".

        Returns:
            bool: True if the device type is within the RTK range, False otherwise.

        """

        if not product_key:
            device_type = DeviceType.value_of_str(device_name)
        else:
            device_type = DeviceType.value_of_str(device_name, product_key)

        return DeviceType.RTK.get_value() <= device_type.get_value() < DeviceType.LUBA.get_value()

    @staticmethod
    def contain_rtk_product_key(product_key):
        """Check if the given product key is in a predefined list of RTK product keys.

        Args:
            product_key (str): The product key to be checked.

        Returns:
            bool: True if the product key is in the predefined list, False otherwise.

        """

        if not product_key:
            return False
        return product_key in ["a1qXkZ5P39W", "a1Nc68bGZzX"]

    @staticmethod
    def contain_luba_product_key(product_key):
        """Check if the given product key is in the list of valid product keys.

        Args:
            product_key (str): The product key to be checked.

        Returns:
            bool: True if the product key is in the list of valid keys, False otherwise.

        """

        if not product_key:
            return False
        return product_key in [
            "a1UBFdq6nNz",
            "a1x0zHD3Xop",
            "a1pvCnb3PPu",
            "a1kweSOPylG",
            "a1JFpmAV5Ur",
            "a1BmXWlsdbA",
            "a1jOhAYOIG8",
            "a1K4Ki2L5rK",
            "a1ae1QnXZGf",
            "a1nf9kRBWoH",
            "a1ZU6bdGjaM",
        ]

    @staticmethod
    def contain_luba_2_product_key(product_key):
        """Check if the given product key is present in a predefined list.

        Args:
            product_key (str): The product key to be checked.

        Returns:
            bool: True if the product key is in the predefined list, False otherwise.

        """

        if not product_key:
            return False
        return product_key in ["a1iMygIwxFC", "a1LLmy1zc0j", "a1LLmy1zc0j"]

    def is_support_video(self):
        return self == DeviceType.LUBA_YUKA

    def get_blade_height_range(self):
        """Returns the blade height range (min, max) for Luba 1 and Luba 2 devices.

        Returns:
            tuple: A tuple containing the minimum and maximum blade height (in mm),
                or None if the device type doesn't have a specified range.

        """
        if self == DeviceType.LUBA:
            return (30, 70)
        if self == DeviceType.LUBA_2:
            return (25, 70)
        return None
