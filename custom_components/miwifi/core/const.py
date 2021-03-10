DOMAIN = "miwifi"

DATA_UPDATED = "miwifi_data_updated"
DEVICES_UPDATED = "miwifi_device_updated"

STORAGE_VERSION = 1

DOMAINS = ["binary_sensor", "sensor", "light", "switch", "device_tracker"]
SCAN_INTERVAL = 10

CONF_LAST_ACTIVITY_DAYS = "last_activity_days"
DEFAULT_LAST_ACTIVITY_DAYS = 30

BASE_RESOURCE = "http://{ip}/cgi-bin/luci"

DEFAULT_USERNAME = "admin"
LOGIN_TYPE = 2
NONCE_TYPE = 0
PUBLIC_KEY = "a2ffa5c9be07488bbb04a3a47d3c5f6a"

DEFAULT_MANUFACTURER = "Xiaomi"

LEGACY_YAML_DEVICES = "legacy_known_devices.yaml"
DEVICE_TRACKER_ENTITY_ID_FORMAT = "device_tracker.{}"

BINARY_SENSORS = {
    "state": {"name": "State", "icon": "mdi:router-wireless", "skip_available": True},
    "repeater_mode": {"name": "Repeater mode", "icon": "mdi:repeat"},
    "wifi_state": {"name": "Wifi state", "icon": "mdi:wifi"},
    "wan_state": {"name": "Wan state", "icon": "mdi:wan", "device_class": "connectivity"},
}

SENSORS = {
    "devices": {"name": "Devices", "icon": "mdi:counter", "unit": "pcs"},
    "devices_lan": {"name": "Devices (lan)", "icon": "mdi:counter", "unit": "pcs"},
    "devices_5ghz": {"name": "Devices (5 Ghz)", "icon": "mdi:counter", "unit": "pcs"},
    "devices_2_4ghz": {"name": "Devices (2.4 Ghz)", "icon": "mdi:counter", "unit": "pcs"},
    "uptime": {"name": "Uptime", "icon": "mdi:timer-sand", "unit": None},
}

LIGHTS = {
    "led": {"name": "Led", "icon_off": "mdi:led-off", "icon_on": "mdi:led-on", "action_on": "led_on", "action_off": "led_off"}
}

SWITCHS = {
    "reboot": {"name": "Reboot", "icon_off": "mdi:restart", "icon_on": "mdi:restart", "action_on": "reboot", "action_off": "reboot", "blocked": False}
}

DEVICES_LIST = {}

CONNECTION_TO_SENSOR = {
    0: "devices_lan",
    1: "devices_2_4ghz",
    2: "devices_5ghz",
}

CONNECTION_RANGES = {
    0: "Lan",
    1: "2.4 Ghz",
    2: "5 Ghz"
}
