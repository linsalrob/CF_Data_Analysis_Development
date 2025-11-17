#!/usr/bin/env bash
# Usage:
#   Dry run (default):   ./rename_in_files.sh /path/to/dir
#   Apply changes:       ./rename_in_files.sh --apply /path/to/dir
#
# Notes:
# - Reports per-file, per-mapping replacement counts.
# - Handles both *.txt and *.txt.gz recursively.
# - Uses a temp file for gz files. No changes are made unless --apply is set.

set -euo pipefail
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

# -------- Parse args --------
APPLY=false
TARGET_DIR="."
# these are the files to check. Others (e.g. png, pdf) will be skipped.
PATTERNS=( "*.md" "*.md.gz" "*.txt" "*.tsv" "*.tsv.gz" "*.txt.gz" "*.json" "*.json.gz" )

for arg in "$@"; do
  case "$arg" in
    --apply) APPLY=true ;;
    -h|--help)
      echo "Usage: $0 [--apply] [DIRECTORY]"
      exit 0
      ;;
    *)
      TARGET_DIR="$arg"
      ;;
  esac
done

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Error: '$TARGET_DIR' is not a directory." >&2
  exit 1
fi

# -------- Mapping --------
declare -A MAP=(
  ['1112926_20171212_S']='1447437_20171212_S'
  ['1128691_20170206_S']='1128691_20171206_S'
  ['1255498_20171212_S']='1590009_20171212_S'
  ['1316979_20171215_S']='1651490_20171215_S'
  ['1598281_20180508_S']='1588281_20180508_S'
  ['1723809_20180227_S']='1085876_20180227_S'
  ['649354_20170206_S']='639354_20171206_S'
  ['652927_20180226_S']='715927_20180226_S'
  ['658355_20180301_S']='658355_20180327_S'
  ['777851_20170918_S']='778851_20170918_S'
  ['788707_20181126_S']='788707_20181129_S'
  ['698917_20190119_S']='698917_20180119_S'
)

# -------- Summary counters --------
total_files=0
total_modified_files=0
total_replacements=0

mode="DRY RUN"
$APPLY && mode="APPLY MODE"
echo " $mode scanning: $TARGET_DIR"
echo

# -------- Helper: process a plain text file --------
process_txt_file() {
  local file="$1"
  local file_total=0
  echo "Processing $file"
  for old in "${!MAP[@]}"; do
    local new="${MAP[$old]}"
    # Count prospective replacements without changing the file
    local count
    count=$(sed -n "s/${old}/${new}/gp" "$file" | wc -l | awk '{print $1}')
    if (( count > 0 )); then
      printf "    %s ->  %s : %d\n" "$old" "$new" "$count"
      file_total=$((file_total + count))
      if $APPLY; then
        sed -i "s/${old}/${new}/g" "$file"
      fi
    fi
  done
  if (( file_total > 0 )); then
    total_modified_files=$((total_modified_files + 1))
    total_replacements=$((total_replacements + file_total))
    echo "  ->  File total: $file_total replacements"
  fi
}

# -------- Helper: process a gzipped text file --------
process_gz_file() {
  local file="$1"
  local file_total=0
  echo "Processing $file"
  local tmp
  tmp=$(mktemp)
  # Always inflate to inspect; only write back if --apply and changes occurred
  gunzip -c "$file" > "$tmp"

  for old in "${!MAP[@]}"; do
    local new="${MAP[$old]}"
    local count
    count=$(sed -n "s/${old}/${new}/gp" "$tmp" | wc -l | awk '{print $1}')
    if (( count > 0 )); then
      printf "    %s -> %s : %d\n" "$old" "$new" "$count"
      file_total=$((file_total + count))
      if $APPLY; then
        sed -i "s/${old}/${new}/g" "$tmp"
      fi
    fi
  done

  if $APPLY && (( file_total > 0 )); then
    # Write to a temp gz then atomically replace
    local out_tmp="${file}.tmp"
    gzip -c "$tmp" > "$out_tmp"
    mv "$out_tmp" "$file"
  fi
  rm -f "$tmp"

  if (( file_total > 0 )); then
    total_modified_files=$((total_modified_files + 1))
    total_replacements=$((total_replacements + file_total))
    echo "  ->  File total: $file_total replacements"
  fi
}

# which files to test
FIND_EXPR=()
for i in "${!PATTERNS[@]}"; do
	FIND_EXPR+=(-name "${PATTERNS[$i]}")
	if (( i < ${#PATTERNS[@]} - 1 )); then
		FIND_EXPR+=(-o)
	fi
done

# -------- Walk files safely (null-delimited) --------
while IFS= read -r -d '' f; do
  ((total_files+=1))
  if [[ "$f" == *.gz ]]; then
    process_gz_file "$f"
  else
    process_txt_file "$f"
  fi
done < <(find "$TARGET_DIR" -type f \( ${FIND_EXPR[@]} \) -print0)

echo
echo "===== Summary: $mode ====="
echo "Files scanned        : $total_files"
echo "Files with changes   : $total_modified_files"
echo "Total replacements   : $total_replacements"
$APPLY || echo "(No files were modified  -- rerun with --apply to perform changes)"


echo "These files were NOT examined:" >&2
find "$TARGET_DIR" -type f ! \( ${FIND_EXPR[@]} \) -print0 | xargs -0 ls -l >&2
