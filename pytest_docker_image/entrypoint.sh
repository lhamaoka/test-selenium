#!/bin/bash

main_command="pytest"

if [ $ENABLE_PYTEST_CACHE != True ]
then
main_command="${main_command} -p no:cacheprovider"
fi

if [ $ENABLE_ALLURE_REPORT != False ]
then
main_command="${main_command} --alluredir=/AllureReports"
fi

if [ $ENABLE_MULTITHEAD != False ]
then
main_command="${main_command} -n ${THREAD_COUNT}"
fi

${main_command} ${@}
