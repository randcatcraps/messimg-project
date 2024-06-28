#!/bin/bash

set -e

cd "$(dirname "$0")"

_l10n_dir=l10n

(set -x && mkdir -p "$_l10n_dir")

[[ -z "$LUPDATE" ]] && LUPDATE=/usr/lib/qt6/bin/lupdate

echo "lupdate is '${LUPDATE}'"

# exclude uic emitted files, N.B. don't match the specials files
mapfile -t _src_files < <(find ./ -type f -name \*.py | grep -vE '^./_[^_]+.py$')

# dummy translation
echo 'create stub translation for japanese'
cat > "${_l10n_dir}/ja_JP.ts" << EOF
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1">
</TS>
EOF

for _lang in en_US zh_CN; do
	_ts_file="${_l10n_dir}/${_lang}.ts"

	(set -x && $LUPDATE -no-obsolete \
	  -source-language ja_JP \
	  -target-language "$_lang" \
	  ./*.ui "${_src_files[@]}" -ts "$_ts_file")
done

echo 'done'
