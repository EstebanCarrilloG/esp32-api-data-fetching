
# ESP8266 PWM Control with API Integration

This project demonstrates how to use an ESP8266 microcontroller to control three PWM (Pulse Width Modulation) pins by fetching data from an API. The project connects to a Wi-Fi network, retrieves JSON data from a RESTful API, and adjusts the PWM duty cycle of connected pins based on the API response.

---

## Features

- **Wi-Fi Connectivity:** Connects to a specified Wi-Fi network using `network.WLAN`.
- **API Integration:** Fetches data from a REST API endpoint and parses the JSON response.
- **PWM Control:** Dynamically adjusts the duty cycles of three PWM-enabled pins (`D0`, `D2`, and `D4`) based on the received data.
- **Error Handling:** Includes basic error handling for API requests.

---

## Requirements

### Hardware:
- ESP8266 microcontroller.
- Devices connected to PWM-enabled pins (e.g., LEDs, motors, etc.).

### Software:
- MicroPython installed on the ESP8266.
- Libraries used:
  - `network`
  - `urequests` (MicroPython library for HTTP requests)
  - `json`
  - `machine`

---

## Pin Configuration

| GPIO | Pin   | Function      |
|------|-------|---------------|
| D0   | GPIO0 | PWM Output 1  |
| D2   | GPIO2 | PWM Output 2  |
| D4   | GPIO4 | PWM Output 3  |

---

## How It Works

### Wi-Fi Connection:
The script connects to a Wi-Fi network using the provided SSID and password.

```python
connectWifi(SSID, PASSWORD)
```

### API Data Retrieval:
It fetches JSON data from the API endpoint using `urequests`. If the request succeeds, the JSON data is processed.

### Data Mapping and PWM Adjustment:
The JSON data is parsed, and each value is mapped to the PWM range using the `map_range()` function.

```python
pwm0.duty(map_range(data[0].get("output1")))
pwm1.duty(map_range(data[0].get("output2")))
pwm2.duty(map_range(data[0].get("output3")))
```

### Continuous Updates:
The script continuously fetches data from the API and adjusts the PWM duty cycles in a loop, updating every second.

---

## Setup

1. **Edit Wi-Fi Credentials:**
   Replace the `SSID` and `PASSWORD` variables with your Wi-Fi network credentials.

2. **Set API Endpoint:**
   Replace `URL_API` with your API's URL.

3. **Upload the Script:**
   Upload the script to your ESP8266 using a tool like Thonny.

4. **Connect Hardware:**
   Connect the devices (e.g., LEDs, motors) to the specified GPIO pins.

5. **Run the Script:**
   Execute the script to establish a connection, fetch API data, and control the PWM pins.

---

## Example API Response

The API should return JSON data in the following format:

```json
[  
  {  
    "output1": 128,  
    "output2": 64,  
    "output3": 255  
  }  
]
```

---

## Notes

- The `map_range` function scales 8-bit values (0–255) to 10-bit PWM duty cycle values (0–1023).
- Ensure that the API is reachable and returns valid JSON data.
