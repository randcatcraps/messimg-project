#!/bin/bash

set -e

cd "$(dirname "$0")"

[[ -z "$UIC" ]] && UIC=/usr/lib/qt6/uic

echo "uic is '${UIC}'"

for _ui_file in *.ui; do
	_py_file="_${_ui_file%.ui}.py"

	(set -x && $UIC -g python "$_ui_file" -o "$_py_file")
done

echo 'done'
