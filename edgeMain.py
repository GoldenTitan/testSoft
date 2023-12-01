import pygetwindow as gw
import pyautogui
import pyperclip
import time

# 寻找标题后缀为"Edge"的窗口
selected_window = gw.getWindowsWithTitle("Edge")

# 如果找到了对应标题的窗口，则进行操作
if selected_window:
    # 进行你想要的操作
    # print("已找到对应标题的窗口：", selected_window[0])
    print("已找到Edge")
    # Activate the Edge window
    selected_window[0].activate()

    # Simulate keyboard shortcut to open a new tab
    pyautogui.hotkey('ctrl', 't')
    # Copy the URL to clipboard
    pyperclip.copy('http://localhost:8091/')

    # Simulate keyboard shortcut to paste and go
    pyautogui.hotkey('ctrl', 'shift', 'l')
    print("已找到http://localhost:8091/的前置窗口：")
    # Wait for the new tab to open
    time.sleep(2)
    pyperclip.copy('http://localhost:8091/leave_hospital')

    # Simulate keyboard shortcut to paste and go
    pyautogui.hotkey('ctrl', 'shift', 'l')
    print("已找到http://localhost:8091/leave_hospital的窗口：")

else:
    print("未找到'Edge'的窗口")
