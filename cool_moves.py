#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_move(robot: cozmo.robot.Robot):
    robot.say_text("Halo, allemaal!").wait_for_completed()

    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()

    for _ in range(12):
        if _ % 2 == 0:
            robot.set_all_backpack_lights(cozmo.lights.green_light)
        else:
            robot.set_all_backpack_lights(cozmo.lights.red_light)

        robot.turn_in_place(degrees(30)).wait_for_completed()

    robot.set_all_backpack_lights(cozmo.lights.off_light)
    robot.drive_straight(distance_mm(-150), speed_mmps(50)).wait_for_completed()
    robot.say_text("Show is done!").wait_for_completed()
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()


cozmo.run_program(cozmo_move)
