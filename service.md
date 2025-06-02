[Service]
Type=simple
User=root
WorkingDirectory=/root/api/Bot
ExecStart=/root/venv/bin/python3 Bot.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target

[Unit]
Description=Shopee_Data
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/api/Data
ExecStart=/root/venv/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 6789
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
