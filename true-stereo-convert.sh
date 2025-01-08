#!/bin/sh
# Batch script to convert various types of audio files to Duplicated True Stereo (LRLR)

# true-stereo-convert
# Copyright (C) 2024 chmaha
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

if ! command -v sox >/dev/null 2>&1
then
    echo "Error: Please install SoX to use this script."
    echo "On Linux, you can install it with your package manager. For example:"
    echo "  - On Debian/Ubuntu-based systems: sudo apt install sox"
    echo "  - On Red Hat/Fedora/CentOS-based systems: sudo dnf install sox"
    echo "  - On Arch-based systems: sudo pacman -S sox"
    echo "On macOS, you can install it with: brew install sox"
    exit 1
fi

if [ "$#" -eq 0 ]; then
  echo "Usage: ./true-stereo-convert.sh file1 file2 ..."
  echo "Supports: WAV, FLAC, AIFF (or AIF), OGG, OPUS, WAVPACK"
  exit 1
fi

SUPPORTED_EXTENSIONS="wav flac aiff aif ogg opus wv"

for file in "$@"; do
  extension=$(echo "${file##*.}" | tr '[:upper:]' '[:lower:]')

  if echo "$SUPPORTED_EXTENSIONS" | grep -qw "$extension"; then
    echo "Converting '$file' to Duplicated True Stereo (LRLR) format..."
    output="${file%.*}_DTS.${extension}"
    sox "$file" "$output" remix 1 2 1 2
    echo "Done: '$output'"
  else
    echo "Skipping unsupported file type: '$file'"
  fi
done

echo "Conversion complete!"

