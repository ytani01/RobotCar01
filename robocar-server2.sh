#!/bin/sh

#ENVDIR=${HOME}/env.pigpio
ENVDIR=${HOME}/env

ACTIVATE_SCRIPT=${ENVDIR}/bin/activate

WORK_DIR=${HOME}/RobotCar01
CMD=${WORK_DIR}/robocar-server2.py

if [ ! -f ${ACTIVATE_SCRIPT} ]; then
    echo ${ACTIVATE_SCRIPT}: no such file
    exit 1
fi

. ${ACTIVATE_SCRIPT}

cd ${WORK_DIR}
exec ${CMD} $*
