#!/bin/sh
# -*- coding: utf-8 -*-

MYNAME=`basename $0`

MODEL_ID_FILE=${HOME}/bin/model-id.txt
MODEL_ID=`cat ${MODEL_ID_FILE}`

ENVDIR=${HOME}/env
ENVBIN=${ENVDIR}/bin
ROBOTCAR_DIR=${HOME}/RobotCar01

#####
cp ${ROBOTCAR_DIR}/RobotCar-GoogleAssistant.py ${ENVBIN}

. ${ENVBIN}/activate

#CMDLINE="FabLabKannai-GoogleAssistant.py --device_model_id ${MODEL_ID}"
CMDLINE="RobotCar-GoogleAssistant.py --device_model_id ${MODEL_ID}"
exec ${CMDLINE}
