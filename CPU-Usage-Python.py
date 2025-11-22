import psutil
import time

def monitor_cpu_health(threshold_percent=80, interval_seconds=2):
    """
    Continuously monitors CPU usage and displays an alert if it exceeds a threshold.

    Args:
        threshold_percent (int): CPU usage percentage that triggers an alert.
        interval_seconds (int): Time interval (seconds) between checks.
    """

    print(f"\n Monitoring CPU usage... (Alert threshold: {threshold_percent}%)")
    print("Press Ctrl + C to stop monitoring.\n")

    try:
        while True:
            # Get CPU usage percentage averaged over interval_seconds
            cpu_usage = psutil.cpu_percent(interval=interval_seconds)

            # Alert if threshold exceeded
            if cpu_usage >= threshold_percent:
                print(f"  ALERT! CPU usage HIGH: {cpu_usage}%")
            else:
                print(f"CPU usage: {cpu_usage}%")

    except KeyboardInterrupt:
        print("\n CPU monitoring stopped by user.")
    except Exception as e:
        print(f"\n ERROR: An exception occurred: {e}")


# Run only if script is executed directly
if __name__ == "__main__":
    CPU_THRESHOLD = 80       # Alert threshold (%)
    MONITOR_INTERVAL = 2     # Check interval (seconds)

    monitor_cpu_health(
        threshold_percent=CPU_THRESHOLD,
        interval_seconds=MONITOR_INTERVAL
    )
