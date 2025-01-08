#!/usr/bin/env python3
# Python script to convert various types of audio files to Duplicated True Stereo (LRLR)
#
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

import os
import sys
import subprocess
import glob


def check_sox_installed():
    """Check if SoX is installed."""
    # Check if SoX is in PATH
    try:
        subprocess.run(["sox", '--version'],
                       capture_output=True, text=True, check=True)
        return "sox"
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # On Windows, check common installation paths
    if os.name == 'nt':
        common_paths = [
            r"C:\\Program Files (x86)\\sox-*",
            r"C:\\Program Files\\sox-*"
        ]

        for base_path in common_paths:
            path_pattern = os.path.join(base_path, "sox.exe")
            for sox_path in glob.glob(path_pattern):
                if os.path.exists(sox_path):
                    return sox_path

    # If SoX isn't found, inform the user
    if os.name == "posix":
        print("Error: SoX is not installed or not in PATH.")
        print("On Linux, you can install it with your package manager. For example:")
        print("  - On Debian/Ubuntu-based systems: sudo apt install sox")
        print("  - On Red Hat/Fedora/CentOS-based systems: sudo dnf install sox")
        print("  - On Arch-based systems: sudo pacman -S sox")
        print("On macOS, you can install it with: brew install sox")
    else:
        print("Error: SoX is not installed.")
        print("Download and install SoX from: http://sox.sourceforge.net/")
    sys.exit(1)


def convert_to_true_stereo(file, sox_command):
    """Convert the file to Duplicated True Stereo (LRLR) format."""
    supported_extensions = {"wav", "flac", "aiff", "aif", "ogg", "opus", "wv"}
    extension = os.path.splitext(file)[-1].lower().lstrip(".")

    if extension in supported_extensions:
        print(f"Converting '{file}' to Duplicated True Stereo (LRLR) format...")
        output = f"{os.path.splitext(file)[0]}_DTS.{extension}"
        try:
            subprocess.run([sox_command, file, output, "remix",
                           "1", "2", "1", "2"], check=True)
            print(f"Done: '{output}'")
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion of '{file}': {e}")
    else:
        print(f"Skipping unsupported file type: '{file}'")


def main():
    sox_command = check_sox_installed()

    if len(sys.argv) <= 1:
        print("Usage: python truestereoconvert.py file1 file2 ...")
        print("Supports: WAV, FLAC, AIFF (or AIF), OGG, OPUS, WAVPACK")
        sys.exit(1)

    # Handle wildcard expansion using glob
    files_to_process = []
    for arg in sys.argv[1:]:
        expanded_files = glob.glob(arg)  # Expand wildcard patterns
        if not expanded_files:
            print(f"Warning: No files matched for pattern '{arg}'")
        files_to_process.extend(expanded_files)  # Add expanded files to the list

    if not files_to_process:
        print("No files to process. Exiting.")
        sys.exit(1)

    # Process each file
    for file in files_to_process:
        if os.path.isfile(file):
            convert_to_true_stereo(file, sox_command)
        else:
            print(f"Skipping: '{file}' (not a valid file)")

    print("Conversion complete!")


if __name__ == "__main__":
    main()
