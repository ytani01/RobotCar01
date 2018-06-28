#!/bin/sh

ENVDIR=${HOME}/env.pigpio
ENVDIR=${HOME}/env

ACTIVATE_SCRIPT=${ENVDIR}/bin/activate

WORK_DIR=${HOME}/RobotCar01
CMD=${WORK_DIR}/robocar4.py

if [ ! -f ${ACTIVATE_SCRIPT} ]; then
    echo ${ACTIVATE_SCRIPT}: no such file
    exit 1
fi

. ${ENVDIR}/bin/activate

cd ${WORK_DIR}
exec python ${CMD}
