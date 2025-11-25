import subprocess
import os
import time
from datetime import datetime

try:
    import pyautogui
except ImportError:
    os.system("pip install pyautogui")
    import pyautogui

# ===== CẤU HÌNH =====

RESTART_LIST_FILE = "ld_launch_list.txt" 
TARGET_HOUR = 18   # Giờ 18h (6 PM)
TARGET_MINUTE = 0 # Phút 30

def find_ldconsole():
    """Tự động tìm ldconsole.exe trong ổ C và D."""
    possible_drives = ["C:\\", "D:\\"]
    for drive in possible_drives:
        for root, dirs, files in os.walk(drive):
            if "ldconsole.exe" in files and "LDPlayer4.0\\LDPlayer" in root:
                return os.path.join(root, "ldconsole.exe")
    print("[LỖI] Không tìm thấy ldconsole.exe")
    return None

LDCONSOLE = find_ldconsole()

# ===== CÁC HÀM LDCONSOLE =====
def get_ld_list():
    """Lấy danh sách các giả lập LDPlayer."""
    if not LDCONSOLE:
        return []
    try:
        result = subprocess.run(
            [LDCONSOLE, "list2"],
            capture_output=True, text=True, timeout=8, encoding='utf-8'
        )
        lines = result.stdout.strip().splitlines()
        data = []
        for line in lines:
            parts = line.split(',')
            if len(parts) < 5:
                continue
            index = parts[0]
            name = parts[1]
            is_running = parts[4] == "1"
            pid = int(parts[2])
            if pid == 0 and parts[1].strip() == "":
                continue
            data.append({
                "index": index,
                "name": name,
                "running": is_running,
                "pid": pid
            })
        return data
    except Exception as e:
        print(f"Lỗi khi gọi ldconsole: {e}")
        return []

def ld_quit(index):
    """Tắt một giả lập theo index."""
    if not LDCONSOLE:
        return
    print(f"  Đang tắt index {index}...")
    subprocess.run([LDCONSOLE, "quit", "--index", str(index)], capture_output=True)

def ld_launch(index):
    """Mở một giả lập theo index."""
    if not LDCONSOLE:
        return
    print(f"  Đang mở index {index}...")
    subprocess.run([LDCONSOLE, "launch", "--index", str(index)], capture_output=True)

def uwindow():
    """Sắp xếp lại cửa sổ LDPlayer."""
    if not LDCONSOLE:
        return
    print("Sắp xếp các cửa sổ LD...")
    subprocess.run([LDCONSOLE, "sortWnd"], capture_output=True)

def restart_computer():
    """Khởi động lại máy tính sau 10 giây."""
    print("Đang khởi động lại máy tính sau 10 giây...")
    os.system("shutdown /r /t 10")

# ===== HÀM CLICK CHUỘT (RunTool) =====
def RunTool():
    """Thực hiện chuỗi thao tác click chuột."""
    print("Bắt đầu chạy tool (click chuột)...")
    try:
        pyautogui.click(60, 23); time.sleep(1)
        pyautogui.click(285, 73); time.sleep(1)
        pyautogui.click(365, 50); time.sleep(2)
        pyautogui.click(270, 67); time.sleep(1)
        pyautogui.click(20, 420); time.sleep(1)
        pyautogui.click(70, 85); time.sleep(1)
        
        #Close LD's ADs
        pyautogui.click(240, 60); time.sleep(0.5)
        pyautogui.click(265, 60); time.sleep(0.5)
        pyautogui.click(290, 60); time.sleep(0.5)

        uwindow()

        pyautogui.click(330, 60); time.sleep(10)
        pyautogui.click(310, 170); time.sleep(2)
        pyautogui.click(330, 215); time.sleep(10)
        pyautogui.click(330, 95); time.sleep(20)
        pyautogui.click(360, 145); time.sleep(5)
        pyautogui.click(330, 130); time.sleep(10)
        pyautogui.click(175, 90); time.sleep(5)
        pyautogui.click(330, 165); time.sleep(300)
        
        pyautogui.click(120, 200); time.sleep(5)
        pyautogui.click(120, 200); time.sleep(5)
        pyautogui.click(120, 200); time.sleep(1)
        pyautogui.click(245, 155); time.sleep(1)
        pyautogui.click(120, 200); time.sleep(1)
        time.sleep(10)
        
        pyautogui.click(120, 200); time.sleep(1)
        pyautogui.click(245, 155); time.sleep(1)
        time.sleep(20)
        
        pyautogui.click(120, 200); time.sleep(3)
        pyautogui.click(120, 200); time.sleep(1)
        
        pyautogui.click(12, 42); time.sleep(1)
        pyautogui.click(12, 42); time.sleep(1)
        pyautogui.click(12, 42); time.sleep(1)

        pyautogui.click(120, 200); time.sleep(3)
        pyautogui.click(120, 200); time.sleep(1)
        
        pyautogui.click(215, 145); time.sleep(1)
        pyautogui.click(215, 145); time.sleep(1)
        pyautogui.click(215, 145); time.sleep(1)
        
        pyautogui.click(12, 42); time.sleep(1)
        pyautogui.click(12, 42); time.sleep(1)
        pyautogui.click(12, 42); time.sleep(1)
        pyautogui.click(12, 42); time.sleep(1)
        pyautogui.click(12, 42); time.sleep(1)
        pyautogui.click(12, 42); time.sleep(1)
        pyautogui.click(12, 42); time.sleep(1)
        pyautogui.click(12, 42); time.sleep(1)
        
        
        pyautogui.click(10, 215); time.sleep(60)
        pyautogui.click(155, 75); time.sleep(10)
        pyautogui.click(330, 80); time.sleep(10)
        pyautogui.click(265, 190); time.sleep(10)
        pyautogui.click(333, 50); time.sleep(5)
        pyautogui.click(170, 60)
        print("...Hoàn tất RunTool.")
    except Exception as e:
        print(f"[LỖI] Lỗi xảy ra trong RunTool (pyautogui): {e}")


