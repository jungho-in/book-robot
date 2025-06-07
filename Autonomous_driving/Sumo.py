import traci
import subprocess
import time
import os

# SUMO 실행 파일 경로 (sumo 또는 sumo-gui)
SUMO_BINARY = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui.exe"  # 경로는 설치 위치에 맞게 수정

# 시뮬레이션 설정 파일 경로
SUMO_CONFIG = r"C:\book-robot\book-robot\Autonomous_driving\simulation.sumocfg"  # 본인 경로로 수정

# 사용할 포트
PORT = 8813

def start_sumo():
    cmd = [SUMO_BINARY, "-c", SUMO_CONFIG, "--remote-port", str(PORT)]
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def connect_traci(port=PORT, retries=10, wait=1):
    for _ in range(retries):
        try:
            traci.connect(port=port)
            print("TraCI 연결 성공")
            return True
        except Exception as e:
            print(f"연결 실패: {e}")
            time.sleep(wait)
    return False

def run_simulation():
    # 시뮬레이션 100스텝 동안 진행하며 차량 속도 제어 예시
    for step in range(100):
        traci.simulationStep()

        # 예: 차량 ID가 'veh0'라면 50번째 스텝에 속도 줄였다가 다시 올리기
        if step == 50:
            traci.vehicle.setSpeed('veh0', 0)  # 정지
            print("veh0 정지")
        elif step == 70:
            traci.vehicle.setSpeed('veh0', 10)  # 다시 속도 10으로
            print("veh0 속도 재개")

    traci.close()

def main():
    sumo_proc = start_sumo()
    if connect_traci():
        run_simulation()
    else:
        print("TraCI 연결 실패")
    sumo_proc.terminate()

if __name__ == "__main__":
    main()