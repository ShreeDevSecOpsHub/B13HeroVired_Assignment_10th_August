
# CPU Monitoring Program

## Overview
This Python program continuously monitors the CPU usage of the local machine and alerts the user if the usage exceeds a predefined threshold. 
It is useful for DevOps engineers to keep track of server performance and detect potential overload situations.

---

## Features
- **Continuous Monitoring**: Runs indefinitely until manually stopped by the user.
- **Threshold Alerts**: Alerts when CPU usage exceeds the configured limit.
- **Configurable Settings**: Easily change the CPU usage threshold and monitoring interval.
- **Error Handling**: Handles user interruptions and unexpected runtime errors gracefully.

---

## Requirements
- **Python 3.x**
- **psutil library**

Install the required library using pip:
```bash
pip install psutil
```

---

## Program Code
```python
import psutil
import time

def monitor_cpu(threshold=80, interval=1):
    """
    Monitors CPU usage and alerts if usage exceeds threshold.
    
    Args:
        threshold (int): CPU usage percentage to trigger an alert.
        interval (int): Time in seconds between checks.
    """
    print("Monitoring CPU usage... (Press Ctrl+C to stop)")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=interval)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Error occurred during monitoring: {e}")

if __name__ == "__main__":
    monitor_cpu(threshold=80, interval=1)
```

---

## How It Works
1. The program uses the **`psutil`** library to get CPU usage percentage at regular intervals.
2. It compares the usage against a **threshold value** (default: 80%).
3. If the usage exceeds the threshold, it prints an **alert message**.
4. The loop runs indefinitely until the user stops it with **Ctrl + C**.

---

## Example Output
```text
Monitoring CPU usage... (Press Ctrl+C to stop)
Alert! CPU usage exceeds threshold: 85%
Alert! CPU usage exceeds threshold: 90%
```

---

## Customization
You can change the `threshold` and `interval` in the `monitor_cpu()` function call:

```python
monitor_cpu(threshold=75, interval=2)
```

This will check CPU usage every 2 seconds and alert if it exceeds 75%.

---

## License
This program is provided for educational purposes and can be modified freely.