# ===== LOGIC MỚI (TÁC VỤ KHỞI ĐỘNG & HẸN GIỜ) =====

def trigger_scheduled_restart():
    if not LDCONSOLE:
        print("[LỖI] Không có LDCONSOLE, không thể thực hiện restart.")
        return

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Đã tới giờ, bắt đầu quá trình restart...")
    ld_list = get_ld_list()
    if not ld_list:
        print("Không có dữ liệu LDPlayer, bỏ qua.")
        return

    not_running_tabs = [
    ld['index'] for ld in ld_list
    if not ld['running'] and ld['index'] != "0"
    ]
    try:
        with open(RESTART_LIST_FILE, 'w') as f:
            for idx in not_running_tabs:
                f.write(f"{idx}\n")
        print(f"Đã lưu {len(not_running_tabs)} tab (chưa chạy) vào {RESTART_LIST_FILE}.")
    except Exception as e:
        print(f"[LỖI] Không thể ghi file {RESTART_LIST_FILE}: {e}")
        return

    running_tabs = [ld['index'] for ld in ld_list if ld['running']]
    if running_tabs:
        print(f"Đang tắt {len(running_tabs)} tab (đang chạy)...")
        for idx in running_tabs:
            ld_quit(idx)
        time.sleep(15)
    else:
        print("Không có tab nào đang chạy.")
    restart_computer()

def check_and_run_startup_task():
    if not LDCONSOLE:
        print("[LỖI] Không có LDCONSOLE, không thể chạy tác vụ khởi động.")
        return

    if os.path.exists(RESTART_LIST_FILE):
        print(f"Phát hiện file {RESTART_LIST_FILE}. Bắt đầu mở lại các tab đã lưu...")
        try:
            with open(RESTART_LIST_FILE, 'r') as f:
                indices_to_launch = [line.strip() for line in f if line.strip()]
            
            if not indices_to_launch:
                print("File restart rỗng, không làm gì cả.")
            else:
                print(f"Sẽ mở {len(indices_to_launch)} tab...")
                for idx in indices_to_launch:
                    ld_launch(idx)
                    time.sleep(7)
                
                print("Đã mở xong các tab. Chờ 30s để ổn định...")
                time.sleep(30)
                
                uwindow()
                
                print("Chờ 300s (5 phút) trước khi chạy tool...")
                time.sleep(300)
                
                RunTool()
                
            os.remove(RESTART_LIST_FILE)
            print(f"Đã xử lý và xóa file {RESTART_LIST_FILE}.")
        
        except Exception as e:
            print(f"[LỖI] Lỗi khi xử lý file restart: {e}")
            print(f"File {RESTART_LIST_FILE} sẽ KHÔNG bị xóa để kiểm tra lỗi.")
    else:
        print("Không tìm thấy file restart. Chuyển sang chế độ chờ hẹn giờ.")

# ===== VÒNG LẶP CHÍNH =====
if __name__ == "__main__":
    os.system("cls")
    print("===== SCRIPT TỰ ĐỘNG KHỞI ĐỘNG LẠI LDPLAYER =====")
    
    if not LDCONSOLE:
        input("[LỖI NGHIÊM TRỌNG] Không tìm thấy 'ldconsole.exe'. Nhấn Enter để thoát...")
    else:
        check_and_run_startup_task()
        print(f"\nScript đang chạy, sẽ thực hiện restart PC lúc {TARGET_HOUR}:{TARGET_MINUTE:02d} hàng ngày.")
        
        while True:
            try:
                now = datetime.now()
                if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
                    trigger_scheduled_restart()
                    break 
                if now.minute % 10 == 0 and now.second < 30:
                     print(f"[{now.strftime('%H:%M:%S')}] Đang chờ đến {TARGET_HOUR}:{TARGET_MINUTE:02d} để restart...")
                time.sleep(30)
            
            except KeyboardInterrupt:
                print("\nĐã nhận lệnh thoát (Ctrl+C). Tạm biệt!")
                break
            except Exception as e:
                print(f"[LỖI VÒNG LẶP CHÍNH] {e}")
                time.sleep(60) 





