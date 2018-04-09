#!/bin/bash

echo 5 > /sys/class/leds/red/ramp_step_ms
echo 5 > /sys/class/leds/green/ramp_step_ms
echo 5 > /sys/class/leds/blue/ramp_step_ms
