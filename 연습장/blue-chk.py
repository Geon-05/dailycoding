import asyncio
from bleak import BleakScanner

async def scan_all_devices():
    print("주변의 모든 BLE 장치를 검색 중...")
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"이름: {device.name}, 주소: {device.address}, RSSI: {device.rssi} dBm")
    print("검색 완료")

# 비동기 실행
asyncio.run(scan_all_devices())


import asyncio
from bleak import BleakScanner

# 확인하려는 특정 기기의 MAC 주소
TARGET_ADDRESS = "F6:35:EC:CA:2D:00"  # 측정할 기기의 MAC 주소를 넣으세요

async def scan_and_check_signal_strength():
    print("BLE 장치 검색 중...")

    # 검색할 때마다 감도 정보를 확인하는 콜백 함수
    def detection_callback(device, advertisement_data):
        if device.address == TARGET_ADDRESS:
            print(f"이름: {device.name}, 주소: {device.address}, RSSI: {device.rssi} dBm")

    # BleakScanner에서 detection_callback을 설정하여 모든 검색 결과를 확인
    scanner = BleakScanner(detection_callback=detection_callback)
    
    # 스캐너를 일정 시간 동안 실행합니다.
    await scanner.start()
    await asyncio.sleep(10)  # 10초 동안 검색
    await scanner.stop()
    print("검색 완료")

# 비동기 함수 실행
asyncio.run(scan_and_check_signal_strength())