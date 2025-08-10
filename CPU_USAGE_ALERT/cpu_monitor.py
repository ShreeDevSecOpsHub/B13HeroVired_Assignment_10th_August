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
    monitor_cpu(threshold=10, interval=1)