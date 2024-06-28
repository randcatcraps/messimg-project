#!/bin/bash

set -e

cd "$(dirname "$0")"

_l10n_dir=l10n
_locales_dir=_locales

(set -x && mkdir -p "$_locales_dir")

[[ -z "$LRELEASE" ]] && LRELEASE=/usr/lib/qt6/bin/lrelease

echo "lrelease is '${LRELEASE}'"

for _lang in ja_JP en_US zh_CN; do
	_ts_file="${_l10n_dir}/${_lang}.ts"
	_qm_file="${_locales_dir}/${_lang}.qm"

	if [ ! -e "$_ts_file" ]; then
		echo "warn: skipping non-existing locale: ${_lang}"
		continue
	fi

	(set -x && $LRELEASE \
	  -nounfinished -removeidentical \
	  "$_ts_file" -qm "$_qm_file")
done

echo 'done'
