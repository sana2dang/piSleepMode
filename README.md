# pi_sleepMode
- 파이 슬립모드

pStop.sh <-- 컨트롤러 일정시간 조작이 없을 때 수행할 업무 : 프로세스 멈추기

pStart.sh <-- pStop.sh이 동작한 후 컨트롤러 조작하면 수행할 업무 : 프로세스 깨우기



- 선행작업

sudo chmod 755 ./pAction/pStart.sh

sudo chmod 755 ./pAction/pStop.sh


piSleep.py 소스내부의 actionPath 경로 바꿔주기


- 실행 방법

piSleep.py 분(소수점가능)


예) python piSleep.py 1.1




프로세스명이 아래 문구를 포함하면 일시정지

emulator
pcsx
