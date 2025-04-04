[Unit]
Description=App

[Service]
User=root
WorkingDirectory=/root/api/
ExecStart=/root/api/venv/bin/python3 -m uvicorn main:app --reload --port 8000 --host 0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target

systemctl daemon-reload
systemctl restart app

// up source len server
scp -r /api root@10.10.10.10:/root/api
// lay tren server ve 
scp -r root@10.10.10.10:/root/data ./


Description=Bot_Signal
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/bot/Bot_signal
ExecStart=/root/api/venv/bin/python3 bot_signal.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target



com.xworld.free.welfare.game.app.io
