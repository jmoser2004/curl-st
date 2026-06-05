#!/bin/bash
mkdir dummy_data
dd if=/dev/zero of=dummy_data/quarter_gig.bin bs=1M count=256
dd if=/dev/zero of=dummy_data/half_gig.bin bs=1M count=512
dd if=/dev/zero of=dummy_data/gig.bin bs=1M count=1024

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt