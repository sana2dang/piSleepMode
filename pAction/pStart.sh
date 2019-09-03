#!/usr/bin/env bash

ps -ef | grep emulators | grep -v grep | awk '{print $2}' | xargs kill -SIGCONT
ps -ef | grep pcsx | grep -v grep | awk '{print $2}' | xargs kill -SIGCONT