# true-stereo-convert

A simple script to convert stereo audio files (WAV, FLAC, AIFF, OGG, Opus, WavPack) into "true stereo" (LRLR) format using [SoX](http://sox.sourceforge.net/). 

This tool processes audio files by duplicating the left and right channels and outputting them in the LRLR format (Left-Right-Left-Right) while maintaining the same channel information.

## Features

- Supports a wide range of audio formats: WAV, FLAC, AIFF, OGG, Opus, and WavPack.
- Simple batch conversion by python (all OSes) or shell script (Linux/MacOS).
- The output is saved with the suffix `_DTS` ("Duplicated True Stereo") to indicate the processed format.
  

## Prerequisites

Before using this script, ensure you have SoX (Sound eXchange) installed:
  - **Linux**: Install via your package manager using `sudo apt install sox` (Debian/Ubuntu), `sudo dnf in sox` (Fedora) etc.
  - **macOS**: Install using `brew install sox` (Homebrew).
  - **Windows**: Download and install SoX from: http://sox.sourceforge.net/.

### Python Usage:
If you don't have the script set as executable or if you're on Windows, run the script using Python:
```sh
python true-stereo-convert.py <file_pattern>
```
On Unix-based systems (MacOS/Linux), if you have the script as executable, you can run it directly:
```sh
chmod +x true-stereo-convert.py
./true-stereo-convert <file_pattern>
```

## Usage Example

```shell
./true-stereo-convert.sh *.wav
```
or
```shell
./true-stereo-convert.py *.wav
```

## Test IR

Included in the repository is a mono-to-stereo IR. To convert:
```shell
python true-stereo-convert.py IR-Berliner-Philharmoniker-Berlin.wav
```
