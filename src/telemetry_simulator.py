import json
import random
import time
from datetime import datetime, timezone


DEVICE_ID = "simulated-iot-device-01"


def generate_telemetry():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "device_id": DEVICE_ID,
        "light_percent": round(random.uniform(10, 100), 2),
        "sound_db": round(random.uniform(25, 100), 2),
        "distance_cm": round(random.uniform(5, 200), 2),
    }


def evaluate_telemetry(data):
    alerts = []

    if data["light_percent"] > 85:
        alerts.append("HIGH_LIGHT")

    if data["sound_db"] > 80:
        alerts.append("HIGH_SOUND")

    if data["distance_cm"] < 20:
        alerts.append("OBJECT_TOO_CLOSE")

    data["status"] = "ALERT" if alerts else "NORMAL"
    data["alerts"] = alerts

    return data


def main():
    while True:
        telemetry = generate_telemetry()
        telemetry = evaluate_telemetry(telemetry)

        output = json.dumps(telemetry)

        print(output)

        with open("telemetry.log", "a") as log_file:
            log_file.write(output + "\n")

        time.sleep(10)


if __name__ == "__main__":
    main()
