#!/bin/bash

echo 5 > /sys/devices/leds-qpnp-f616c600/leds/red/ramp_step_ms
echo 5 > /sys/devices/leds-qpnp-f616c600/leds/green/ramp_step_ms
echo 5 > /sys/devices/leds-qpnp-f616c600/leds/blue/ramp_step_ms
