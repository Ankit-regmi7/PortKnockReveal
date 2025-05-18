# 🖥️ Test VM Setup Guide

If you want to simulate real knocking:

1. Use any Linux VM (like Kali Linux or Ubuntu).
2. Create dummy listener using `nc`:
   ```bash
   nc -lvp 1111
   ```
3. Run your knock script from another terminal.
4. Monitor with:
   ```bash
   sudo tcpdump -i lo port 1111 or port 2222 or port 3333
   ```
