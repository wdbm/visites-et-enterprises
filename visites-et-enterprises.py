#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# visites-et-enterprises                                                       #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is an automated web login program.                              #
#                                                                              #
# copyright (C) 2015 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

name    = "visites-et-enterprises"
version = "2015-01-30T2346Z"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

identification = "Apt999"
passcode       = "wanknob"
URLlogin       = "https://controller.mobile.lan/101/portal/"

def main():

    driver = webdriver.Firefox()
    driver.get(URLlogin)

    time.sleep(4)

    inputLogin = driver.find_element_by_name("login")
    inputLogin.send_keys(identification)

    inputPasscode = driver.find_element_by_name("password")
    inputPasscode.send_keys(passcode)
    inputPasscode.send_keys(Keys.RETURN)

    driver.close()

if __name__ == "__main__":
    main()
