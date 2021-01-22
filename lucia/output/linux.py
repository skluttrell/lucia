# Copyright LuciaSoftware 2019 - 2020
#
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE or copy at
# https://www.boost.org/LICENSE_1_0.txt)
import espeakng  # type: ignore

from lucia.output.generic import GenericOutputDriver


class LinuxOutputDriver(GenericOutputDriver):
    def __init__(self):
        self._speech_driver = espeakng.Speaker()

    def output(self, message, interrupt=True):
        return self.speak(message, interrupt)

    def speak(self, message, interrupt=True):
        if interrupt:
            self._speech_driver.say(message)
            return True
        self._speech_driver.say(message, wait4prev=True)
        return True