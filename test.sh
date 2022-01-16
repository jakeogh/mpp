#!/bin/sh

set -o nounset
set -x

timestamp=$(date "+%s")
working_dir="${timestamp}_mpp_test"
mkdir "${working_dir}" || exit 1
cd "${working_dir}" || exit 1
mpp && { echo "Error: mpp exited 0 with no args." ; exit 1 ; }
mpp "${timestamp}" | grep "${timestamp}" || { echo "Error: mpp did not write ${timestamp} to stdout." ; exit 1 ; }
mpp "" && { echo "Error: mpp exited 0 with only an empty arg." ; exit 1 ; }
