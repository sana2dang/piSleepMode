# pi_sleepMode
- 파이 슬립모드

./pAction/pStop.sh <-- 컨트롤러 일정시간 조작이 없을 때 수행할 업무 : 프로세스 멈추기

./pAction/pStart.sh <-- pStop.sh이 동작한 후 컨트롤러 조작하면 수행할 업무 : 프로세스 깨우기




- install 방법

git clone https://github.com/sana2dang/piSleepMode

cd piSleepMode

sudo chmod 755 ./install.sh

sudo chmod 755 ./uninstall.sh

./install.sh



- uninstall 방법

./uninstall.sh



- 실행방법

게임 실행시 자동으로 실행되며 

컨트롤러 조작이 없을 경우 1분 뒤 게임이 일시정지 됩니다.

컨트롤러를 다시 조작하면 게임이 다시 시작됩니다.



- 슬립 시간 변경하기

/opt/retropie/configs/all/runcommand-onstart.sh 를 편집기로 열어서


sudo python /opt/retropie/configs/all/piSleepMode/piSleep.py 1.0 & > /dev/null 2>&1


5분30초로 변경 하기

piSleep.py 1.0 을 -> piSleep.py 5.5





- 프로세스명이 아래 문구를 포함하면 일시정지

emulator

pcsx

cannonball

SorR.dat
