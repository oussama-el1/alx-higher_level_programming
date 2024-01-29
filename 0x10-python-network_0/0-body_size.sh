#!/bin/bash
# size of body response
curl -s "$1" | wc -c
